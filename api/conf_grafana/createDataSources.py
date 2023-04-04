import os
import requests
from dotenv import load_dotenv, get_key, set_key
load_dotenv()
IP_API_GR = os.getenv("IP_HOST_API")
URL_API_DS = f'http://{IP_API_GR}:3000/api/datasources'

headers = {
    'Content-Type': 'application/json',
    'Authorization': ''
}
prometheus_payload = {
    'name': 'prometheus_data_src',
    'type': 'prometheus',
    'url': '',
    'access': 'proxy',
    'isDefault': True
}

csv_payload = {
    "name": "csv_data_src",
    "type": "marcusolsson-csv-datasource",
    "url": "/var/lib/grafana/csv/test.csv",
    "access": "Proxy",
    "jsonData": {
        "storage": "local",
        "csvFields": [
           {"name": "Time", "type": "time"},
           {"name": "Instances", "type": "number"},
        ],
        "csvDelimiter": ",",
        "csvSkipRows": 1,
        "csvCommentCharacter": "#"

    }

}


def create_data_src(url, api_key, type):
    headers['Authorization'] = f'Bearer {api_key}'
    payload = csv_payload if type == 'csv' else prometheus_payload

    payload['url'] = url

    PROMTS_DATASRC_UID = os.getenv('PROMTS_DATASRC_UID')
    PROMTS_DATASRC_ID = os.getenv('PROMTS_DATASRC_ID')

    CSV_DATASRC_UID = os.getenv('CSV_DATASRC_UID')
    CSV_DATASRC_ID = os.getenv('CSV_DATASRC_ID')

    if type == 'csv':
        if CSV_DATASRC_ID:

            CSV_DATASRC_UID = get_key(
                '.env', 'CSV_DATASRC_UID', encoding='utf-8')
            CSV_DATASRC_ID = get_key(
                '.env', 'CSV_DATASRC_ID', encoding='utf-8')

            response_get_csv = requests.get(
                f"{URL_API_DS}/{CSV_DATASRC_ID}", headers=headers)

            if response_get_csv.status_code == 200:
                if response_get_csv.json():
                    update_data_src(url, headers, csv_payload,
                                    CSV_DATASRC_ID)
                    return {
                        'uid': CSV_DATASRC_UID,
                        'id': CSV_DATASRC_ID
                    }

    else:
        if PROMTS_DATASRC_ID:

            PROMTS_DATASRC_UID = get_key(
                '.env', 'PROMTS_DATASRC_UID', encoding='utf-8')
            PROMTS_DATASRC_ID = get_key(
                '.env', 'PROMTS_DATASRC_ID', encoding='utf-8')

            response_get_promts = requests.get(
                f"{URL_API_DS}/{PROMTS_DATASRC_ID}", headers=headers)

            if response_get_promts.status_code == 200:
                if response_get_promts.json():
                    update_data_src(url, headers, prometheus_payload,
                                    PROMTS_DATASRC_ID)
                    return {
                        'uid': PROMTS_DATASRC_UID,
                        'id': PROMTS_DATASRC_ID
                    }

    response = requests.post(
        URL_API_DS, headers=headers, json=payload)

    if response.status_code == 200:

        data_src_uid = response.json()["datasource"]["uid"]
        data_src_id = response.json()["datasource"]["id"]

        if type == 'prometheus':
            set_key('.env', "PROMTS_DATASRC_UID", f'{data_src_uid}',
                    quote_mode='always', export=False, encoding='utf-8')
            set_key('.env', "PROMTS_DATASRC_ID", f'{data_src_id}',
                    quote_mode='always', export=False, encoding='utf-8')
            return {
                'uid': data_src_uid,
                'id': data_src_id
            }
        if type == 'csv':

            set_key('.env', "CSV_DATASRC_UID", f'{data_src_uid}',
                    quote_mode='always', export=False, encoding='utf-8')
            set_key('.env', "CSV_DATASRC_ID", f'{data_src_id}',
                    quote_mode='always', export=False, encoding='utf-8')
            return {
                'uid': data_src_uid,
                'id': data_src_id
            }
    else:
        return response.json()


def update_data_src(url, headers, payload, data_src_id):
    payload['url'] = url
    response = requests.put(f'{URL_API_DS}/{data_src_id}',
                            headers=headers,
                            json=payload)
    if response.status_code == 200:
        response.json()['datasource']['uid']
    else:
        return response.json()
