import requests
import json
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

path_env = Path(os.path.abspath(""))
IP_API_GR = os.getenv("IP_HOST_API")
URL_API_DASHBOARD = f'http://{IP_API_GR}:3000/api/dashboards/db'
DATASOURCE_UID = os.getenv("DATASOURCE_UID")

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
        "title": "Network Traffic"
    }
}

# Criar o dashboard


def create_dashboard(api_key, data_src_uid):

    load_dotenv()
    headers["Authorization"] = f"Bearer {api_key}"

    data["dashboard"]["panels"][0]["datasource"]["uid"] = f"{data_src_uid}"
    data["dashboard"]["templating"]["list"][0][
        "datasource"]["uid"] = f"{data_src_uid}"
    # data["dashboard"]["panels"][1]["datasource"]["uid"] = f"{data_src_uid}"
    print(data["dashboard"]["panels"][0]["datasource"]["uid"])

    grafana_dashboard = os.getenv("DASHBOARD_UID")

    if grafana_dashboard is not None:
        return grafana_dashboard

    response = requests.post(
        URL_API_DASHBOARD, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        # Extrair o valor do uid dashbord do corpo da resposta
        dashb_uid = response.json()["uid"]

        # Armazenar o valor do uid em uma variável de ambiente
        with open(".env", "a") as env_file:
            env_file.write(f"\nDASHBOARD_UID=\'{dashb_uid}\'")
            os.environ["DASHBOARD_UID"] = dashb_uid
            return dashb_uid

    else:
        return response.json()
