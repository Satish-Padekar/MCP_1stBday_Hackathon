import React from 'react'
import PracticeFlow from './components/PracticeFlow'

export default function App(){
  return (
    <div className="app-root">
      <header className="header">
        <h1>MCP — Practice</h1>
      </header>
      <main className="container">
        <PracticeFlow />
      </main>
    </div>
  )
}
