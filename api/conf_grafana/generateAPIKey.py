import requests
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

path_env = Path(os.path.abspath(""))
IP_API_GR = os.getenv("IP_HOST_API")
URL_AUTH_API = f'http://{IP_API_GR}:3000/api/auth/keys'

headers = {
    'Content-Type': 'application/json',
}

data = '''
    {
        "name": "api_key",
        "role": "Admin"
    }
    '''


def create_api_key_grf():

    grafana_api_key = os.getenv("GRAFANA_API_KEY")

    if grafana_api_key is not None:
        return grafana_api_key

    response = requests.post(URL_AUTH_API, headers=headers,
                             data=data, auth=('admin', 'admin'))

    if response.status_code == 200:
        # Extrair o valor da API Key do corpo da resposta
        api_key = response.json()["key"]
        env_dir = Path(path_env, ".env")
        # Armazenar o valor da API Key em uma variável de ambiente
        with open(env_dir, "a") as env_file:
            env_file.write(
                f"\nGRAFANA_API_KEY=\'{api_key}\'")
            os.environ["GRAFANA_API_KEY"] = api_key
            return api_key

    else:
        return response.json()
