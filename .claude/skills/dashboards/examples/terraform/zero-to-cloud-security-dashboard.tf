resource "datadog_dashboard_json" "dashboard_json" {
    dashboard = <<EOF
{
    "title": "TechStories Cloud Security Posture Report",
    "description": "A daily view into TechStories’ cloud security environment, showing where risks are rising, what’s improving, and which areas need immediate attention.",
    "widgets": [
        {
            "id": 6303703828728240,
            "definition": {
                "title": "Overview",
                "background_color": "vivid_purple",
                "show_title": true,
                "type": "group",
                "layout_type": "ordered",
                "widgets": [
                    {
                        "id": 3206174655968316,
                        "definition": {
                            "title": "Resource: High Risk",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "query_value",
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": [],
                                            "search": {
                                                "query": "evaluation:fail status:(critical OR high) $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework @workflow.mute.muted:false vulnerability_type:misconfiguration"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "palette": "white_on_red",
                                            "value": 400
                                        },
                                        {
                                            "comparator": "<",
                                            "value": 400,
                                            "palette": "white_on_green"
                                        }
                                    ]
                                }
                            ],
                            "autoscale": true,
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View misconfiguration",
                                    "link": "/security/compliance?query=evaluation%3Afail%20@workflow.mute.muted%3Afalse%20status%3A(critical%20OR%20high)%20{{@resource_type}}%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}%20{{$azure_subscription_id}}%20{{$gcp_project_id}}%20{{$framework}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp=1710188545416&live=true"
                                }
                            ],
                            "precision": 2,
                            "timeseries_background": {
                                "type": "area"
                            }
                        },
                        "layout": {
                            "x": 0,
                            "y": 0,
                            "width": 4,
                            "height": 1
                        }
                    },
                    {
                        "id": 6727175476399628,
                        "definition": {
                            "title": "Percent",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "query_value",
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "query1 / query2 * 100",
                                            "number_format": {
                                                "unit": {
                                                    "type": "canonical_unit",
                                                    "unit_name": "percent"
                                                }
                                            }
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": [],
                                            "search": {
                                                "query": "evaluation:fail status:(critical OR high) $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework @workflow.mute.muted:false vulnerability_type:misconfiguration"
                                            }
                                        },
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query2",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": [],
                                            "search": {
                                                "query": "evaluation:fail status:(critical OR high) $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework @workflow.mute.muted:false vulnerability_type:misconfiguration"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "palette": "white_on_red",
                                            "value": 400
                                        },
                                        {
                                            "comparator": "<",
                                            "value": 400,
                                            "palette": "white_on_green"
                                        }
                                    ]
                                }
                            ],
                            "autoscale": true,
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View misconfiguration",
                                    "link": "/security/compliance?query=evaluation%3Afail%20@workflow.mute.muted%3Afalse%20status%3A(critical%20OR%20high)%20{{@resource_type}}%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}%20{{$azure_subscription_id}}%20{{$gcp_project_id}}%20{{$framework}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp=1710188545416&live=true"
                                }
                            ],
                            "precision": 2,
                            "timeseries_background": {
                                "type": "area"
                            }
                        },
                        "layout": {
                            "x": 4,
                            "y": 0,
                            "width": 2,
                            "height": 1
                        }
                    },
                    {
                        "id": 6726631778291426,
                        "definition": {
                            "title": "Number of Critical/High misconfigurations",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "query_value",
                            "requests": [
                                {
                                    "response_format": "scalar",
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "count"
                                            },
                                            "group_by": [],
                                            "search": {
                                                "query": "evaluation:fail $gcp_project_id $azure_subscription_id $aws_account_id $service $env $team $framework @workflow.mute.muted:false status:(critical OR high) vulnerability_type:misconfiguration"
                                            }
                                        }
                                    ],
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "value": 0,
                                            "palette": "red_on_white"
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "default_zero(query1)"
                                        }
                                    ]
                                }
                            ],
                            "autoscale": true,
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View related misconfigurations",
                                    "link": "/security/compliance?query=@workflow.mute.muted%3Afalse%20status%3A(high%20OR%20critical)%20evaluation%3Afail%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}%20{{$azure_subscription_id}}%20{{$gcp_project_id}}%20{{$framework}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp={{timestamp_start}}{{timestamp_end}}"
                                }
                            ],
                            "precision": 2
                        },
                        "layout": {
                            "x": 7,
                            "y": 0,
                            "width": 5,
                            "height": 1
                        }
                    },
                    {
                        "id": 8936724298019212,
                        "definition": {
                            "title": "Resource: High Risk, Production",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "query_value",
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": [],
                                            "search": {
                                                "query": "evaluation:fail status:(critical OR high) $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework @workflow.mute.muted:false env:prod vulnerability_type:misconfiguration"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "palette": "white_on_red",
                                            "value": 12
                                        },
                                        {
                                            "comparator": "=",
                                            "value": 12,
                                            "palette": "white_on_yellow"
                                        },
                                        {
                                            "comparator": "<",
                                            "value": 12,
                                            "palette": "white_on_green"
                                        }
                                    ]
                                }
                            ],
                            "autoscale": true,
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View misconfiguration",
                                    "link": "/security/compliance?query=evaluation%3Afail%20@workflow.mute.muted%3Afalse%20status%3A(critical%20OR%20high)%20{{@resource_type}}%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}%20{{$azure_subscription_id}}%20{{$gcp_project_id}}%20{{$framework}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp=1710188545416&live=true"
                                }
                            ],
                            "precision": 2,
                            "timeseries_background": {
                                "type": "area"
                            }
                        },
                        "layout": {
                            "x": 0,
                            "y": 1,
                            "width": 4,
                            "height": 1
                        }
                    },
                    {
                        "id": 8553727648481664,
                        "definition": {
                            "title": "Resource: High Risk, Production",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "query_value",
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "query1 / query2 * 100",
                                            "number_format": {
                                                "unit": {
                                                    "type": "canonical_unit",
                                                    "unit_name": "percent"
                                                }
                                            }
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": [],
                                            "search": {
                                                "query": "evaluation:fail status:(critical OR high) $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework @workflow.mute.muted:false env:prod vulnerability_type:misconfiguration"
                                            }
                                        },
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query2",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": [],
                                            "search": {
                                                "query": "evaluation:fail status:(critical OR high) $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework @workflow.mute.muted:false vulnerability_type:misconfiguration"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "palette": "white_on_yellow",
                                            "value": 1
                                        }
                                    ]
                                }
                            ],
                            "autoscale": true,
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View misconfiguration",
                                    "link": "/security/compliance?query=evaluation%3Afail%20@workflow.mute.muted%3Afalse%20status%3A(critical%20OR%20high)%20{{@resource_type}}%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}%20{{$azure_subscription_id}}%20{{$gcp_project_id}}%20{{$framework}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp=1710188545416&live=true"
                                }
                            ],
                            "precision": 2,
                            "timeseries_background": {
                                "type": "area"
                            }
                        },
                        "layout": {
                            "x": 4,
                            "y": 1,
                            "width": 2,
                            "height": 1
                        }
                    },
                    {
                        "id": 6109302300168210,
                        "definition": {
                            "title": "Top Critical/High misconfigurations",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "toplist",
                            "requests": [
                                {
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "count"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "@workflow.rule.name",
                                                    "limit": 10,
                                                    "sort": {
                                                        "order": "desc",
                                                        "aggregation": "count"
                                                    }
                                                }
                                            ],
                                            "search": {
                                                "query": "evaluation:fail status:(critical OR high) $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework @workflow.mute.muted:false vulnerability_type:misconfiguration"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "palette": "white_on_red",
                                            "value": 0
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "sort": {
                                        "count": 10,
                                        "order_by": [
                                            {
                                                "type": "formula",
                                                "index": 0,
                                                "order": "desc"
                                            }
                                        ]
                                    }
                                }
                            ],
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View misconfiguration",
                                    "link": "/security/compliance?query=evaluation:fail status:(high OR critical) {{@workflow.rule.name}} {{$team}} {{$env}} {{$service}} {{$aws_account_id}} {{$azure_subscription_id}} {{$gcp_project_id}} {{$framework}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp={{timestamp_start}}%20{{timestamp_end}}"
                                }
                            ],
                            "style": {}
                        },
                        "layout": {
                            "x": 7,
                            "y": 1,
                            "width": 5,
                            "height": 3
                        }
                    },
                    {
                        "id": 3969739410431542,
                        "definition": {
                            "title": "Resource: High Risk, Production, Public Access",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "query_value",
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": [],
                                            "search": {
                                                "query": "evaluation:fail status:(critical OR high) $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework @workflow.mute.muted:false env:prod @dd_computed_attributes.is_publicly_accessible:true vulnerability_type:misconfiguration"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "palette": "white_on_red",
                                            "value": 0
                                        }
                                    ]
                                }
                            ],
                            "autoscale": true,
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View misconfiguration",
                                    "link": "/security/compliance?query=evaluation%3Afail%20@workflow.mute.muted%3Afalse%20status%3A(critical%20OR%20high)%20{{@resource_type}}%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}%20{{$azure_subscription_id}}%20{{$gcp_project_id}}%20{{$framework}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp=1710188545416&live=true"
                                }
                            ],
                            "precision": 2,
                            "timeseries_background": {
                                "type": "area"
                            }
                        },
                        "layout": {
                            "x": 0,
                            "y": 2,
                            "width": 4,
                            "height": 1
                        }
                    },
                    {
                        "id": 3746797559538170,
                        "definition": {
                            "title": "Resource: High Risk, Production, Public Access",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "query_value",
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "query1 / query2 * 100",
                                            "number_format": {
                                                "unit": {
                                                    "type": "canonical_unit",
                                                    "unit_name": "percent"
                                                }
                                            }
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": [],
                                            "search": {
                                                "query": "evaluation:fail status:(critical OR high) $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework @workflow.mute.muted:false env:prod @dd_computed_attributes.is_publicly_accessible:true vulnerability_type:misconfiguration"
                                            }
                                        },
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query2",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": [],
                                            "search": {
                                                "query": "evaluation:fail status:(critical OR high) $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework @workflow.mute.muted:false vulnerability_type:misconfiguration"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "palette": "white_on_red",
                                            "value": 0
                                        }
                                    ]
                                }
                            ],
                            "autoscale": true,
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View misconfiguration",
                                    "link": "/security/compliance?query=evaluation%3Afail%20@workflow.mute.muted%3Afalse%20status%3A(critical%20OR%20high)%20{{@resource_type}}%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}%20{{$azure_subscription_id}}%20{{$gcp_project_id}}%20{{$framework}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp=1710188545416&live=true"
                                }
                            ],
                            "precision": 2,
                            "timeseries_background": {
                                "type": "area"
                            }
                        },
                        "layout": {
                            "x": 4,
                            "y": 2,
                            "width": 2,
                            "height": 1
                        }
                    },
                    {
                        "id": 5150009647138536,
                        "definition": {
                            "title": "Resource: High Risk, Production, Public Access, Privilege Role",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "query_value",
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": [],
                                            "search": {
                                                "query": "evaluation:fail status:(critical OR high) $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework @workflow.mute.muted:false env:prod @dd_computed_attributes.is_publicly_accessible:true @dd_computed_attributes.privileged_access:true vulnerability_type:misconfiguration"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "palette": "white_on_red",
                                            "value": 0
                                        }
                                    ]
                                }
                            ],
                            "autoscale": true,
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View misconfiguration",
                                    "link": "/security/compliance?query=evaluation%3Afail%20@workflow.mute.muted%3Afalse%20status%3A(critical%20OR%20high)%20{{@resource_type}}%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}%20{{$azure_subscription_id}}%20{{$gcp_project_id}}%20{{$framework}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp=1710188545416&live=true"
                                }
                            ],
                            "precision": 2,
                            "timeseries_background": {
                                "type": "area"
                            }
                        },
                        "layout": {
                            "x": 0,
                            "y": 3,
                            "width": 4,
                            "height": 1
                        }
                    },
                    {
                        "id": 1769399468611262,
                        "definition": {
                            "title": "Resource: High Risk, Production, Public Access, Privilege Role",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "query_value",
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "query1 / query2 * 100",
                                            "number_format": {
                                                "unit": {
                                                    "type": "canonical_unit",
                                                    "unit_name": "percent"
                                                }
                                            }
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": [],
                                            "search": {
                                                "query": "evaluation:fail status:(critical OR high) $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework @workflow.mute.muted:false env:prod @dd_computed_attributes.is_publicly_accessible:true @dd_computed_attributes.privileged_access:true vulnerability_type:misconfiguration"
                                            }
                                        },
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query2",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": [],
                                            "search": {
                                                "query": "evaluation:fail status:(critical OR high) $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework @workflow.mute.muted:false vulnerability_type:misconfiguration"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "palette": "white_on_red",
                                            "value": 0
                                        }
                                    ]
                                }
                            ],
                            "autoscale": true,
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View misconfiguration",
                                    "link": "/security/compliance?query=evaluation%3Afail%20@workflow.mute.muted%3Afalse%20status%3A(critical%20OR%20high)%20{{@resource_type}}%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}%20{{$azure_subscription_id}}%20{{$gcp_project_id}}%20{{$framework}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp=1710188545416&live=true"
                                }
                            ],
                            "precision": 2,
                            "timeseries_background": {
                                "type": "area"
                            }
                        },
                        "layout": {
                            "x": 4,
                            "y": 3,
                            "width": 2,
                            "height": 1
                        }
                    }
                ]
            },
            "layout": {
                "x": 0,
                "y": 0,
                "width": 12,
                "height": 5
            }
        },
        {
            "definition": {
                "title": "Critical/High Misconfigurations",
                "background_color": "vivid_orange",
                "show_title": true,
                "type": "group",
                "layout_type": "ordered",
                "widgets": [
                    {
                        "id": 7670190301598750,
                        "definition": {
                            "type": "note",
                            "content": "## Get detailed insights into your CSM Misconfigurations\n\n[Documentation ↗](https://docs.datadoghq.com/security/misconfigurations/) | \n[View All Misconfigurations ↗](/security/compliance?query=evaluation%3Afail%20%40workflow.mute.muted%3Afalse%20&aggregation=rules&column=status&order=asc&sort=ruleSeverity%2CfailedResources-desc&live=true) ",
                            "background_color": "transparent",
                            "font_size": "16",
                            "text_align": "left",
                            "vertical_align": "top",
                            "show_tick": false,
                            "tick_pos": "50%",
                            "tick_edge": "left",
                            "has_padding": true
                        },
                        "layout": {
                            "x": 0,
                            "y": 0,
                            "width": 7,
                            "height": 2
                        }
                    },
                    {
                        "id": 6726631778291426,
                        "definition": {
                            "title": "Number of Critical/High misconfigurations",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "query_value",
                            "requests": [
                                {
                                    "response_format": "scalar",
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "count"
                                            },
                                            "group_by": [],
                                            "search": {
                                                "query": "evaluation:fail $gcp_project_id $azure_subscription_id $aws_account_id $service $env $team $framework vulnerability_type:misconfiguration @workflow.mute.muted:false status:(critical OR high)"
                                            }
                                        }
                                    ],
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "value": 0,
                                            "palette": "red_on_white"
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "default_zero(query1)"
                                        }
                                    ]
                                }
                            ],
                            "autoscale": true,
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View related misconfigurations",
                                    "link": "/security/compliance?query=@workflow.mute.muted%3Afalse%20status%3A(high%20OR%20critical)%20evaluation%3Afail%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}%20{{$azure_subscription_id}}%20{{$gcp_project_id}}%20{{$framework}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp={{timestamp_start}}{{timestamp_end}}"
                                }
                            ],
                            "precision": 2
                        },
                        "layout": {
                            "x": 7,
                            "y": 0,
                            "width": 5,
                            "height": 1
                        }
                    },
                    {
                        "id": 6109302300168210,
                        "definition": {
                            "title": "Top Critical/High misconfigurations",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "toplist",
                            "requests": [
                                {
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "count"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "@workflow.rule.name",
                                                    "limit": 10,
                                                    "sort": {
                                                        "order": "desc",
                                                        "aggregation": "count"
                                                    }
                                                }
                                            ],
                                            "search": {
                                                "query": "evaluation:fail status:(critical OR high) $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework vulnerability_type:misconfiguration @workflow.mute.muted:false"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "palette": "white_on_red",
                                            "value": 0
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "sort": {
                                        "count": 10,
                                        "order_by": [
                                            {
                                                "type": "formula",
                                                "index": 0,
                                                "order": "desc"
                                            }
                                        ]
                                    }
                                }
                            ],
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View misconfiguration",
                                    "link": "/security/compliance?query=evaluation:fail status:(high OR critical) {{@workflow.rule.name}} {{$team}} {{$env}} {{$service}} {{$aws_account_id}} {{$azure_subscription_id}} {{$gcp_project_id}} {{$framework}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp={{timestamp_start}}%20{{timestamp_end}}"
                                }
                            ],
                            "style": {}
                        },
                        "layout": {
                            "x": 7,
                            "y": 1,
                            "width": 5,
                            "height": 3
                        }
                    },
                    {
                        "id": 82379750940280,
                        "definition": {
                            "title": "Number of misconfigurations vs last month",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "change",
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View related misconfigurations",
                                    "link": "/security/compliance?query=@workflow.mute.muted%3Afalse%20evaluation%3Afail%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}%20{{$azure_subscription_id}}%20{{$gcp_project_id}}%20{{$framework}}%20{{tags}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp={{timestamp_start}}{{timestamp_end}}"
                                }
                            ],
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "month_before(query1)"
                                        },
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "count"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "status",
                                                    "limit": 10,
                                                    "sort": {
                                                        "order": "desc",
                                                        "aggregation": "count"
                                                    }
                                                }
                                            ],
                                            "search": {
                                                "query": "evaluation:fail $team $env $service $aws_account_id $gcp_project_id $azure_subscription_id $framework vulnerability_type:misconfiguration @workflow.mute.muted:false"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "change_type": "absolute",
                                    "show_present": true,
                                    "order_by": "present",
                                    "order_dir": "desc",
                                    "increase_good": false
                                }
                            ]
                        },
                        "layout": {
                            "x": 0,
                            "y": 2,
                            "width": 7,
                            "height": 2
                        }
                    }
                ]
            },
            "layout": {
                "x": 0,
                "y": 0,
                "width": 12,
                "height": 1
            }
        },
        {
            "id": 237806942128402,
            "definition": {
                "title": "Critical/High Identity Risks",
                "background_color": "vivid_orange",
                "show_title": true,
                "type": "group",
                "layout_type": "ordered",
                "widgets": [
                    {
                        "id": 747593541365750,
                        "definition": {
                            "type": "note",
                            "content": "## Get detailed insights into your CSM Identity Risks\n\n[Documentation ↗](https://docs.datadoghq.com/security/identity_risks/) | \n[View All Identity Risks ↗](/security/identities) ",
                            "background_color": "transparent",
                            "font_size": "16",
                            "text_align": "left",
                            "vertical_align": "top",
                            "show_tick": false,
                            "tick_pos": "50%",
                            "tick_edge": "left",
                            "has_padding": true
                        },
                        "layout": {
                            "x": 0,
                            "y": 0,
                            "width": 7,
                            "height": 2
                        }
                    },
                    {
                        "id": 2498717421456173,
                        "definition": {
                            "title": "Number of Critical/High identity risks",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "query_value",
                            "requests": [
                                {
                                    "response_format": "scalar",
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "count"
                                            },
                                            "group_by": [],
                                            "search": {
                                                "query": "evaluation:fail $aws_account_id $service $env $team @workflow.mute.muted:false status:(critical OR high) vulnerability_type:identity_risk"
                                            }
                                        }
                                    ],
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "value": 0,
                                            "palette": "red_on_white"
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "default_zero(query1)"
                                        }
                                    ]
                                }
                            ],
                            "autoscale": true,
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View related identity risks",
                                    "link": "https://app.datadoghq.com/security/identities?aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp={{timestamp_start}} {{timestamp_end}}&query=evaluation%3Afail%20status%3A(critical%20OR%20high)%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}"
                                }
                            ],
                            "precision": 2
                        },
                        "layout": {
                            "x": 7,
                            "y": 0,
                            "width": 5,
                            "height": 1
                        }
                    },
                    {
                        "id": 2492789001833441,
                        "definition": {
                            "title": "Top Critical/High identity risks",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "toplist",
                            "requests": [
                                {
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "count"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "@workflow.rule.name",
                                                    "limit": 10,
                                                    "sort": {
                                                        "order": "desc",
                                                        "aggregation": "count"
                                                    }
                                                }
                                            ],
                                            "search": {
                                                "query": "evaluation:fail status:(critical OR high) $team $env $service $aws_account_id @workflow.mute.muted:false vulnerability_type:identity_risk"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "palette": "white_on_red",
                                            "value": 0
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "sort": {
                                        "count": 10,
                                        "order_by": [
                                            {
                                                "type": "formula",
                                                "index": 0,
                                                "order": "desc"
                                            }
                                        ]
                                    }
                                }
                            ],
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View identity risk",
                                    "link": "https://app.datadoghq.com/security/identities?aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp={{timestamp_start}} {{timestamp_end}}&query=evaluation%3Afail%20status%3A(critical%20OR%20high)%20{{@workflow.rule.name}}%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}%20"
                                }
                            ],
                            "style": {}
                        },
                        "layout": {
                            "x": 7,
                            "y": 1,
                            "width": 5,
                            "height": 3
                        }
                    },
                    {
                        "id": 607371519865339,
                        "definition": {
                            "title": "Resources with most Critical/High identity risks vs last month",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "change",
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View related identity risks",
                                    "link": "https://app.datadoghq.com/security/identities?query=evaluation%3Afail%20status%3A(critical%20OR%20high)%20{{@resource_type}}%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp=1710441404812&live=true"
                                }
                            ],
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "month_before(query1)"
                                        },
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "count"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "@resource_type",
                                                    "limit": 10,
                                                    "sort": {
                                                        "order": "desc",
                                                        "aggregation": "count"
                                                    }
                                                }
                                            ],
                                            "search": {
                                                "query": "evaluation:fail $team $env $service $aws_account_id @workflow.mute.muted:false status:(critical OR high) vulnerability_type:identity_risk"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "change_type": "absolute",
                                    "show_present": true,
                                    "order_by": "present",
                                    "order_dir": "desc",
                                    "increase_good": false
                                }
                            ]
                        },
                        "layout": {
                            "x": 0,
                            "y": 2,
                            "width": 7,
                            "height": 3
                        }
                    }
                ]
            },
            "layout": {
                "x": 0,
                "y": 1,
                "width": 12,
                "height": 1
            }
        },
        {
            "id": 5114672048388460,
            "definition": {
                "title": "Vulnerabilities Overview",
                "background_color": "vivid_orange",
                "show_title": true,
                "type": "group",
                "layout_type": "ordered",
                "widgets": [
                    {
                        "id": 3772645728383221,
                        "definition": {
                            "type": "note",
                            "content": "## Get detailed insights into your CSM Vulnerabilities\n\n[Documentation ↗](https://docs.datadoghq.com/security/vulnerabilities/) | \n[View All Vulnerabilities ↗](/security/csm/vm)",
                            "background_color": "transparent",
                            "font_size": "14",
                            "text_align": "left",
                            "vertical_align": "top",
                            "show_tick": false,
                            "tick_pos": "50%",
                            "tick_edge": "left",
                            "has_padding": true
                        },
                        "layout": {
                            "x": 0,
                            "y": 0,
                            "width": 6,
                            "height": 2
                        }
                    },
                    {
                        "id": 132599572382434,
                        "definition": {
                            "title": "Active critical or high vulns",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "query_value",
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "metrics",
                                            "name": "query1",
                                            "query": "sum:datadog.csm.vulnerabilities{(status:open OR status:in_progress) AND (severity:critical OR severity:high) AND $env AND $team}",
                                            "aggregator": "last"
                                        }
                                    ],
                                    "response_format": "scalar"
                                }
                            ],
                            "autoscale": true,
                            "precision": 2,
                            "timeseries_background": {
                                "type": "area"
                            }
                        },
                        "layout": {
                            "x": 6,
                            "y": 0,
                            "width": 6,
                            "height": 2
                        }
                    },
                    {
                        "id": 1012342532745416,
                        "definition": {
                            "title": "Active container image vulns distribution",
                            "title_size": "16",
                            "title_align": "left",
                            "requests": [
                                {
                                    "queries": [
                                        {
                                            "data_source": "metrics",
                                            "name": "query1",
                                            "query": "sum:datadog.csm.vulnerabilities{(status:open OR status:in_progress) AND resource_type:container_image AND $env AND $team} by {severity}",
                                            "aggregator": "last"
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "style": {
                                        "palette": "semantic"
                                    },
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "sort": {
                                        "count": 500,
                                        "order_by": [
                                            {
                                                "type": "formula",
                                                "index": 0,
                                                "order": "desc"
                                            }
                                        ]
                                    }
                                }
                            ],
                            "type": "sunburst",
                            "legend": {
                                "type": "automatic"
                            }
                        },
                        "layout": {
                            "x": 0,
                            "y": 2,
                            "width": 3,
                            "height": 3
                        }
                    },
                    {
                        "id": 6566139180613109,
                        "definition": {
                            "title": "Active host vulns distribution",
                            "title_size": "16",
                            "title_align": "left",
                            "requests": [
                                {
                                    "queries": [
                                        {
                                            "data_source": "metrics",
                                            "name": "query1",
                                            "query": "sum:datadog.csm.vulnerabilities{(status:open OR status:in_progress) AND resource_type:host AND $env AND $team} by {severity}",
                                            "aggregator": "last"
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "style": {
                                        "palette": "semantic"
                                    },
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "sort": {
                                        "count": 500,
                                        "order_by": [
                                            {
                                                "type": "formula",
                                                "index": 0,
                                                "order": "desc"
                                            }
                                        ]
                                    }
                                }
                            ],
                            "type": "sunburst",
                            "legend": {
                                "type": "automatic"
                            }
                        },
                        "layout": {
                            "x": 3,
                            "y": 2,
                            "width": 3,
                            "height": 3
                        }
                    },
                    {
                        "id": 6286079862540450,
                        "definition": {
                            "title": "Active vulns distribution",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "query_table",
                            "requests": [
                                {
                                    "queries": [
                                        {
                                            "data_source": "metrics",
                                            "name": "query1",
                                            "query": "sum:datadog.csm.vulnerabilities{(status:open OR status:in_progress) AND $env AND $team} by {severity}",
                                            "aggregator": "last"
                                        },
                                        {
                                            "data_source": "metrics",
                                            "name": "query2",
                                            "query": "sum:datadog.csm.vulnerabilities{(status:open OR status:in_progress) AND resource_type:container_image AND $env AND $team} by {severity}",
                                            "aggregator": "last"
                                        },
                                        {
                                            "data_source": "metrics",
                                            "name": "query3",
                                            "query": "sum:datadog.csm.vulnerabilities{(status:open OR status:in_progress) AND resource_type:host AND $env AND $team} by {severity}",
                                            "aggregator": "last"
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "sort": {
                                        "count": 10,
                                        "order_by": [
                                            {
                                                "type": "formula",
                                                "index": 0,
                                                "order": "desc"
                                            }
                                        ]
                                    },
                                    "formulas": [
                                        {
                                            "cell_display_mode": "number",
                                            "alias": "Total vulns",
                                            "formula": "query1"
                                        },
                                        {
                                            "cell_display_mode": "number",
                                            "alias": "Container image vulns",
                                            "formula": "query2"
                                        },
                                        {
                                            "cell_display_mode": "number",
                                            "alias": "Host vulns",
                                            "formula": "query3"
                                        }
                                    ]
                                }
                            ],
                            "has_search_bar": "never"
                        },
                        "layout": {
                            "x": 6,
                            "y": 2,
                            "width": 6,
                            "height": 3
                        }
                    }
                ]
            },
            "layout": {
                "x": 0,
                "y": 2,
                "width": 12,
                "height": 1
            }
        },
        {
            "id": 3527947713782588,
            "definition": {
                "title": "Misconfiguration Trends",
                "background_color": "vivid_blue",
                "show_title": true,
                "type": "group",
                "layout_type": "ordered",
                "widgets": [
                    {
                        "id": 2633943084853502,
                        "definition": {
                            "type": "note",
                            "content": "Start with rule and resource trends to determine why security posture may have changed over time. Click on a rule or resource to [view related misconfigurations](/security/compliance?query=evaluation%3Afail%20%40workflow.mute.muted%3Afalse%20&aggregation=rules&column=status&order=asc&sort=ruleSeverity%2CfailedResources-desc&live=true).",
                            "background_color": "yellow",
                            "font_size": "14",
                            "text_align": "left",
                            "vertical_align": "center",
                            "show_tick": true,
                            "tick_pos": "50%",
                            "tick_edge": "bottom",
                            "has_padding": true
                        },
                        "layout": {
                            "x": 0,
                            "y": 0,
                            "width": 12,
                            "height": 1
                        }
                    },
                    {
                        "id": 4760381151198906,
                        "definition": {
                            "title": "Rules with most Critical/High misconfigurations vs last month",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "change",
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View related misconfigurations",
                                    "link": "/security/compliance?query=status%3A(critical%20OR%20high)%20evaluation%3Afail%20@workflow.mute.muted%3Afalse%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}%20{{$azure_subscription_id}}%20{{$gcp_project_id}}%20{{$framework}}%20{{@workflow.rule.name}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp={{timestamp_start}} {{timestamp_end}}"
                                }
                            ],
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "month_before(query1)"
                                        },
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "count"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "@workflow.rule.name",
                                                    "limit": 10,
                                                    "sort": {
                                                        "order": "desc",
                                                        "aggregation": "count"
                                                    }
                                                }
                                            ],
                                            "search": {
                                                "query": "evaluation:fail $team $env $service $aws_account_id $gcp_project_id $azure_subscription_id $framework vulnerability_type:misconfiguration @workflow.mute.muted:false status:(critical OR high)"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "change_type": "absolute",
                                    "show_present": true,
                                    "order_by": "present",
                                    "order_dir": "desc",
                                    "increase_good": false
                                }
                            ]
                        },
                        "layout": {
                            "x": 0,
                            "y": 1,
                            "width": 6,
                            "height": 3
                        }
                    },
                    {
                        "id": 1866152433321582,
                        "definition": {
                            "title": "Resources with most Critical/High misconfigurations vs last month",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "change",
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View related misconfigurations",
                                    "link": "/security/compliance?query=status%3A(critical%20OR%20high)%20%20evaluation%3Afail%20@workflow.mute.muted%3Afalse%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}%20{{$azure_subscription_id}}%20{{$gcp_project_id}}%20{{$framework}}%20{{@resource_type}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp={{timestamp_start}} {{timestamp_end}}"
                                }
                            ],
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "month_before(query1)"
                                        },
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "count"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "@resource_type",
                                                    "limit": 10,
                                                    "sort": {
                                                        "order": "desc",
                                                        "aggregation": "count"
                                                    }
                                                }
                                            ],
                                            "search": {
                                                "query": "evaluation:fail $team $env $service $aws_account_id $gcp_project_id $azure_subscription_id $framework vulnerability_type:misconfiguration @workflow.mute.muted:false status:(critical OR high)"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "change_type": "absolute",
                                    "show_present": true,
                                    "order_by": "present",
                                    "order_dir": "desc",
                                    "increase_good": false
                                }
                            ]
                        },
                        "layout": {
                            "x": 6,
                            "y": 1,
                            "width": 6,
                            "height": 3
                        }
                    },
                    {
                        "id": 3058995383288986,
                        "definition": {
                            "type": "note",
                            "content": "Tags help you understand who is responsible for a specific resource (`team`), in what environment the resource is running (`env`), and in what service it is running (`service`). [View documentation](https://docs.datadoghq.com/getting_started/tagging/) to learn tagging best practices.",
                            "background_color": "yellow",
                            "font_size": "14",
                            "text_align": "left",
                            "vertical_align": "center",
                            "show_tick": true,
                            "tick_pos": "50%",
                            "tick_edge": "bottom",
                            "has_padding": true
                        },
                        "layout": {
                            "x": 0,
                            "y": 4,
                            "width": 12,
                            "height": 1
                        }
                    },
                    {
                        "id": 6347229790127958,
                        "definition": {
                            "title": "Teams with most Critical/High misconfigurations vs last month",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "change",
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View related misconfigurations",
                                    "link": "/security/compliance?query=status%3A(critical%20OR%20high)%20%20evaluation%3Afail%20@workflow.mute.muted%3Afalse%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}%20{{$azure_subscription_id}}%20{{$gcp_project_id}}%20{{$framework}}%20{{team}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp={{timestamp_start}} {{timestamp_end}}"
                                }
                            ],
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "month_before(query1)"
                                        },
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "count"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "team",
                                                    "limit": 10,
                                                    "sort": {
                                                        "order": "desc",
                                                        "aggregation": "count"
                                                    }
                                                }
                                            ],
                                            "search": {
                                                "query": "evaluation:fail $team $env $service $aws_account_id $gcp_project_id $azure_subscription_id $framework vulnerability_type:misconfiguration @workflow.mute.muted:false status:(critical OR high)"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "change_type": "absolute",
                                    "show_present": true,
                                    "order_by": "present",
                                    "order_dir": "desc",
                                    "increase_good": false
                                }
                            ]
                        },
                        "layout": {
                            "x": 0,
                            "y": 5,
                            "width": 4,
                            "height": 3
                        }
                    },
                    {
                        "id": 4062320291774298,
                        "definition": {
                            "title": "Environments with the most Critical/High misconfigurations vs last month",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "change",
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View related misconfigurations",
                                    "link": "/security/compliance?query=status%3A(critical%20OR%20high)%20%20evaluation%3Afail%20@workflow.mute.muted%3Afalse%20{{env}}%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}%20{{$azure_subscription_id}}%20{{$gcp_project_id}}%20{{$framework}}%20&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp={{timestamp_start}} {{timestamp_end}}&live="
                                }
                            ],
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "month_before(query1)"
                                        },
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "count"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "env",
                                                    "limit": 10,
                                                    "sort": {
                                                        "order": "desc",
                                                        "aggregation": "count"
                                                    }
                                                }
                                            ],
                                            "search": {
                                                "query": "evaluation:fail $env $service $team $aws_account_id $gcp_project_id $azure_subscription_id $framework vulnerability_type:misconfiguration @workflow.mute.muted:false status:(critical OR high)"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "increase_good": false,
                                    "order_by": "present",
                                    "order_dir": "desc",
                                    "show_present": true
                                }
                            ]
                        },
                        "layout": {
                            "x": 4,
                            "y": 5,
                            "width": 4,
                            "height": 3
                        }
                    },
                    {
                        "id": 662418149288514,
                        "definition": {
                            "title": "Services with most Critical/High misconfigurations vs last month",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "change",
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View related misconfigurations",
                                    "link": "/security/compliance?query=status%3A(critical%20OR%20high)%20%20evaluation%3Afail%20@workflow.mute.muted%3Afalse%20{{service}}%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}%20{{$azure_subscription_id}}%20{{$gcp_project_id}}%20{{$framework}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp={{timestamp_start}} {{timestamp_end}}"
                                }
                            ],
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "month_before(query1)"
                                        },
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "count"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "service",
                                                    "limit": 10,
                                                    "sort": {
                                                        "order": "desc",
                                                        "aggregation": "count"
                                                    }
                                                }
                                            ],
                                            "search": {
                                                "query": "evaluation:fail $team $env $service $aws_account_id $gcp_project_id $azure_subscription_id $framework vulnerability_type:misconfiguration @workflow.mute.muted:false status:(critical OR high)"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "change_type": "absolute",
                                    "show_present": true,
                                    "order_by": "present",
                                    "order_dir": "desc",
                                    "increase_good": false
                                }
                            ]
                        },
                        "layout": {
                            "x": 8,
                            "y": 5,
                            "width": 4,
                            "height": 3
                        }
                    },
                    {
                        "id": 1445682280490196,
                        "definition": {
                            "type": "note",
                            "content": "A misconfiguration is muted when it has a pending fix, is an accepted risk, or is a false positive. [View documentation](https://docs.datadoghq.com/security/cloud_security_management/review_remediate/mute_issues/) to learn more about muting misconfigurations.",
                            "background_color": "yellow",
                            "font_size": "14",
                            "text_align": "left",
                            "vertical_align": "center",
                            "show_tick": true,
                            "tick_pos": "50%",
                            "tick_edge": "bottom",
                            "has_padding": true
                        },
                        "layout": {
                            "x": 0,
                            "y": 8,
                            "width": 12,
                            "height": 1
                        }
                    },
                    {
                        "id": 734064938946622,
                        "definition": {
                            "title": "Rules with most mutes vs last month",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "change",
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View related misconfigurations",
                                    "link": "/security/compliance?query=@workflow.mute.muted%3Atrue%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}%20{{$azure_subscription_id}}%20{{$gcp_project_id}}%20{{$framework}}%20{{@workflow.rule.name}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp={{timestamp_start}} {{timestamp_end}}"
                                }
                            ],
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "month_before(query1)"
                                        },
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "count"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "@workflow.rule.name",
                                                    "limit": 10,
                                                    "sort": {
                                                        "order": "desc",
                                                        "aggregation": "count"
                                                    }
                                                }
                                            ],
                                            "search": {
                                                "query": "$team $env $service $aws_account_id $gcp_project_id $azure_subscription_id $framework vulnerability_type:misconfiguration @workflow.mute.muted:true"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "change_type": "absolute",
                                    "show_present": true,
                                    "order_by": "present",
                                    "order_dir": "desc",
                                    "increase_good": false
                                }
                            ]
                        },
                        "layout": {
                            "x": 0,
                            "y": 9,
                            "width": 6,
                            "height": 3
                        }
                    },
                    {
                        "id": 4481154289740240,
                        "definition": {
                            "title": "Mute reasons vs last month",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "change",
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View related misconfigurations",
                                    "link": "/security/compliance?query=@workflow.mute.muted%3Atrue%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}%20{{$azure_subscription_id}}%20{{$gcp_project_id}}%20{{$framework}}%20{{@workflow.mute.reason}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp={{timestamp_start}} {{timestamp_end}}"
                                }
                            ],
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "month_before(query1)"
                                        },
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "count"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "@workflow.mute.reason",
                                                    "limit": 10,
                                                    "sort": {
                                                        "order": "desc",
                                                        "aggregation": "count"
                                                    }
                                                }
                                            ],
                                            "search": {
                                                "query": "$team $env $service $aws_account_id $gcp_project_id $azure_subscription_id $framework vulnerability_type:misconfiguration @workflow.mute.muted:true"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "change_type": "absolute",
                                    "show_present": true,
                                    "order_by": "present",
                                    "order_dir": "desc",
                                    "increase_good": false
                                }
                            ]
                        },
                        "layout": {
                            "x": 6,
                            "y": 9,
                            "width": 6,
                            "height": 3
                        }
                    }
                ]
            },
            "layout": {
                "x": 0,
                "y": 3,
                "width": 12,
                "height": 1
            }
        },
        {
            "id": 7275127798353910,
            "definition": {
                "title": "Identity Risk Trends",
                "background_color": "vivid_blue",
                "show_title": true,
                "type": "group",
                "layout_type": "ordered",
                "widgets": [
                    {
                        "id": 5823374751877554,
                        "definition": {
                            "type": "note",
                            "content": "To determine why security posture may have changed over time, start with rule and resource trends. Click on a rule or resource to [view related identity risks](/security/identities).",
                            "background_color": "yellow",
                            "font_size": "14",
                            "text_align": "left",
                            "vertical_align": "center",
                            "show_tick": true,
                            "tick_pos": "50%",
                            "tick_edge": "bottom",
                            "has_padding": true
                        },
                        "layout": {
                            "x": 0,
                            "y": 0,
                            "width": 12,
                            "height": 1
                        }
                    },
                    {
                        "id": 4861001981483100,
                        "definition": {
                            "title": "Rules with most Critical/High identity risks vs last month",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "change",
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View related identity risks",
                                    "link": "https://app.datadoghq.com/security/identities?query=evaluation:fail status:(critical OR high) {{@workflow.rule.name}} {{$team}} {{$env}} {{$service}} {{$aws_account_id}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc"
                                }
                            ],
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "month_before(query1)"
                                        },
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "count"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "@workflow.rule.name",
                                                    "limit": 10,
                                                    "sort": {
                                                        "order": "desc",
                                                        "aggregation": "count"
                                                    }
                                                }
                                            ],
                                            "search": {
                                                "query": "evaluation:fail $team $env $service $aws_account_id @workflow.mute.muted:false status:(critical OR high) vulnerability_type:identity_risk"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "change_type": "absolute",
                                    "show_present": true,
                                    "order_by": "present",
                                    "order_dir": "desc",
                                    "increase_good": false
                                }
                            ]
                        },
                        "layout": {
                            "x": 0,
                            "y": 1,
                            "width": 6,
                            "height": 3
                        }
                    },
                    {
                        "id": 4099312590662286,
                        "definition": {
                            "title": "Resources with most Critical/High identity risks vs last month",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "change",
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View related identity risks",
                                    "link": "https://app.datadoghq.com/security/identities?query=evaluation%3Afail%20status%3A(critical%20OR%20high)%20{{@resource_type}}%20{{$team}}%20{{$env}}%20{{$service}}%20{{$aws_account_id}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc&timestamp=1710441404812&live=true"
                                }
                            ],
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "month_before(query1)"
                                        },
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "count"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "@resource_type",
                                                    "limit": 10,
                                                    "sort": {
                                                        "order": "desc",
                                                        "aggregation": "count"
                                                    }
                                                }
                                            ],
                                            "search": {
                                                "query": "evaluation:fail $team $env $service $aws_account_id @workflow.mute.muted:false status:(critical OR high) vulnerability_type:identity_risk"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "change_type": "absolute",
                                    "show_present": true,
                                    "order_by": "present",
                                    "order_dir": "desc",
                                    "increase_good": false
                                }
                            ]
                        },
                        "layout": {
                            "x": 6,
                            "y": 1,
                            "width": 6,
                            "height": 3
                        }
                    },
                    {
                        "id": 1041982567596670,
                        "definition": {
                            "type": "note",
                            "content": "Tags help you understand who is responsible for a specific resource (`team`), in what environment the resource is running (`env`), and in what service it is running (`service`). [View documentation](https://docs.datadoghq.com/getting_started/tagging/) to learn tagging best practices.",
                            "background_color": "yellow",
                            "font_size": "14",
                            "text_align": "left",
                            "vertical_align": "center",
                            "show_tick": true,
                            "tick_pos": "50%",
                            "tick_edge": "bottom",
                            "has_padding": true
                        },
                        "layout": {
                            "x": 0,
                            "y": 4,
                            "width": 12,
                            "height": 1
                        }
                    },
                    {
                        "id": 7319072799104034,
                        "definition": {
                            "title": "Teams with most Critical/High identity risks vs last month",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "change",
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View related identity risks",
                                    "link": "https://app.datadoghq.com/security/identities?query=evaluation%3Afail%20status%3A(critical%20OR%20high)%20%20{{team}}%20{{$team}}%20{{$env}}%20{{$service}}{{$aws_account_id}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc"
                                }
                            ],
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "month_before(query1)"
                                        },
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "count"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "team",
                                                    "limit": 10,
                                                    "sort": {
                                                        "order": "desc",
                                                        "aggregation": "count"
                                                    }
                                                }
                                            ],
                                            "search": {
                                                "query": "evaluation:fail $team $env $service $aws_account_id @workflow.mute.muted:false status:(critical OR high) vulnerability_type:identity_risk"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "change_type": "absolute",
                                    "show_present": true,
                                    "order_by": "present",
                                    "order_dir": "desc",
                                    "increase_good": false
                                }
                            ]
                        },
                        "layout": {
                            "x": 0,
                            "y": 5,
                            "width": 4,
                            "height": 3
                        }
                    },
                    {
                        "id": 8271529500721280,
                        "definition": {
                            "title": "Environments with the most Critical/High identity risks vs last month",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "change",
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View related identity risks",
                                    "link": "https://app.datadoghq.com/security/identities?query=evaluation%3Afail%20status%3A(critical%20OR%20high)%20{{env}}%20{{$team}}%20{{$env}}%20{{$service}}{{$aws_account_id}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc"
                                }
                            ],
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "month_before(query1)"
                                        },
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "count"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "env",
                                                    "limit": 10,
                                                    "sort": {
                                                        "order": "desc",
                                                        "aggregation": "count"
                                                    }
                                                }
                                            ],
                                            "search": {
                                                "query": "evaluation:fail $env $service $team $aws_account_id @workflow.mute.muted:false status:(critical OR high) vulnerability_type:identity_risk"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "increase_good": false,
                                    "order_by": "present",
                                    "order_dir": "desc",
                                    "show_present": true
                                }
                            ]
                        },
                        "layout": {
                            "x": 4,
                            "y": 5,
                            "width": 4,
                            "height": 3
                        }
                    },
                    {
                        "id": 3402599104105998,
                        "definition": {
                            "title": "Services with most Critical/High identity risks vs last month",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "change",
                            "custom_links": [
                                {
                                    "override_label": "containers",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "hosts",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "logs",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "traces",
                                    "is_hidden": true
                                },
                                {
                                    "override_label": "profiles",
                                    "is_hidden": true
                                },
                                {
                                    "label": "View related identity risks",
                                    "link": "https://app.datadoghq.com/security/identities?query=evaluation:fail status:(critical OR high) {{service}}  {{$team}} {{$env}} {{$service}} {{$aws_account_id}}&aggregation=rules&column=status&order=asc&sort=ruleSeverity,failedResources-desc"
                                }
                            ],
                            "requests": [
                                {
                                    "formulas": [
                                        {
                                            "formula": "month_before(query1)"
                                        },
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "count"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "service",
                                                    "limit": 10,
                                                    "sort": {
                                                        "order": "desc",
                                                        "aggregation": "count"
                                                    }
                                                }
                                            ],
                                            "search": {
                                                "query": "evaluation:fail $team $env $service $aws_account_id @workflow.mute.muted:false status:(critical OR high) vulnerability_type:identity_risk"
                                            }
                                        }
                                    ],
                                    "response_format": "scalar",
                                    "change_type": "absolute",
                                    "show_present": true,
                                    "order_by": "present",
                                    "order_dir": "desc",
                                    "increase_good": false
                                }
                            ]
                        },
                        "layout": {
                            "x": 8,
                            "y": 5,
                            "width": 4,
                            "height": 3
                        }
                    }
                ]
            },
            "layout": {
                "x": 0,
                "y": 4,
                "width": 12,
                "height": 1
            }
        },
        {
            "id": 8681535978511432,
            "definition": {
                "title": "Tagging",
                "background_color": "vivid_purple",
                "show_title": true,
                "type": "group",
                "layout_type": "ordered",
                "widgets": [
                    {
                        "id": 5431627987322772,
                        "definition": {
                            "type": "note",
                            "content": "Tags help you understand who is responsible for a specific resource (`team`), in what environment the resource is running (`env`), and in what service it is running (`service`). [View documentation](https://docs.datadoghq.com/getting_started/tagging/) to learn tagging best practices.",
                            "background_color": "yellow",
                            "font_size": "14",
                            "text_align": "left",
                            "vertical_align": "center",
                            "show_tick": true,
                            "tick_pos": "50%",
                            "tick_edge": "bottom",
                            "has_padding": true
                        },
                        "layout": {
                            "x": 0,
                            "y": 0,
                            "width": 12,
                            "height": 1
                        }
                    },
                    {
                        "id": 353908548014706,
                        "definition": {
                            "title": "Percentage of tagged resources - team",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "query_value",
                            "requests": [
                                {
                                    "response_format": "scalar",
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query2",
                                            "search": {
                                                "query": "$team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework vulnerability_type:misconfiguration"
                                            },
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": []
                                        },
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "search": {
                                                "query": "team:* $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework vulnerability_type:misconfiguration"
                                            },
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": []
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "query1 / query2 * 100"
                                        }
                                    ],
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "value": 0,
                                            "palette": "custom_text",
                                            "custom_fg_color": "#0014ad"
                                        }
                                    ]
                                }
                            ],
                            "autoscale": true,
                            "custom_unit": "%",
                            "precision": 1
                        },
                        "layout": {
                            "x": 0,
                            "y": 1,
                            "width": 4,
                            "height": 1
                        }
                    },
                    {
                        "id": 1495333574611430,
                        "definition": {
                            "title": "Tagged resources - team",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "query_value",
                            "requests": [
                                {
                                    "response_format": "scalar",
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "search": {
                                                "query": "team:* $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework vulnerability_type:misconfiguration"
                                            },
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": []
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "value": 0,
                                            "palette": "green_on_white"
                                        }
                                    ]
                                }
                            ],
                            "autoscale": true,
                            "precision": 2
                        },
                        "layout": {
                            "x": 4,
                            "y": 1,
                            "width": 4,
                            "height": 1
                        }
                    },
                    {
                        "id": 7745977797960324,
                        "definition": {
                            "title": "Untagged resources - team",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "query_value",
                            "requests": [
                                {
                                    "response_format": "scalar",
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "search": {
                                                "query": "-team:* $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework vulnerability_type:misconfiguration"
                                            },
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": []
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "value": 0,
                                            "palette": "red_on_white"
                                        }
                                    ]
                                }
                            ],
                            "autoscale": true,
                            "precision": 2
                        },
                        "layout": {
                            "x": 8,
                            "y": 1,
                            "width": 4,
                            "height": 1
                        }
                    },
                    {
                        "id": 3041054461481678,
                        "definition": {
                            "title": "Teams with the most tagged resources",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "toplist",
                            "requests": [
                                {
                                    "response_format": "scalar",
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "search": {
                                                "query": "team:* $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework vulnerability_type:misconfiguration"
                                            },
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "team",
                                                    "limit": 10,
                                                    "sort": {
                                                        "aggregation": "cardinality",
                                                        "order": "desc",
                                                        "metric": "@resource_id"
                                                    }
                                                }
                                            ]
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "sort": {
                                        "count": 10,
                                        "order_by": [
                                            {
                                                "type": "formula",
                                                "index": 0,
                                                "order": "desc"
                                            }
                                        ]
                                    }
                                }
                            ]
                        },
                        "layout": {
                            "x": 0,
                            "y": 2,
                            "width": 4,
                            "height": 2
                        }
                    },
                    {
                        "id": 486845723671134,
                        "definition": {
                            "title": "Tagged resources - team",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "toplist",
                            "requests": [
                                {
                                    "response_format": "scalar",
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "search": {
                                                "query": "team:* $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework vulnerability_type:misconfiguration"
                                            },
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "@resource_type",
                                                    "limit": 10,
                                                    "sort": {
                                                        "aggregation": "cardinality",
                                                        "order": "desc",
                                                        "metric": "@resource_id"
                                                    }
                                                }
                                            ]
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "sort": {
                                        "count": 10,
                                        "order_by": [
                                            {
                                                "type": "formula",
                                                "index": 0,
                                                "order": "desc"
                                            }
                                        ]
                                    }
                                }
                            ]
                        },
                        "layout": {
                            "x": 4,
                            "y": 2,
                            "width": 4,
                            "height": 2
                        }
                    },
                    {
                        "id": 5508755774518240,
                        "definition": {
                            "title": "Untagged resources - team",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "toplist",
                            "requests": [
                                {
                                    "response_format": "scalar",
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "search": {
                                                "query": "-team:* $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework vulnerability_type:misconfiguration"
                                            },
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "@resource_type",
                                                    "limit": 10,
                                                    "sort": {
                                                        "aggregation": "cardinality",
                                                        "order": "desc",
                                                        "metric": "@resource_id"
                                                    }
                                                }
                                            ]
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "sort": {
                                        "count": 10,
                                        "order_by": [
                                            {
                                                "type": "formula",
                                                "index": 0,
                                                "order": "desc"
                                            }
                                        ]
                                    }
                                }
                            ]
                        },
                        "layout": {
                            "x": 8,
                            "y": 2,
                            "width": 4,
                            "height": 2
                        }
                    },
                    {
                        "id": 1272175564434212,
                        "definition": {
                            "title": "Percentage of tagged resources - service",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "query_value",
                            "requests": [
                                {
                                    "response_format": "scalar",
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query2",
                                            "search": {
                                                "query": "$team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework vulnerability_type:misconfiguration"
                                            },
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": []
                                        },
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "search": {
                                                "query": "service:* $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework vulnerability_type:misconfiguration"
                                            },
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": []
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "query1 / query2 * 100"
                                        }
                                    ],
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "value": 0,
                                            "palette": "custom_text",
                                            "custom_fg_color": "#0014ad"
                                        }
                                    ]
                                }
                            ],
                            "autoscale": true,
                            "custom_unit": "%",
                            "precision": 1
                        },
                        "layout": {
                            "x": 0,
                            "y": 4,
                            "width": 4,
                            "height": 1
                        }
                    },
                    {
                        "id": 4121920434499282,
                        "definition": {
                            "title": "Tagged resources - service",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "query_value",
                            "requests": [
                                {
                                    "response_format": "scalar",
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "search": {
                                                "query": "service:* $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework vulnerability_type:misconfiguration"
                                            },
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": []
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "value": 0,
                                            "palette": "green_on_white"
                                        }
                                    ]
                                }
                            ],
                            "autoscale": true,
                            "precision": 2
                        },
                        "layout": {
                            "x": 4,
                            "y": 4,
                            "width": 4,
                            "height": 1
                        }
                    },
                    {
                        "id": 4816588766900452,
                        "definition": {
                            "title": "Untagged resources - service",
                            "title_size": "16",
                            "title_align": "left",
                            "time": {},
                            "type": "query_value",
                            "requests": [
                                {
                                    "response_format": "scalar",
                                    "queries": [
                                        {
                                            "name": "query1",
                                            "data_source": "compliance_findings",
                                            "search": {
                                                "query": "vulnerability_type:misconfiguration -service:* $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework"
                                            },
                                            "indexes": [
                                                "*"
                                            ],
                                            "group_by": [],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "storage": "hot"
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "value": 0,
                                            "palette": "red_on_white"
                                        }
                                    ]
                                }
                            ],
                            "autoscale": true,
                            "precision": 2
                        },
                        "layout": {
                            "x": 8,
                            "y": 4,
                            "width": 4,
                            "height": 1
                        }
                    },
                    {
                        "id": 1437529553699974,
                        "definition": {
                            "title": "Services with the most tagged resources",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "toplist",
                            "requests": [
                                {
                                    "response_format": "scalar",
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "search": {
                                                "query": "service:* $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework vulnerability_type:misconfiguration"
                                            },
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "team",
                                                    "limit": 10,
                                                    "sort": {
                                                        "aggregation": "cardinality",
                                                        "order": "desc",
                                                        "metric": "@resource_id"
                                                    }
                                                }
                                            ]
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "sort": {
                                        "count": 10,
                                        "order_by": [
                                            {
                                                "type": "formula",
                                                "index": 0,
                                                "order": "desc"
                                            }
                                        ]
                                    }
                                }
                            ]
                        },
                        "layout": {
                            "x": 0,
                            "y": 5,
                            "width": 4,
                            "height": 2
                        }
                    },
                    {
                        "id": 5635845433924114,
                        "definition": {
                            "title": "Tagged resources - service",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "toplist",
                            "requests": [
                                {
                                    "response_format": "scalar",
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "search": {
                                                "query": "service:* $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework vulnerability_type:misconfiguration"
                                            },
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "@resource_type",
                                                    "limit": 10,
                                                    "sort": {
                                                        "aggregation": "cardinality",
                                                        "order": "desc",
                                                        "metric": "@resource_id"
                                                    }
                                                }
                                            ]
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "sort": {
                                        "count": 10,
                                        "order_by": [
                                            {
                                                "type": "formula",
                                                "index": 0,
                                                "order": "desc"
                                            }
                                        ]
                                    }
                                }
                            ]
                        },
                        "layout": {
                            "x": 4,
                            "y": 5,
                            "width": 4,
                            "height": 2
                        }
                    },
                    {
                        "id": 7083630780764002,
                        "definition": {
                            "title": "Untagged resources - service",
                            "title_size": "16",
                            "title_align": "left",
                            "time": {},
                            "type": "toplist",
                            "requests": [
                                {
                                    "response_format": "scalar",
                                    "queries": [
                                        {
                                            "name": "query1",
                                            "data_source": "compliance_findings",
                                            "search": {
                                                "query": "vulnerability_type:misconfiguration -service:* $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework"
                                            },
                                            "indexes": [
                                                "*"
                                            ],
                                            "group_by": [
                                                {
                                                    "facet": "@resource_type",
                                                    "limit": 10,
                                                    "sort": {
                                                        "aggregation": "cardinality",
                                                        "order": "desc",
                                                        "metric": "@resource_id"
                                                    },
                                                    "should_exclude_missing": true
                                                }
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "storage": "hot"
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "sort": {
                                        "count": 10,
                                        "order_by": [
                                            {
                                                "type": "formula",
                                                "index": 0,
                                                "order": "desc"
                                            }
                                        ]
                                    }
                                }
                            ],
                            "style": {}
                        },
                        "layout": {
                            "x": 8,
                            "y": 5,
                            "width": 4,
                            "height": 2
                        }
                    },
                    {
                        "id": 71554036235084,
                        "definition": {
                            "title": "Percentage of tagged resources - env",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "query_value",
                            "requests": [
                                {
                                    "response_format": "scalar",
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "search": {
                                                "query": "env:* $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework vulnerability_type:misconfiguration"
                                            },
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": []
                                        },
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query2",
                                            "search": {
                                                "query": "$team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework vulnerability_type:misconfiguration"
                                            },
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": []
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "query1 / query2 * 100"
                                        }
                                    ],
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "value": 0,
                                            "palette": "custom_text",
                                            "custom_fg_color": "#0014ad"
                                        }
                                    ]
                                }
                            ],
                            "autoscale": true,
                            "custom_unit": "%",
                            "precision": 1
                        },
                        "layout": {
                            "x": 0,
                            "y": 7,
                            "width": 4,
                            "height": 1
                        }
                    },
                    {
                        "id": 3216980961061558,
                        "definition": {
                            "title": "Tagged resources - env",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "query_value",
                            "requests": [
                                {
                                    "response_format": "scalar",
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "search": {
                                                "query": "env:* $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework vulnerability_type:misconfiguration"
                                            },
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": []
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "value": 0,
                                            "palette": "green_on_white"
                                        }
                                    ]
                                }
                            ],
                            "autoscale": true,
                            "precision": 2
                        },
                        "layout": {
                            "x": 4,
                            "y": 7,
                            "width": 4,
                            "height": 1
                        }
                    },
                    {
                        "id": 66054820834442,
                        "definition": {
                            "title": "Untagged resources - env",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "query_value",
                            "requests": [
                                {
                                    "response_format": "scalar",
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "search": {
                                                "query": "-env:* $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework vulnerability_type:misconfiguration"
                                            },
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": []
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "conditional_formats": [
                                        {
                                            "comparator": ">",
                                            "value": 0,
                                            "palette": "red_on_white"
                                        }
                                    ]
                                }
                            ],
                            "autoscale": true,
                            "precision": 2
                        },
                        "layout": {
                            "x": 8,
                            "y": 7,
                            "width": 4,
                            "height": 1
                        }
                    },
                    {
                        "id": 2689699743203848,
                        "definition": {
                            "title": "Envs with the most tagged resources",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "toplist",
                            "requests": [
                                {
                                    "response_format": "scalar",
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "search": {
                                                "query": "env:* $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework vulnerability_type:misconfiguration"
                                            },
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "env",
                                                    "limit": 10,
                                                    "sort": {
                                                        "aggregation": "cardinality",
                                                        "order": "desc",
                                                        "metric": "@resource_id"
                                                    }
                                                }
                                            ]
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "sort": {
                                        "count": 10,
                                        "order_by": [
                                            {
                                                "type": "formula",
                                                "index": 0,
                                                "order": "desc"
                                            }
                                        ]
                                    }
                                }
                            ]
                        },
                        "layout": {
                            "x": 0,
                            "y": 8,
                            "width": 4,
                            "height": 2
                        }
                    },
                    {
                        "id": 8894663265610696,
                        "definition": {
                            "title": "Tagged resources - env",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "toplist",
                            "requests": [
                                {
                                    "response_format": "scalar",
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "search": {
                                                "query": "env:* $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework vulnerability_type:misconfiguration"
                                            },
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "@resource_type",
                                                    "limit": 10,
                                                    "sort": {
                                                        "aggregation": "cardinality",
                                                        "order": "desc",
                                                        "metric": "@resource_id"
                                                    }
                                                }
                                            ]
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "sort": {
                                        "count": 10,
                                        "order_by": [
                                            {
                                                "type": "formula",
                                                "index": 0,
                                                "order": "desc"
                                            }
                                        ]
                                    }
                                }
                            ]
                        },
                        "layout": {
                            "x": 4,
                            "y": 8,
                            "width": 4,
                            "height": 2
                        }
                    },
                    {
                        "id": 2580214462460598,
                        "definition": {
                            "title": "Untagged resources - env",
                            "title_size": "16",
                            "title_align": "left",
                            "type": "toplist",
                            "requests": [
                                {
                                    "response_format": "scalar",
                                    "queries": [
                                        {
                                            "data_source": "compliance_findings",
                                            "name": "query1",
                                            "search": {
                                                "query": "-env:* $team $azure_subscription_id $env $service $aws_account_id $gcp_project_id $framework vulnerability_type:misconfiguration"
                                            },
                                            "indexes": [
                                                "*"
                                            ],
                                            "compute": {
                                                "aggregation": "cardinality",
                                                "metric": "@resource_id"
                                            },
                                            "group_by": [
                                                {
                                                    "facet": "@resource_type",
                                                    "limit": 10,
                                                    "sort": {
                                                        "aggregation": "cardinality",
                                                        "order": "desc",
                                                        "metric": "@resource_id"
                                                    }
                                                }
                                            ]
                                        }
                                    ],
                                    "formulas": [
                                        {
                                            "formula": "query1"
                                        }
                                    ],
                                    "sort": {
                                        "count": 10,
                                        "order_by": [
                                            {
                                                "type": "formula",
                                                "index": 0,
                                                "order": "desc"
                                            }
                                        ]
                                    }
                                }
                            ]
                        },
                        "layout": {
                            "x": 8,
                            "y": 8,
                            "width": 4,
                            "height": 2
                        }
                    }
                ]
            },
            "layout": {
                "x": 0,
                "y": 5,
                "width": 12,
                "height": 1
            }
        }
    ],
    "template_variables": [
        {
            "name": "team",
            "prefix": "team",
            "available_values": [],
            "default": "*"
        },
        {
            "name": "env",
            "prefix": "env",
            "available_values": [],
            "default": "*"
        },
        {
            "name": "service",
            "prefix": "service",
            "available_values": [],
            "default": "*"
        },
        {
            "name": "framework",
            "prefix": "framework",
            "available_values": [],
            "default": "*"
        },
        {
            "name": "aws_account_id",
            "prefix": "account_id",
            "available_values": [],
            "default": "*"
        },
        {
            "name": "azure_subscription_id",
            "prefix": "subscription_id",
            "available_values": [],
            "default": "*"
        },
        {
            "name": "gcp_project_id",
            "prefix": "project_id",
            "available_values": [],
            "default": "*"
        }
    ],
    "layout_type": "ordered",
    "notify_list": [],
    "reflow_type": "fixed"
}
EOF
}