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
        {reports.length === 0 ? (
          <div className="no-reports">No drift reports found. Trigger a scan to generate reports.</div>
        ) : (
          <div className="reports-grid">
            {reports.map(report => (
              <div key={report.id} className={`report-card ${report.drift_detected ? 'has-drift' : 'no-drift'}`}>
                <div className="report-header">
                  <h3>Scan Report</h3>
                  <span className={`status-badge ${report.drift_detected ? 'status-drift' : 'status-clean'}`}>
                    {report.drift_detected ? 'Drift Detected' : 'No Drift'}
                  </span>
                </div>
                <div className="report-stats">
                  <div className="stat">
                    <span className="stat-label">Total Resources</span>
                    <span className="stat-value">{report.total_resources}</span>
                  </div>
                  <div className="stat">
                    <span className="stat-label">Drifted</span>
                    <span className="stat-value">{report.drifted_resources}</span>
                  </div>
                </div>
                <div className="severity-breakdown">
                  <h4>Severity Breakdown</h4>
                  <div className="severity-stats">
                    <div className="severity-stat critical">
                      <span className="severity-label">Critical</span>
                      <span className="severity-value">{report.severity_critical}</span>
                    </div>
                    <div className="severity-stat high">
                      <span className="severity-label">High</span>
                      <span className="severity-value">{report.severity_high}</span>
                    </div>
                    <div className="severity-stat medium">
                      <span className="severity-label">Medium</span>
                      <span className="severity-value">{report.severity_medium}</span>
                    </div>
                    <div className="severity-stat low">
                      <span className="severity-label">Low</span>
                      <span className="severity-value">{report.severity_low}</span>
                    </div>
                  </div>
                </div>
                <p className="timestamp">Scanned: {new Date(report.scan_time).toLocaleString()}</p>
              </div>
            ))}
          </div>
        )}
      </main>
    </div>
  )
}

export default Dashboard
