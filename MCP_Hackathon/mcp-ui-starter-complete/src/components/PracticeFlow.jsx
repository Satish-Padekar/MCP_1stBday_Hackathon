import React, {useState} from 'react'

export default function PracticeFlow(){
  const [problems, setProblems] = useState([])
  const [answers, setAnswers] = useState({})
  const [results, setResults] = useState(null)

  async function load(){
    const res = await fetch('http://localhost:8000/api/practice', {method: 'POST', headers: {'content-type':'application/json'}, body: JSON.stringify({count:3})})
    const j = await res.json()
    setProblems(j.problems)
    setResults(null)
  }

  function handleChange(pid, v){
    setAnswers(a => ({...a, [pid]: v}))
  }

  async function submit(){
    const attempts = problems.map(p => ({problem_id: p.id, answer: answers[p.id] || '', _solution: p.solution}))
    const res = await fetch('http://localhost:8000/api/check', {method:'POST', headers:{'content-type':'application/json'}, body: JSON.stringify(attempts)})
    const j = await res.json()
    setResults(j.results)
  }

  return (
    <div style={{maxWidth:680}}>
      <div style={{display:'flex', gap:8}}>
        <button onClick={load}>Load practice</button>
      </div>

      <div style={{marginTop:16}}>
        {problems.map(p => (
          <div key={p.id} style={{padding:12, borderRadius:8, background:'#fff', marginBottom:8}}>
            <div style={{fontWeight:600}}>{p.statement}</div>
            <input style={{marginTop:8, padding:8, width:'100%'}} onChange={e => handleChange(p.id, e.target.value)} />
          </div>
        ))}
      </div>

      {problems.length>0 && <button onClick={submit}>Submit</button>}

      {results && (
        <div style={{marginTop:16}}>
          <h3>Results</h3>
          {results.map(r => (
            <div key={r.problem_id}>{r.problem_id} — {r.score}/{r.max_score} — {r.feedback}</div>
          ))}
        </div>
      )}
    </div>
  )
}
