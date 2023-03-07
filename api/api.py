import os
from provision import Provision
from pathlib import Path
from flask import Flask
from flask_restx import Resource, Api
app = Flask(__name__)
api = Api(app, version='1.0', title='LoadGen API',
    description='Provision API LoadGen')

path_app = Path(os.path.abspath("app"))    
config_dir = Path(path_app,"provision") 
pro_env = Provision(config_dir)

@api.route('/provision/up')
class ProvisionInit(Resource):
    def get(self):
        pro_env.up()
        return {'provision': 'up'}

@api.route('/provision/down')
class ProvisionDestroy(Resource):
    def get(self):
        pro_env.down()
        return {'provision': 'down'}

@api.route('/provision/results')
class ProvisionResult(Resource):
    def get(self):
        analysis_result = pro_env.result()
        return analysis_result
        
@api.route('/provision/execute')
class ProvisionExcuteScenario(Resource):
    def get(self):
        pro_env.execute_scenario(15)
        return {'provision': 'executed'}
        
@api.route('/provision/execute/sin/<durantion>')
@api.doc(params={'durantion': 'Sinusoid Duration'})
class ProvisionExcuteScenario(Resource):
    def get(self, durantion):
        pro_env.execute_scenario(durantion)
        return {'provision': 'executed'}

@app.errorhandler(404)
def not_found(error):
    return {'error': 'Not found'}, 404

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8181)

   
