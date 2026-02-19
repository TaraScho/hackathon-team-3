import { useState } from 'react'

interface AddRepositoryModalProps {
  isOpen: boolean
  onClose: () => void
  onAdd: (name: string, url: string, branch: string) => void
}

function AddRepositoryModal({ isOpen, onClose, onAdd }: AddRepositoryModalProps) {
  const [name, setName] = useState('')
  const [url, setUrl] = useState('')
  const [branch, setBranch] = useState('main')
  const [error, setError] = useState<string | null>(null)
  const [isSubmitting, setIsSubmitting] = useState(false)

  if (!isOpen) return null

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setError(null)

    if (!name.trim() || !url.trim() || !branch.trim()) {
      setError('All fields are required')
      return
    }

    if (!url.match(/^https?:\/\/.+/)) {
      setError('Please enter a valid Git URL (http:// or https://)')
      return
    }

    setIsSubmitting(true)
    try {
      await onAdd(name.trim(), url.trim(), branch.trim())
      setName('')
      setUrl('')
      setBranch('main')
      onClose()
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to add repository')
    } finally {
      setIsSubmitting(false)
    }
  }

  const handleClose = () => {
    if (!isSubmitting) {
      setName('')
      setUrl('')
      setBranch('main')
      setError(null)
      onClose()
    }
  }

  return (
    <div className="modal-overlay" onClick={handleClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h2>Add Repository</h2>
          <button className="modal-close" onClick={handleClose} disabled={isSubmitting}>
            ×
          </button>
        </div>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="repo-name">Repository Name</label>
            <input
              id="repo-name"
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="my-infrastructure"
              disabled={isSubmitting}
              autoFocus
            />
          </div>
          <div className="form-group">
            <label htmlFor="repo-url">Git URL</label>
            <input
              id="repo-url"
              type="text"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              placeholder="https://github.com/username/repo.git"
              disabled={isSubmitting}
            />
          </div>
          <div className="form-group">
            <label htmlFor="repo-branch">Branch</label>
            <input
              id="repo-branch"
              type="text"
              value={branch}
              onChange={(e) => setBranch(e.target.value)}
              placeholder="main"
              disabled={isSubmitting}
            />
          </div>
          {error && <div className="form-error">{error}</div>}
          <div className="modal-actions">
            <button
              type="button"
              className="btn-secondary"
              onClick={handleClose}
              disabled={isSubmitting}
            >
              Cancel
            </button>
            <button
              type="submit"
              className="btn-primary"
              disabled={isSubmitting}
            >
              {isSubmitting ? 'Adding...' : 'Add Repository'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default AddRepositoryModal
