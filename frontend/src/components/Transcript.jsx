import React from 'react';
import axios from 'axios';

function Transcript({ sessionId }) {
  const downloadTranscript = async () => {
    if (!sessionId) return;

    try {
      const res = await axios.get(`http://localhost:8000/transcript/${sessionId}`);
      const transcript = res.data;
      if (!transcript.length) return;

      const text = transcript
        .map(msg => `${msg.role === 'user' ? 'You' : 'Agent'}: ${msg.message}`)
        .join('\n');
      const blob = new Blob([text], { type: 'text/plain' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'transcript.txt';
      a.click();
      URL.revokeObjectURL(url);
    } catch (err) {
      alert('Failed to download transcript.');
      console.error('Failed to download transcript:', err);
    }
  };

  return (
    <button onClick={downloadTranscript} disabled={!sessionId}>
      Download Transcript
    </button>
  );
}

export default Transcript;
