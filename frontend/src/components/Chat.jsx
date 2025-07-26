import React, { useState } from 'react';
import axios from 'axios';

function Chat({ sessionId, setSessionId }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const sendMessage = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMsg = { role: 'user', message: input };
    setMessages((msgs) => [...msgs, userMsg]);
    setLoading(true);

    try {
      const res = await axios.post('http://localhost:8000/chat', {
        message: input,
        session_id: sessionId,
      });
      setSessionId(res.data.session_id);

      const agentMsg = { role: 'agent', message: res.data.response };
      setMessages((msgs) => [...msgs, agentMsg]);
    } catch (err) {
      setMessages((msgs) => [
        ...msgs,
        { role: 'agent', message: 'Error: Could not get response from agent.' },
      ]);
    }
    setInput('');
    setLoading(false);
  };

  return (
    <div style={{ margin: '20px 0', padding: 16, border: '1px solid #ccc', borderRadius: 8 }}>
      <h2>Chat with Pizza Agent</h2>
      <div style={{ minHeight: 200, marginBottom: 10 }}>
        {messages.map((msg, idx) => (
          <div key={idx} style={{ textAlign: msg.role === 'user' ? 'right' : 'left' }}>
            <b>{msg.role === 'user' ? 'You' : 'Agent'}:</b> {msg.message}
          </div>
        ))}
        {loading && <div><i>Agent is typing...</i></div>}
      </div>
      <form onSubmit={sendMessage} style={{ display: 'flex', gap: 8 }}>
        <input
          type="text"
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Type your message..."
          style={{ flex: 1 }}
          disabled={loading}
        />
        <button type="submit" disabled={loading || !input.trim()}>Send</button>
      </form>
    </div>
  );
}

export default Chat;
