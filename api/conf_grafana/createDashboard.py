import os
import json
import requests
from dotenv import load_dotenv, set_key, get_key

load_dotenv()

IP_API_GR = os.getenv("IP_HOST_API")
URL_API_DASHBOARD = f'http://{IP_API_GR}:3000/api/dashboards'


headers = {"Content-Type": "application/json",
           "Authorization": ""}
# Definir as informações do dashboard
data = {
    "dashboard": {
        "annotations": {
            "list": [
                 {
                     "builtIn": 1,
                     "datasource": {
                         "type": "datasource",
                         "uid": "grafana"
                     },
                     "enable": True,
                     "hide": True,
                     "iconColor": "rgba(0, 211, 255, 1)",
                     "name": "Annotations & Alerts",
                     "target": {
                         "limit": 100,
                         "matchAny": False,
                         "tags": [],
                         "type": "dashboard"
                     },
                     "type": "dashboard"
                 }
            ]
        },
        "description": "This is a modification of dashboard.",
        "editable": True,
        "fiscalYearStartMonth": 0,
        "graphTooltip": 0,
        "id": None,
        "links": [],
        "liveNow": False,
        "panels": [


            {
                "datasource": {
                    "type": "prometheus",
                    "uid": ""
                },
                "aliasColors": {
                    "receive_packets_eth0": "#7EB26D",
                    "receive_packets_lo": "#E24D42",
                    "transmit_packets_eth0": "#7EB26D",
                    "transmit_packets_lo": "#E24D42"
                },
                "bars": False,
                "dashLength": 10,
                "dashes": False,

                "description": "",
                "fill": 2,
                "fillGradient": 0,
                "gridPos": {
                    "h": 10,
                    "w": 12,
                    "x": 0,
                    "y": 1
                },
                "hiddenSeries": False,
                "id": 1,
                "legend": {
                    "alignAsTable": True,
                    "avg": True,
                    "current": True,
                    "max": True,
                    "min": True,
                    "rightSide": False,
                    "show": True,
                    "sideWidth": 300,
                    "total": False,
                    "values": True
                },
                "lines": True,
                "linewidth": 1,
                "links": [],
                "nullPointMode": "null",
                "options": {
                    "alertThreshold": True
                },
                "percentage": False,
                "pluginVersion": "9.4.3",
                "pointradius": 5,
                "points": False,
                "renderer": "flot",
                "seriesOverrides": [
                    {
                        "alias": "/.*Trans.*/",
                        "transform": "negative-Y"
                    },
                    {
                        "alias": "/.*lo.*/",
                        "color": "#7EB26D"
                    },
                    {
                        "alias": "/.*eth0.*/",
                        "color": "#EAB839"
                    },
                    {
                        "alias": "/.*eth1.*/",
                        "color": "#6ED0E0"
                    },
                    {
                        "alias": "/.*eth2.*/",
                        "color": "#EF843C"
                    },
                    {
                        "alias": "/.*eth3.*/",
                        "color": "#E24D42"
                    },
                    {
                        "alias": "/.*eth4.*/",
                        "color": "#1F78C1"
                    },
                    {
                        "alias": "/.*eth5.*/",
                        "color": "#BA43A9"
                    }
                ],
                "spaceLength": 10,
                "stack": False,
                "steppedLine": False,
                "targets": [

                    {
                        "datasource": {

                            "uid": "Prometheus"
                        },
                        "editorMode": "code",
                        "expr": "irate(node_network_receive_bytes_total{instance=~\"$instance\"}[5m])",
                        "format": "time_series",
                        "intervalFactor": 2,
                        "legendFormat": "{{device}} - Receive",
                        "range": True,
                        "refId": "O",
                        "step": 4
                    },
                    {
                        "datasource": {

                            "uid": "Prometheus"
                        },
                        "editorMode": "code",
                        "expr": "irate(node_network_transmit_bytes_total{instance=~\"$instance\"}[5m])",
                        "format": "time_series",
                        "intervalFactor": 2,
                        "legendFormat": "{{device}} - Transmit",
                        "range": True,
                        "refId": "P",
                        "step": 4
                    }
                ],
                "thresholds": [],
                "timeRegions": [],
                "title": "Network Traffic by Mb",
                "tooltip": {
                    "shared": True,
                    "sort": 0,
                    "value_type": "individual"
                },
                "type": "graph",
                "xaxis": {
                    "mode": "time",
                    "show": True,
                    "values": []
                },
                "yaxes": [
                    {
                        "$$hashKey": "object:584",
                        "format": "bps",
                        "label": "Bytes out (-) / in (+)",
                        "logBase": 1,
                        "show": True
                    },
                    {
                        "$$hashKey": "object:585",
                        "format": "short",
                        "logBase": 1,
                        "show": False
                    }
                ],
                "yaxis": {
                    "align": False
                }
            },
            {
                "datasource": {
                    "type": "marcusolsson-csv-datasource",
                            "uid": ""
                },
                "fieldConfig": {
                    "defaults": {
                        "color": {
                            "mode": "palette-classic"
                        },
                        "custom": {
                            "axisCenteredZero": False,
                            "axisColorMode": "text",
                            "axisLabel": "",
                            "axisPlacement": "auto",
                            "barAlignment": 0,
                            "drawStyle": "line",
                            "fillOpacity": 25,
                            "gradientMode": "none",
                            "hideFrom": {
                                "legend": False,
                                "tooltip": False,
                                "viz": False
                            },
                            "lineInterpolation": "smooth",
                            "lineWidth": 1,
                            "pointSize": 4,
                            "scaleDistribution": {
                                "type": "linear"
                            },
                            "showPoints": "auto",
                            "spanNulls": False,
                            "stacking": {
                                "group": "A",
                                "mode": "none"
                            },
                            "thresholdsStyle": {
                                "mode": "off"
                            }
                        },
                        "mappings": [],
                        "thresholds": {
                            "mode": "absolute",
                                    "steps": [
                                        {
                                            "color": "green",
                                            "value": None
                                        },
                                        {
                                            "color": "red",
                                            "value": 80
                                        }
                                    ]
                        }
                    },
                    "overrides": []
                },
                "gridPos": {
                    "h": 8,
                    "w": 12,
                    "x": 0,
                    "y": 0
                },
                "id": None,
                "options": {
                    "legend": {
                        "calcs": [],
                        "displayMode": "list",
                        "placement": "bottom",
                        "showLegend": True
                    },
                    "tooltip": {
                        "mode": "single",
                                "sort": "none"
                    }
                },
                "pluginVersion": "9.4.3",
                "targets": [
                    {
                        "datasource": {
                            "uid": "marcusolsson-csv-datasource",
                        },
                        "decimalSeparator": ".",
                        "delimiter": ",",
                        "header": True,
                        "ignoreUnknown": False,
                        "refId": "A",
                        "schema": [
                            {
                                "name": "Time",
                                        "type": "time"
                            },
                            {
                                "name": "Instances",
                                        "type": "number"
                            }
                        ],
                        "skipRows": 0,
                        "timezone": "America/Recife"
                    }
                ],
                "title": "Instances Iperf",
                "transparent": True,
                "type": "timeseries"
            }
        ],
        "refresh": "5s",
        "revision": 1,
        "schemaVersion": 38,
        "style": "dark",
        "tags": [
            "Prometheus"
        ],
        "templating": {
            "list": [
                {
                    "current": {
                        "selected": False,
                        "text": "localhost:9100",
                        "value": "localhost:9100"
                    },
                    "datasource": {

                        "type": "prometheus",
                        "uid": ""
                    },
                    "definition": "label_values(node_exporter_build_info, instance)",
                    "hide": 0,
                    "includeAll": False,
                    "label": "Instance:",
                    "multi": False,
                    "name": "instance",
                    "options": [],
                    "query": {
                        "query": "label_values(node_exporter_build_info, instance)",
                        "refId": "My Datasource-instance-Variable-Query"
                    },
                    "refresh": 1,
                    "regex": "",
                    "skipUrlSync": False,
                    "sort": 1,
                    "tagValuesQuery": "",
                    "tagsQuery": "",
                    "type": "query",
                    "useTags": False
                }
            ]
        },
        "time": {"from": "now-30m", "to": "now"},
        "timezone": "browser",
        "title": "Wave - Analysis Results"
    }
}

