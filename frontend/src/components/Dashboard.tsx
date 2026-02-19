import { useState } from 'react'
import { DriftReport, Repository } from '../types'
import { addRepository, triggerDriftScan } from '../services/api'
import AddRepositoryModal from './AddRepositoryModal'

interface DashboardProps {
  reports: DriftReport[]
  repositories: Repository[]
  loading: boolean
  error: string | null
  onRepositoryAdded: () => void
}

function Dashboard({ reports, repositories, loading, error, onRepositoryAdded }: DashboardProps) {
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [scanningRepoId, setScanningRepoId] = useState<string | null>(null)

  // Create a map of repository ID to repository for quick lookup
  const repoMap = new Map(repositories.map(repo => [repo.id, repo]))

  const handleAddRepository = async (name: string, url: string, branch: string) => {
    await addRepository(name, url, branch)
    onRepositoryAdded()
  }

  const handleScanRepository = async (repositoryId: string) => {
    setScanningRepoId(repositoryId)
    try {
      await triggerDriftScan(repositoryId)
      setTimeout(() => {
        onRepositoryAdded()
      }, 2000)
    } catch (err) {
      console.error('Failed to trigger scan:', err)
    } finally {
      setScanningRepoId(null)
    }
  }
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
        <section className="repositories-section">
          <div className="section-header">
            <h2>Monitored Repositories</h2>
            <button className="add-repo-btn" onClick={() => setIsModalOpen(true)}>
              + Add Repository
            </button>
          </div>
          {repositories.length === 0 ? (
            <div className="no-repositories">No repositories configured. Add a repository to start monitoring.</div>
          ) : (
            <div className="repositories-list">
              {repositories.map(repo => (
                <div key={repo.id} className="repository-item">
                  <div className="repo-info">
                    <h3 className="repo-name">{repo.name}</h3>
                    <a href={repo.url} target="_blank" rel="noopener noreferrer" className="repo-url">
                      {repo.url}
                    </a>
                    <div className="repo-meta">
                      <span className="repo-branch">Branch: {repo.branch}</span>
                      {repo.last_scan_at ? (
                        <span className="repo-last-scan">Last scan: {new Date(repo.last_scan_at).toLocaleString()}</span>
                      ) : (
                        <span className="repo-last-scan">Never scanned</span>
                      )}
                    </div>
                  </div>
                  <button
                    className="scan-btn"
                    onClick={() => handleScanRepository(repo.id)}
                    disabled={scanningRepoId === repo.id}
                  >
                    {scanningRepoId === repo.id ? 'Scanning...' : 'Scan Now'}
                  </button>
                </div>
              ))}
            </div>
          )}
        </section>

        <AddRepositoryModal
          isOpen={isModalOpen}
          onClose={() => setIsModalOpen(false)}
          onAdd={handleAddRepository}
        />

        <h2>Drift Reports</h2>
        {reports.length === 0 ? (
          <div className="no-reports">No drift reports found. Trigger a scan to generate reports.</div>
        ) : (
          <div className="reports-grid">
            {reports.map(report => (
              <div key={report.id} className={`report-card ${report.drift_detected ? 'has-drift' : 'no-drift'}`}>
                <div className="report-header">
                  <div className="report-title-section">
                    <h3>Scan Report</h3>
                    {repoMap.has(report.repository_id) ? (
                      <a
                        href={repoMap.get(report.repository_id)!.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="repository-link"
                      >
                        {repoMap.get(report.repository_id)!.name}
                      </a>
                    ) : (
                      <p className="repository-id">Repository: {report.repository_id}</p>
                    )}
                  </div>
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
