import { useState, useEffect } from 'react'
import Dashboard from './components/Dashboard'
import { fetchDriftReports } from './services/api'
import { DriftReport } from './types'
import './App.css'

function App() {
  const [reports, setReports] = useState<DriftReport[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetchDriftReports()
      .then(setReports)
      .catch(err => setError(err.message))
      .finally(() => setLoading(false))
  }, [])

  return (
    <div className="App">
      <Dashboard reports={reports} loading={loading} error={error} />
    </div>
  )
}

export default App