# Criar o dashboard


def create_dashboard(api_key, promts_data_src_uid, csv_data_src_uid):

    headers["Authorization"] = f"Bearer {api_key}"

    data["dashboard"]["panels"][0][
        "datasource"]["uid"] = f"{promts_data_src_uid}"
    data["dashboard"]["templating"]["list"][0][
        "datasource"]["uid"] = f"{promts_data_src_uid}"

    data["dashboard"]["panels"][1][
        "datasource"]["uid"] = f"{csv_data_src_uid}"

    DASHBOARD_UID = os.getenv('DASHBOARD_UID')
    if DASHBOARD_UID:
        DASHBOARD_UID = get_key('.env', 'DASHBOARD_UID', encoding='utf-8')
        response_dashb = requests.get(
            f"{URL_API_DASHBOARD}/uid/{DASHBOARD_UID}", headers=headers)
        if response_dashb.status_code == 200:
            return DASHBOARD_UID

    response = requests.post(
        f"{URL_API_DASHBOARD}/db", headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        # Extrair o valor do uid dashbord do corpo da resposta
        dashb_uid = response.json()["uid"]

        # Armazenar o valor do uid em uma variável de ambiente
        set_key(".env", "DASHBOARD_UID", f'{dashb_uid}',
                quote_mode='always', export=False, encoding='utf-8')
        return dashb_uid
    else:
        return response.json()
