# 🍕 AI Pizza Delivery Agent

An AI-powered pizza ordering agent with a modern React frontend and a FastAPI backend, using a local LLM (Ollama) for natural dialog.

---

## Features

- Step-by-step, conversational pizza ordering agent
- Menu, toppings, sides, and dietary preferences
- Order summary and transcript download
- Modern React frontend, FastAPI backend
- Runs locally with free/open-source LLMs (Ollama)

---

## Requirements

- Python 3.8+
- Node.js 16+
- [Ollama](https://ollama.com/) (for local LLM)
- (macOS, Windows, or Linux)

---

## Setup Instructions

### 1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

---

### 2. **Backend Setup**

```bash
cd backend
python3 -m pip install -r requirements.txt
```

#### **Start the Backend**

```bash
uvicorn main:app --reload
```

---

### 3. **Ollama Setup**

- Download and install Ollama from [https://ollama.com/download](https://ollama.com/download) (macOS, Windows, Linux).
- Start the Ollama server:
  ```bash
  ollama serve
  ```
- Download the Llama 2 model (or another supported model):
  ```bash
  ollama pull llama2
  ```
  *(You only need to do this once.)*

---

### 4. **Frontend Setup**

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
backend/    # FastAPI backend, menu, LLM integration
frontend/   # React frontend (Vite)
```

---

## Troubleshooting

- **CORS errors:** Make sure the backend is running and CORS is enabled (already set up in `main.py`).
- **Ollama errors:** Ensure `ollama serve` is running and the model is downloaded.
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

- [Ollama](https://ollama.com/) for local LLMs
- [FastAPI](https://fastapi.tiangolo.com/)
- [React](https://react.dev/) 