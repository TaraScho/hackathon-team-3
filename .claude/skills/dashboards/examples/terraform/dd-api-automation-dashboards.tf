resource "datadog_dashboard" "stately_dashboard" {
  description  = "Created using the Datadog provider in Terraform"
  layout_type  = "ordered"
  reflow_type  = "fixed"
  title        = "Stately! Dashboard"

  widget {
    manage_status_definition {
      color_preference    = "background"
      display_format      = "counts"
      hide_zero_counts    = "true"
      query               = "service:\"redis-session-cache\""
      show_last_triggered = "false"
      show_priority       = "false"
      sort                = "status,asc"
      summary_type        = "monitors"
      title               = "Stately Alerts"
    }

    widget_layout {
      height          = "2"
      width           = "3"
      x               = "0"
      y               = "0"
    }
  }

  widget {
    alert_graph_definition {
      alert_id   = datadog_monitor.redis_cpu.id
      live_span  = "30m"
      title      = "Redis System CPU Usage"
      title_size = "16"
      viz_type   = "timeseries"
    }

    widget_layout {
      height          = "2"
      width           = "4"
      x               = "3"
      y               = "0"
    }
  }

  widget {
    list_stream_definition {
      request {
        columns {
          field = "content"
          width = "compact"
        }

        columns {
          field = "host"
          width = "auto"
        }

        columns {
          field = "service"
          width = "auto"
        }

        columns {
          field = "source"
          width = "auto"
        }

        columns {
          field = "status_line"
          width = "auto"
        }

        columns {
          field = "timestamp"
          width = "auto"
        }

        query {
          data_source  = "logs_stream"
          query_string = "status:error"

          sort {
            column = "timestamp"
            order  = "desc"
          }

          storage = "hot"
        }

        response_format = "event_list"
      }

      title      = "Stately Error Logs"
      title_size = "16"
    }

    widget_layout {
      height          = "5"
      width           = "5"
      x               = "7"
      y               = "0"
    }
  }

  widget {
    note_definition {
      background_color = "purple"
      content          = "This dashboard was created by Terraform in **API Course** lab!"
      font_size        = "36"
      has_padding      = "true"
      show_tick        = "false"
      text_align       = "center"
      tick_edge        = "left"
      tick_pos         = "50%"
      vertical_align   = "center"
    }

    widget_layout {
      height          = "3"
      width           = "3"
      x               = "0"
      y               = "2"
    }
  }

  widget {
    timeseries_definition {
      legend_columns = ["avg", "max", "min", "sum", "value"]
      legend_layout  = "auto"

      request {
        display_type   = "line"
        on_right_yaxis = "false"

        query {
          metric_query {
            data_source = "metrics"
            name        = "query1"
            query       = "avg:docker.cpu.system{env:api-course} by {docker_image}.fill(0)"
          }
        }

        style {
          palette = "cool"
        }
      }

      show_legend = "false"
      title       = "System CPU by image"
      title_align = "left"
      title_size  = "16"

      yaxis {
        include_zero = "true"
        max          = "auto"
        min          = "auto"
        scale        = "linear"
      }
    }

    widget_layout {
      height          = "3"
      width           = "4"
      x               = "3"
      y               = "2"
    }
  }

  widget {
    group_definition {
      layout_type = "ordered"
      show_title  = "true"
      title       = "Stately-app"

      widget {
        timeseries_definition {
          legend_columns = ["avg", "max", "min", "sum", "value"]
          legend_layout  = "auto"

          request {
            display_type = "line"

            formula {
              formula_expression = "p100"
            }

            formula {
              formula_expression = "p50"
            }

            formula {
              formula_expression = "p75"
            }

            formula {
              formula_expression = "p90"
            }

            formula {
              formula_expression = "p95"
            }

            formula {
              formula_expression = "p99"
            }

            formula {
              formula_expression = "p99_9"
            }

            on_right_yaxis = "false"

            query {
              metric_query {
                data_source = "metrics"
                name        = "p100"
                query       = "max:trace.falcon.request{env:api-course,service:stately-app}"
              }
            }

            query {
              metric_query {
                data_source = "metrics"
                name        = "p50"
                query       = "p50:trace.falcon.request{env:api-course,service:stately-app}"
              }
            }

            query {
              metric_query {
                data_source = "metrics"
                name        = "p75"
                query       = "p75:trace.falcon.request{env:api-course,service:stately-app}"
              }
            }

            query {
              metric_query {
                data_source = "metrics"
                name        = "p90"
                query       = "p90:trace.falcon.request{env:api-course,service:stately-app}"
              }
            }

            query {
              metric_query {
                data_source = "metrics"
                name        = "p95"
                query       = "p95:trace.falcon.request{env:api-course,service:stately-app}"
              }
            }

            query {
              metric_query {
                data_source = "metrics"
                name        = "p99"
                query       = "p99:trace.falcon.request{env:api-course,service:stately-app}"
              }
            }

            query {
              metric_query {
                data_source = "metrics"
                name        = "p99_9"
                query       = "p99.9:trace.falcon.request{env:api-course,service:stately-app}"
              }
            }
          }

          show_legend = "false"
          title       = "Latency"
          title_align = "left"
          title_size  = "16"

          yaxis {
            include_zero = "false"
            scale        = "linear"
          }
        }

        widget_layout {
          height          = "2"
          width           = "4"
          x               = "4"
          y               = "0"
        }
      }

      widget {
        timeseries_definition {
          legend_columns = ["avg", "max", "min", "sum", "value"]
          legend_layout  = "auto"

          request {
            display_type = "line"

            formula {
              formula_expression = "top(query1, 5, 'mean', 'desc')"
            }

            on_right_yaxis = "false"

            query {
              metric_query {
                data_source = "metrics"
                name        = "query1"
                query       = "p95:trace.falcon.request{env:api-course,service:stately-app} by {resource_name}"
              }
            }
          }

          show_legend = "false"
          title       = "Resources breakdown p95 latency (top 5)"
          title_align = "left"
          title_size  = "16"
        }

        widget_layout {
          height          = "2"
          width           = "4"
          x               = "4"
          y               = "2"
        }
      }

      widget {
        timeseries_definition {
          legend_columns = ["avg", "max", "min", "sum", "value"]
          legend_layout  = "auto"

          request {
            display_type = "bars"

            formula {
              formula_expression = "top(query1, 5, 'mean', 'desc')"
            }

            on_right_yaxis = "false"

            query {
              metric_query {
                data_source = "metrics"
                name        = "query1"
                query       = "sum:trace.falcon.request.hits{env:api-course,service:stately-app} by {resource_name}.as_count()"
              }
            }
          }

          show_legend = "false"
          title       = "Resources requests (top 5)"
          title_align = "left"
          title_size  = "16"
        }

        widget_layout {
          height          = "2"
          width           = "4"
          x               = "0"
          y               = "2"
        }
      }

      widget {
        timeseries_definition {
          legend_columns = ["avg", "max", "min", "sum", "value"]
          legend_layout  = "auto"

          request {
            display_type = "area"

            formula {
              formula_expression = "ewma_10(query1 * 100 / query2)"
            }

            on_right_yaxis = "false"

            query {
              metric_query {
                data_source = "metrics"
                name        = "query1"
                query       = "sum:trace.falcon.request.exec_time.by_service{env:api-course,service:stately-app} by {sublayer_service,sublayer_inferred}.rollup(sum).fill(zero)"
              }
            }

            query {
              metric_query {
                data_source = "metrics"
                name        = "query2"
                query       = "sum:trace.falcon.request.exec_time.by_service{env:api-course,service:stately-app}.rollup(sum).fill(zero)"
              }
            }
          }

          show_legend = "false"
          title       = "Percent of time spent in downstream services"
          title_align = "left"
          title_size  = "16"

          yaxis {
            include_zero = "false"
            max          = "100"
          }
        }

        widget_layout {
          height          = "2"
          width           = "4"
          x               = "8"
          y               = "2"
        }
      }

      widget {
        timeseries_definition {
          legend_columns = ["avg", "max", "min", "sum", "value"]
          legend_layout  = "auto"

          request {
            display_type = "bars"

            formula {
              formula_expression = "query1"
            }

            on_right_yaxis = "false"

            query {
              metric_query {
                data_source = "metrics"
                name        = "query1"
                query       = "sum:trace.falcon.request.errors{env:api-course,service:stately-app}.as_count()"
              }
            }

            style {
              palette = "warm"
            }
          }

          show_legend = "false"
          title       = "Errors"
          title_align = "left"
          title_size  = "16"
        }

        widget_layout {
          height          = "2"
          width           = "4"
          x               = "8"
          y               = "0"
        }
      }

      widget {
        timeseries_definition {
          legend_columns = ["avg", "max", "min", "sum", "value"]
          legend_layout  = "auto"

          request {
            display_type = "bars"

            formula {
              formula_expression = "query1"
            }

            on_right_yaxis = "false"

            query {
              metric_query {
                data_source = "metrics"
                name        = "query1"
                query       = "sum:trace.falcon.request.hits{env:api-course,service:stately-app}.as_count()"
              }
            }
          }

          show_legend = "false"
          title       = "Total requests"
          title_align = "left"
          title_size  = "16"
        }

        widget_layout {
          height          = "2"
          width           = "4"
          x               = "0"
          y               = "0"
        }
      }
    }

    widget_layout {
      height          = "5"
      width           = "12"
      x               = "0"
      y               = "5"
    }
  }
}
