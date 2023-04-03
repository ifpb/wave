import os
import requests
from dotenv import load_dotenv, set_key

load_dotenv()

IP_API_GR = os.getenv("IP_HOST_API")
URL_AUTH_API = f'http://{IP_API_GR}:3000/api/auth/keys'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}

data = '''
    {
        "name": "api_key",
        "role": "Admin"
    }
    '''


def create_api_key_grf():

    GRAFANA_API_KEY = os.getenv('GRAFANA_API_KEY')

    if existed_api_key():
        return GRAFANA_API_KEY

    response = requests.post(URL_AUTH_API, headers=headers,
                             data=data, auth=('admin', 'admin'))

    if response.status_code == 200:
        # Extrair o valor da API Key do corpo da resposta
        api_key = response.json()["key"]
        api_key_id = response.json()["id"]
        # Armazenar o valor da API Key em uma variável de ambiente
        set_key(".env", "GRAFANA_API_KEY", f'{api_key}',
                quote_mode='always', export=False, encoding='utf-8')
        set_key(".env", "GRAFANA_API_KEY_ID", f'{api_key_id}',
                quote_mode='always', export=False, encoding='utf-8')
        return api_key

    else:
        return response.json()


def existed_api_key():

    response = requests.get(f'{URL_AUTH_API}',
                            headers=headers, auth=('admin', 'admin'))
    if response.status_code == 200:

        if response.json():
            return str(response.json()[0]['id'])
        else:
            return None

    else:
        return response.json()
