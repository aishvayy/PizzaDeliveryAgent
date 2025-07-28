
https://github.com/user-attachments/assets/37494b2f-d131-4b4d-9c0a-f6a88ca62893
# AI Pizza Delivery Agent

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

## Working dialog and Transcript

Video of the working dialog: 

https://github.com/user-attachments/assets/9918cdb9-fa66-4c6e-a640-16adf3731d19

Transcript is available upon hitting the download button, attached transcript for the demo conversation can be found here: 
(https://github.com/user-attachments/files/21471049/transcript.txt)

Screenshot of the order saved in a structured JSON format, available on the backend on the /order/sessionId path: <img width="632" height="659" alt="Screenshot 2025-07-28 at 3 58 56 PM" src="https://github.com/user-attachments/assets/fdcb2cfc-5b62-4b9b-9b55-fb979870e9c1" />

