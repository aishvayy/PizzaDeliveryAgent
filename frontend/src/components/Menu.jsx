import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Menu() {
  const [menu, setMenu] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('http://localhost:8000/menu')
      .then(res => {
        setMenu(res.data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  if (loading) return <div>Loading menu...</div>;
  if (!menu) return <div>Could not load menu.</div>;

  return (
    <div style={{ margin: '20px 0', padding: 16, border: '1px solid #ccc', borderRadius: 8 }}>
      <h2>Pizza Menu</h2>
      <h3>Pizzas</h3>
      <ul>
        {menu.pizzas.map((pizza, idx) => (
          <li key={idx}>{pizza.name} — ${pizza.price.toFixed(2)}</li>
        ))}
      </ul>
      <h3>Toppings/Proteins/Greens</h3>
      <ul>
        {menu.toppings.map((topping, idx) => (
          <li key={idx}>{topping.name} — ${topping.price.toFixed(2)}</li>
        ))}
      </ul>
      <h3>Sides/Drinks</h3>
      <ul>
        {menu.sides.map((side, idx) => (
          <li key={idx}>{side.name} — ${side.price.toFixed(2)}</li>
        ))}
      </ul>
      <h3>Heat Levels</h3>
      <ul>
        {menu.heat_levels.map((level, idx) => (
          <li key={idx}>{level}</li>
        ))}
      </ul>
    </div>
  );
}

export default Menu;
