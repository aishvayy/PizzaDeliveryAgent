# 🍕 AI Pizza Delivery Agent

An AI-powered pizza ordering agent with a modern React frontend and a FastAPI backend, using Google Gemini (AI Studio) for natural dialog.

---

## Features

- Step-by-step, conversational pizza ordering agent
- Menu, toppings, sides, and dietary preferences
- Order summary and transcript download
- Modern React frontend, FastAPI backend
- Uses Google Gemini (AI Studio) LLM via API

---

## Requirements

- Python 3.8+
- Node.js 16+
- Google Gemini API key (from [Google AI Studio](https://aistudio.google.com/app/apikey))
- (macOS, Windows, or Linux)

---

## Setup Instructions

### 1. **Clone the Repository**

```bash
git clone https://github.com/aishvayy/PizzaDeliveryAgent.git
```

---

### 2. **Backend Setup**

```bash
cd backend
python3 -m pip install -r requirements.txt
```

#### **Set up your Gemini API key**
- Create a `.env` file in the `backend/` directory with this line:
  ```
  GEMINI_API_KEY=your_actual_gemini_api_key_here
  ```
- The backend uses `python-dotenv` to load this key automatically.

#### **Start the Backend**

```bash
uvicorn main:app --reload
```

---

### 3. **Frontend Setup**

```bash
cd ../frontend
npm install
npm run dev
```

- Open [http://localhost:5173](http://localhost:5173) in your browser.

---

## Usage

- Click “Show Menu” to view the pizza menu.
- Chat with the agent to place your order.
- After completing your order, download the order summary (JSON) and transcript (TXT).

---

## Project Structure

```
backend/    # FastAPI backend, menu, Gemini LLM integration
frontend/   # React frontend (Vite)
```

---

## Troubleshooting

- **CORS errors:** Make sure the backend is running and CORS is enabled (already set up in `main.py`).
- **Gemini errors:** Ensure your API key is valid and you have access to the Gemini models.
- **Port conflicts:** Default backend is on `8000`, frontend on `5173`.

---

## .gitignore Recommendations

```
# Python
__pycache__/
*.pyc

# Node
node_modules/
dist/

# Mac
.DS_Store

# Env
.env
```
---

## Credits

- [Google Gemini (AI Studio)](https://aistudio.google.com/) for LLM
- [FastAPI](https://fastapi.tiangolo.com/)
- [React](https://react.dev/) 

---

## Working dialog

<img width="410" height="568" alt="Screenshot 2025-07-25 at 1 34 28 PM" src="https://github.com/user-attachments/assets/f52b5c91-ba0c-4b89-953c-1f38b781937e" />
