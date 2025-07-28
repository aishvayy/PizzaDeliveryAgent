[transcript.txt](https://github.com/user-attachments/files/21471006/transcript.txt)# AI Pizza Delivery Agent

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

Transcript is available upon hitting the download button: 
[transcript.txt](https://github.com/user-attachments/files/21471049/transcript.txt)
You: Hey
Agent: Hello! Welcome to our pizza delivery service. What's your name?
You: Vaishnavi
Agent: Nice to meet you, Vaishnavi!

Here is our pizza menu:

Pizzas:
- Margherita — $10.00
- Pepperoni — $11.00
- Veggie Supreme — $11.00
- BBQ Chicken — $12.00
- Vegan Delight — $11.00

Which pizza(s) would you like to order today?
You: Margherita
Agent: Great choice! One Margherita pizza.

Would you like to add any extra toppings or proteins to your Margherita pizza, such as Grilled Chicken, Tofu, Spinach, or Extra Cheese?
You: Spinach and Grilled Chicken
Agent: Okay, adding Spinach and Grilled Chicken to your Margherita pizza.

What heat level would you prefer for your Margherita pizza? Your options are Mild, Medium, Spicy, or Very Spicy.
You: Spicy
Agent: Got it, Spicy for your Margherita pizza.

Before we go further, do you have any dietary preferences or allergies I should be aware of, like vegan, vegetarian, gluten-free, or any specific allergies?
You: No allergies
Agent: Thank you for letting me know.

You've ordered Grilled Chicken. Do you require halal meat for your pizza?
You: No
Agent: Alright. Would you like to add any sides or drinks to your order? We have Garlic Bread, Vegan Garlic Bread, Cola, and Water.
You: Cola and Garlic Bread
Agent: Okay, adding Cola and Garlic Bread to your order.

Could you please provide your delivery address?
You: Dropkeweg 2A, 12353, Berlin
Agent: Thank you! Your delivery address is Dropkeweg 2A, 12353, Berlin.

Here is a summary of your order:

Customer Name: Vaishnavi
Delivery Address: Dropkeweg 2A, 12353, Berlin

Your Order:
- 1 Margherita Pizza with Spinach and Grilled Chicken, Spicy heat level ($10.00 + $1.00 + $2.00 = $13.00)
- 1 Cola ($2.00)
- 1 Garlic Bread ($3.00)

Total price: $18.00

Does everything look correct? Please confirm your order.
You: Yes, confirm
Agent: Thank you, Vaishnavi! Your order has been placed and will be delivered to Dropkeweg 2A, 12353, Berlin soon. Enjoy your meal!
{
  "customer_name": "Vaishnavi",
  "delivery_address": "Dropkeweg 2A, 12353, Berlin",
  "order_details": [
    {
      "item": "Margherita",
      "type": "pizza",
      "base_price": 10.00,
      "toppings": [
        {"name": "Spinach", "price": 1.00},
        {"name": "Grilled Chicken", "price": 2.00}
      ],
      "heat_level": "Spicy",
      "halal_meat_required": false,
      "subtotal": 13.00
    },
    {
      "item": "Cola",
      "type": "drink",
      "price": 2.00
    },
    {
      "item": "Garlic Bread",
      "type": "side",
      "price": 3.00
    }
  ],
  "dietary_preferences_or_allergies": "No allergies",
  "total_price": 18.00
}
Screenshot of the order saved in a structured JSON format, available on the backend: <img width="632" height="659" alt="Screenshot 2025-07-28 at 3 58 56 PM" src="https://github.com/user-attachments/assets/fdcb2cfc-5b62-4b9b-9b55-fb979870e9c1" />

