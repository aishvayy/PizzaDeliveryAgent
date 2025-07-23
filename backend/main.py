import ollama
import re
import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Dict
import uuid
from models import Order, TranscriptMessage, ChatRequest
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Load menu from file
with open("menu.json", "r") as f:
    MENU = json.load(f)

# In-memory session storage
db_sessions: Dict[str, Dict] = {}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/menu")
def get_menu():
    return MENU

def call_llm(messages):
    prompt = "\n".join([f"{m['role']}: {m['content']}" for m in messages])
    response = ollama.generate(model='llama2', prompt=prompt)
    return response['response']

def extract_json_from_text(text):
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            return None
    return None

@app.post("/chat")
def chat(chat_request: ChatRequest):
    user_message = chat_request.message
    session_id = chat_request.session_id
    if not session_id or session_id not in db_sessions:
        session_id = str(uuid.uuid4())
        db_sessions[session_id] = {"order": None, "transcript": []}
    db_sessions[session_id]["transcript"].append({"role": "user", "message": user_message})

    # Build message history for LLM
    messages = [{"role": m["role"], "content": m["message"]} for m in db_sessions[session_id]["transcript"]]
    system_prompt = {"role": "system", "content": "You are a friendly and helpful pizza ordering assistant for a delivery service. Guide the customer through placing an order step by step, asking only one or two questions at a time. Do not overwhelm the customer with too many questions at once.\n\nFollow this flow:\n1. Greet the customer and ask for their name.\n2. Show the pizza menu and ask which pizza(s) they would like to order.\n3. For each pizza, ask if they want extra toppings or proteins (e.g., grilled chicken, tofu, etc.).\n4. For each pizza, ask for the preferred heat level (Mild, Medium, Spicy, Very Spicy).\n5. Ask about dietary preferences or allergies (e.g., vegan, vegetarian, gluten-free, or any allergies).\n6. If the customer orders meat, ask if they require halal meat.\n7. Ask if they want any sides or drinks.\n8. Ask for the delivery address.\n9. Summarize the order, including all details, and ask for confirmation.\n10. If confirmed, thank the customer by name and display a message that the order is placed and will be delivered soon.\n11. At the end, output the order in a structured JSON format containing all order details.\n\nAlways be polite and conversational. If any information is missing, ask follow-up questions. Present the menu in a clear, readable format when needed."}
    messages.insert(0, system_prompt)

    # Call LLM
    agent_message = call_llm(messages)
    db_sessions[session_id]["transcript"].append({"role": "agent", "message": agent_message})

    # Extract and store order JSON if present
    order_json = extract_json_from_text(agent_message)
    if order_json:
        db_sessions[session_id]["order"] = order_json

    return {"session_id": session_id, "response": agent_message}

@app.get("/order/{session_id}")
def get_order(session_id: str):
    session = db_sessions.get(session_id)
    if session and session["order"]:
        return session["order"]
    return JSONResponse(status_code=404, content={"error": "Order not found"})

@app.get("/transcript/{session_id}")
def get_transcript(session_id: str):
    session = db_sessions.get(session_id)
    if session:
        return session["transcript"]
    return JSONResponse(status_code=404, content={"error": "Transcript not found"})
