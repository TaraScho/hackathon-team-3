import { DriftReport, Repository } from '../types'

const API_BASE_URL = '/api'

export async function fetchDriftReports(): Promise<DriftReport[]> {
  try {
    const response = await fetch(`${API_BASE_URL}/drift`)

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    const data = await response.json()
    return Array.isArray(data) ? data : (data.reports || [])
  } catch (error) {
    console.error('Error fetching drift reports:', error)
    throw error
  }
}

export async function fetchRepositories(): Promise<Repository[]> {
  try {
    const response = await fetch(`${API_BASE_URL}/repositories`)

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    return await response.json()
  } catch (error) {
    console.error('Error fetching repositories:', error)
    throw error
  }
}

export async function triggerDriftScan(repositoryId?: string): Promise<void> {
  try {
    const response = await fetch(`${API_BASE_URL}/drift/scan`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(repositoryId ? { repository_id: repositoryId } : {})
    })

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
  } catch (error) {
    console.error('Error triggering drift scan:', error)
    throw error
  }
}

export async function addRepository(name: string, url: string, branch: string): Promise<Repository> {
  try {
    const response = await fetch(`${API_BASE_URL}/repositories`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ name, git_url: url, branch })
    })

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}))
      throw new Error(errorData.detail || `HTTP error! status: ${response.status}`)
    }

    return await response.json()
  } catch (error) {
    console.error('Error adding repository:', error)
    throw error
  }
}
