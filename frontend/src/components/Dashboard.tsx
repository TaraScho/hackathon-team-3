import { DriftReport } from '../types'

interface DashboardProps {
  reports: DriftReport[]
  loading: boolean
  error: string | null
}

function Dashboard({ reports, loading, error }: DashboardProps) {
  if (loading) {
    return (
      <div className="dashboard">
        <header className="header">
          <h1>DriftGuard</h1>
          <p>Infrastructure Drift Detection</p>
        </header>
        <div className="loading">Loading drift reports...</div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="dashboard">
        <header className="header">
          <h1>DriftGuard</h1>
          <p>Infrastructure Drift Detection</p>
        </header>
        <div className="error">Error: {error}</div>
      </div>
    )
  }

  return (
    <div className="dashboard">
      <header className="header">
        <h1>DriftGuard</h1>
        <p>Infrastructure Drift Detection</p>
      </header>
      <main className="main-content">
        <h2>Drift Reports</h2>
        <div className="reports-grid">
          {reports.map(report => (
            <div key={report.id} className="report-card">
              <h3>{report.resource_id}</h3>
              <p className="drift-type">Type: {report.drift_type}</p>
              <p className="severity">Severity: <span className={`severity-${report.severity}`}>{report.severity}</span></p>
              <p className="description">{report.description}</p>
              <p className="timestamp">{new Date(report.detected_at).toLocaleString()}</p>
            </div>
          ))}
        </div>
      </main>
    </div>
  )
}

export default Dashboard
