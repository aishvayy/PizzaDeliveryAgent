import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Transcript({ sessionId }) {
  const [transcript, setTranscript] = useState([]);

  useEffect(() => {
    if (sessionId) {
      axios.get(`http://localhost:8000/transcript/${sessionId}`)
        .then(res => setTranscript(res.data))
        .catch(() => setTranscript([]));
    }
  }, [sessionId]);

  if (!transcript.length) return null;

  const downloadTranscript = () => {
    const text = transcript.map(msg => `${msg.role === 'user' ? 'You' : 'Agent'}: ${msg.message}`).join('\n');
    const blob = new Blob([text], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'transcript.txt';
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div style={{ margin: '20px 0', padding: 16, border: '1px solid #2196f3', borderRadius: 8 }}>
      <h2>Transcript</h2>
      <pre style={{ background: '#f6f6f6', padding: 10, borderRadius: 4 }}>
        {transcript.map((msg, idx) => (
          <div key={idx}>
            <b>{msg.role === 'user' ? 'You' : 'Agent'}:</b> {msg.message}
          </div>
        ))}
      </pre>
      <button onClick={downloadTranscript}>Download Transcript</button>
    </div>
  );
}

export default Transcript;
