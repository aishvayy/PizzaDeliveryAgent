from pydantic import BaseModel
from typing import List, Optional

class MenuItem(BaseModel):
    name: str
    price: float

class PizzaOrder(BaseModel):
    pizza: str
    heat_level: str
    halal_meat: Optional[bool] = False
    toppings: List[str] = []
    price: float

class SideOrder(BaseModel):
    item: str
    price: float

class Order(BaseModel):
    customer_name: str
    delivery_address: str
    dietary_preferences: List[str] = []
    allergens: List[str] = []
    order: List[PizzaOrder]
    sides: List[SideOrder] = []
    total_price: float

class TranscriptMessage(BaseModel):
    role: str  # 'agent' or 'user'
    message: str
    timestamp: Optional[str] = None

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None 