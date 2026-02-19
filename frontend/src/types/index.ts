export interface DriftReport {
  id: string
  resource_id: string
  drift_type: string
  severity: 'low' | 'medium' | 'high' | 'critical'
  description: string
  detected_at: string
  expected_value?: string
  actual_value?: string
  metadata?: Record<string, any>
}

export interface DriftScanRequest {
  resource_type?: string
  resource_ids?: string[]
  scan_all?: boolean
}
