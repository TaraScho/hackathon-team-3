import { DriftReport } from '../types'

const API_BASE_URL = '/api'

export async function fetchDriftReports(): Promise<DriftReport[]> {
  try {
    const response = await fetch(`${API_BASE_URL}/drift/reports`)

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    const data = await response.json()
    return data.reports || []
  } catch (error) {
    console.error('Error fetching drift reports:', error)
    throw error
  }
}

export async function triggerDriftScan(): Promise<void> {
  try {
    const response = await fetch(`${API_BASE_URL}/drift/scan`, {
      method: 'POST'
    })

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
  } catch (error) {
    console.error('Error triggering drift scan:', error)
    throw error
  }
}
