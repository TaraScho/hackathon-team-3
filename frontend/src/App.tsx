import { useState, useEffect } from 'react'
import Dashboard from './components/Dashboard'
import { fetchDriftReports, fetchRepositories } from './services/api'
import { DriftReport, Repository } from './types'
import './App.css'

function App() {
  const [reports, setReports] = useState<DriftReport[]>([])
  const [repositories, setRepositories] = useState<Repository[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  const loadData = () => {
    Promise.all([
      fetchDriftReports(),
      fetchRepositories()
    ])
      .then(([reportsData, reposData]) => {
        setReports(reportsData)
        setRepositories(reposData)
      })
      .catch(err => setError(err.message))
      .finally(() => setLoading(false))
  }

  useEffect(() => {
    loadData()
  }, [])

  return (
    <div className="App">
      <Dashboard
        reports={reports}
        repositories={repositories}
        loading={loading}
        error={error}
        onRepositoryAdded={loadData}
      />
    </div>
  )
}

export default App
