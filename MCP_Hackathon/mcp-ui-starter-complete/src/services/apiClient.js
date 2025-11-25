const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

export async function generatePractice(count=3){
  const res = await fetch(`${API_BASE}/api/practice`, {method:'POST', headers:{'content-type':'application/json'}, body: JSON.stringify({count})})
  return res.json()
}

export async function checkAttempts(attempts){
  const res = await fetch(`${API_BASE}/api/check`, {method:'POST', headers:{'content-type':'application/json'}, body: JSON.stringify(attempts)})
  return res.json()
}
