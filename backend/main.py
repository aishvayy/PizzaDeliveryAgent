import re
import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Dict
import uuid
from dotenv import load_dotenv
import os
from models import Order, TranscriptMessage, ChatRequest
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Load menu from file
with open("menu.json", "r") as f:
    MENU = json.load(f)

# In-memory session storage
db_sessions: Dict[str, Dict] = {}



@app.get("/menu")
def get_menu():
    return MENU

def call_llm(messages):
    prompt = "\n".join([f"{m['role']}: {m['content']}" for m in messages])
    model = genai.GenerativeModel('gemini-2.5-pro')
    response = model.generate_content(prompt)
    return response.text

def extract_json_from_text(text):
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            return None
    return None

def remove_json_from_message(message):
    # Remove any JSON code block from the message
    return re.sub(r'```json[\s\S]*?```', '', message, flags=re.MULTILINE)

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
    system_prompt = {"role": "system", "content": "You are a friendly and helpful pizza ordering assistant for a delivery service. Guide the customer through placing an order step by step, asking only one or two questions at a time. Do not overwhelm the customer with too many questions at once.\n\nFollow this flow:\n1. Greet the customer and ask for their name.\n2. Show the pizza menu and ask which pizza(s) they would like to order. When showing the menu, use the menu provided below and present it in a clear, readable, plain-text format.\n3. For each pizza, ask if they want extra toppings or proteins (e.g., grilled chicken, tofu, etc.).\n4. For each pizza, ask for the preferred heat level (Mild, Medium, Spicy, Very Spicy).\n5. Ask about dietary preferences or allergies (e.g., vegan, vegetarian, gluten-free, or any allergies).\n6. If the customer orders meat, ask if they require halal meat.\n7. Ask if they want any sides or drinks.\n8. Always ask for the delivery address before confirming or completing the order.\n9. Summarize the order, including all details, and ask for confirmation.\n10. If confirmed, thank the customer by name and display a message that the order is placed and will be delivered soon.\n\nImportant Instructions:\n- Only offer pizzas, toppings, sides, and drinks that are present in the provided menu. Do not invent or suggest items that are not in the menu.\n- Do not hallucinate or add items the user did not request.\n- Do not display the JSON order in the chat. Only show a clear, human-friendly summary to the user. Output the JSON only for the system to record, not for the user to see.\n- If the user provides a string that looks like an address (e.g., contains a street name, number, or city), treat it as the delivery address, even if the user does not explicitly say it is their address.\n- Do not repeat questions if the user has already provided the required information.\n- **Do not use asterisks, markdown, or any special formatting (such as bold or italics) in your responses. Use only plain text for all messages, menus, and summaries.**\n- Always be polite and conversational. If any information is missing, ask follow-up questions. Present the menu in a clear, readable, plain-text format when needed.\n\nMenu (with prices):\nPizzas:\n- Margherita — $10.00\n- Pepperoni — $11.00\n- Veggie Supreme — $11.00\n- BBQ Chicken — $12.00\n- Vegan Delight — $11.00\n\nToppings/Proteins/Greens:\n- Grilled Chicken — $2.00\n- Pepperoni — $2.00\n- Spicy Beef — $2.00\n- Tofu (vegan) — $1.50\n- Tuna — $2.00\n- Spinach — $1.00\n- Arugula — $1.00\n- Broccoli — $1.00\n- Bell Peppers — $1.00\n- Olives — $1.00\n- Mushrooms — $1.00\n- Jalapeños — $1.00\n- Extra Cheese — $1.50\n- BBQ Sauce — $0.50\n\nSides/Drinks:\n- Garlic Bread — $3.00\n- Vegan Garlic Bread — $3.00\n- Cola (0.5L) — $2.00\n- Water (0.5L) — $1.50\n\nHeat Levels: Mild, Medium, Spicy, Very Spicy\n\nInstructions:\n- Always be polite and conversational.\n- If any information is missing, ask follow-up questions.\n- If the customer has dietary restrictions or allergies, warn them about any menu items that may not be suitable.\n- At the end, present a clear, itemized order summary with the total price, including the customer’s name and delivery address, and ask for confirmation.\n- If the order is confirmed, thank the customer by name and display a message that the order is placed and will be delivered soon.\n- At the end, output the order in a structured JSON format for the system to record, but do not show the JSON to the user."}
    messages.insert(0, system_prompt)

    # Call LLM
    agent_message = call_llm(messages)
    agent_message = remove_json_from_message(agent_message)
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
