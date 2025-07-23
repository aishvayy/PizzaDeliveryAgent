import React, { useEffect, useState } from 'react';
import axios from 'axios';

function OrderSummary({ sessionId }) {
  const [order, setOrder] = useState(null);

  useEffect(() => {
    if (sessionId) {
      axios.get(`http://localhost:8000/order/${sessionId}`)
        .then(res => setOrder(res.data))
        .catch(() => setOrder(null));
    }
  }, [sessionId]);

  if (!order) return null;

  const downloadJSON = () => {
    const blob = new Blob([JSON.stringify(order, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'order.json';
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div style={{ margin: '20px 0', padding: 16, border: '1px solid #4caf50', borderRadius: 8 }}>
      <h2>Order Summary</h2>
      <pre style={{ background: '#f6f6f6', padding: 10, borderRadius: 4 }}>
        {JSON.stringify(order, null, 2)}
      </pre>
      <button onClick={downloadJSON}>Download JSON</button>
    </div>
  );
}

export default OrderSummary;
