export interface DriftReport {
  id: string
  repository_id: string
  scan_time: string
  drift_detected: boolean
  total_resources: number
  drifted_resources: number
  severity_critical: number
  severity_high: number
  severity_medium: number
  severity_low: number
  details: Record<string, any>
}

export interface DriftScanRequest {
  resource_type?: string
  resource_ids?: string[]
  scan_all?: boolean
}

export interface Repository {
  id: string
  name: string
  url: string
  branch: string
  created_at: string
  last_scan_at: string | null
}
