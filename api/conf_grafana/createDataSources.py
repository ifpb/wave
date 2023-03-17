import requests
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

path_env = Path(os.path.abspath(""))
IP_API_GR = os.getenv("IP_HOST_API")
URL_API_DS = f'http://{IP_API_GR}:3000/api/datasources'

headers = {
    'Content-Type': 'application/json',
    'Authorization': ''
}
data = {
    'name': 'data_src_server',
    'type': 'prometheus',
    'url': '',
    'access': 'proxy',
    'isDefault': True
}


def create_data_src(host_server, api_key):

    headers['Authorization'] = f'Bearer {api_key}'
    data['url'] = f'http://{host_server}:9090'

    load_dotenv()

    grafana_data_src = os.getenv("DATASOURCE_UID")

    if grafana_data_src is not None:
        return grafana_data_src

    response = requests.post(URL_API_DS, headers=headers, json=data)

    if response.status_code == 200:

        data_src_uid = response.json()["datasource"]["uid"]
        env_dir = Path(path_env, ".env")

        with open(env_dir, "a") as env_file:
            env_file.write(
                f"\nDATASOURCE_UID=\'{data_src_uid}\'")
            os.environ["DATASOURCE_UID"] = data_src_uid
            return data_src_uid

    else:
        return response.json()
