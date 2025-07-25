import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Transcript({ sessionId, messageCount }) {
  const [transcript, setTranscript] = useState([]);

  useEffect(() => {
    if (sessionId) {
      axios.get(`http://localhost:8000/transcript/${sessionId}`)
        .then(res => setTranscript(res.data))
        .catch(() => setTranscript([]));
    }
  }, [sessionId, messageCount]);

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
    <button onClick={downloadTranscript}>Download Transcript</button>
  );
}

export default Transcript;
