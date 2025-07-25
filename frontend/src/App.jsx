import React, { useState } from 'react';
import Menu from './components/Menu';
import Chat from './components/Chat';
import OrderSummary from './components/OrderSummary';
import Transcript from './components/Transcript';

function App() {
  const [sessionId, setSessionId] = useState(null);
  const [showMenu, setShowMenu] = useState(false);
  const [messageCount, setMessageCount] = useState(0);

  return (
    <div style={{ maxWidth: 800, margin: '0 auto', padding: 20 }}>
      <h1>Pizza Delivery Agent</h1>
      <button onClick={() => setShowMenu(!showMenu)}>
        {showMenu ? 'Hide Menu' : 'Show Menu'}
      </button>
      {showMenu && <Menu />}
      <Chat sessionId={sessionId} setSessionId={setSessionId} setMessageCount={setMessageCount}/>
      <OrderSummary sessionId={sessionId} />
      <Transcript sessionId={sessionId} messageCount={messageCount} />
    </div>
  );
}

export default App;
