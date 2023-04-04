import os
from provision import Provision
from pathlib import Path
from flask import Flask
from flask_restx import Resource, Api, reqparse
from conf_grafana import generateAPIKey, createDataSources, createDashboard

app = Flask(__name__)
api = Api(app, version='1.0', title='LoadGen API',
          description='Provision API LoadGen',
          default='API', default_label='Default namespace')

path_app = Path(os.path.abspath("app"))
config_dir = Path(path_app, "provision")
pro_env = Provision(config_dir)

parser_sin = reqparse.RequestParser()
parser_sin.add_argument('a', type=str, help='Sinusoid - Amplitude')
parser_sin.add_argument('p', type=str, help='Sinusoid - Period')
parser_sin.add_argument('d', type=str, help='Sinusoid - Duration')
parser_sin.add_argument('l', type=str, help='Sinusoid - Lambd')

parser_flashc = reqparse.RequestParser()
parser_flashc.add_argument('nl', type=str, help='Flashcrowd - Normal Load')
parser_flashc.add_argument('sl', type=str, help='Flashcrowd - Shock Level')
parser_flashc.add_argument('crd', type=str, help='Flashcrowd - Const RanpDown')

parser_config_grafana = reqparse.RequestParser()
parser_config_grafana.add_argument(
    'host_promts', type=str, help='IP Host runner Promethues')
parser_config_grafana.add_argument(
    'wave_model', type=str, help='Wave model')


@api.route('/provision/up')
class ProvisionInit(Resource):
    def get(self):
        pro_env.up()
        return {'provision': 'up'}


@api.route('/provision/grafana/config')
class ProvisionGrafana(Resource):
    @api.doc(parser=parser_config_grafana)
    def get(self):
        # conf Grafana
        host_promts = parser_config_grafana.parse_args()['host_promts']
        wave_model = parser_config_grafana.parse_args()['wave_model']

        api_key = generateAPIKey.create_api_key_grf()

        promts_data_src_uid = createDataSources.create_data_src(
            f'http://{host_promts}:9090', api_key, 'prometheus')['uid']

        csv_data_src_uid = createDataSources.create_data_src(
            f'/var/lib/grafana/csv/{wave_model}_wave.csv',
            api_key, 'csv')['uid']

        dashboard_uid = createDashboard.create_dashboard(
            api_key, promts_data_src_uid, csv_data_src_uid)

        response = {
            'provision': 'executed',
            'apiKey': api_key,
            'promtsDataSrcUid': promts_data_src_uid,
            'CSVDataSrcUid': csv_data_src_uid,
            'dashboardUid': dashboard_uid
        }

        return response


@api.route('/provision/down')
class ProvisionDestroy(Resource):
    def get(self):
        pro_env.down()
        return {'provision': 'down'}


@api.route('/provision/execute/model/sin')
class ProvisionExcuteScenarioSin(Resource):
    @api.doc(parser=parser_sin)
    def get(self):
        args = parser_sin.parse_args()
        pro_env.execute_scenario(
            'sin', args['a'], args['p'], args['d'], args['l'])

        return {'provision': 'executed'}


@api.route('/provision/execute/model/flashc')
class ProvisionExcuteScenarioFlashc(Resource):
    @api.doc(parser=parser_flashc)
    def get(self):
        args = parser_flashc.parse_args()
        pro_env.execute_scenario('flashc', args['nl'], args['sl'], args['crd'])
        return {'provision': 'executed'}


@app.errorhandler(404)
def not_found(error):
    return {'error': 'Not found'}, 404


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8181)
