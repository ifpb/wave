import os
import requests
from flask import Flask, render_template, request, redirect, abort
from pathlib import Path
from provision.confYaml import ConfYaml


def configure(app):
    path_app = Path(os.path.abspath("app"))
    config_dir = Path(path_app, "provision")

    conf_yaml = ConfYaml()

    IP_HOST_API = os.environ.get("API_PROVISION")
    URL_API = f"http://{IP_HOST_API}:8181/provision"
    URL_GRAFANA = f"http://{IP_HOST_API}:3000/login"

    @app.route('/', methods=["GET", "POST"])
    def index():
        value = "Configurator - WAVE"

        if request.method == "GET":
            return render_template("index.html", value=value)
        else:
            conf = f"""\
---
- traffic: server
  ip: "{request.form.get("ipserver")}"
  gateway: "{request.form.get("gtwserver")}"
  ram: "{request.form.get('memserver')}"
  vcpu: "{request.form.get('cpuserver')}"
  platform: {request.form.get('plafmserver')}

- traffic: client
  ip: "{request.form.get("ipclient")}"
  gateway: "{request.form.get("gtwclient")}"
  ram: "{request.form.get('memclient')}"
  vcpu: "{request.form.get('cpuclient')}"
  platform: {request.form.get('plafmclient')}

"""
        if (request.form.get('select-model') == 'sin'):

            conf_model_sin = f"""\
- model: {request.form.get('select-model')}
  a: "{request.form.get('amp-sin')}"
  p: "{request.form.get('ped-sin')}"
  d: "{request.form.get('drn-sin')}"
  l: "{request.form.get('lmd-sin')}"
"""
            conf_yaml.set_conf(conf)
            conf_yaml.set_conf_model(conf+conf_model_sin)

        elif (request.form.get('select-model') == 'flashc'):

            conf_model_flashc = f"""\
- model: {request.form.get('select-model')}
  nl: "{request.form.get('nload-flashc')}"
  sl: "{request.form.get('shkl-flashc')}"
  crd: "{request.form.get('constrp-flashc')}"
"""
            conf_yaml.set_conf(conf)
            conf_yaml.set_conf_model(conf+conf_model_flashc)

        else:
            conf_yaml.set_conf(conf)

        return redirect('/config')

    # Render page with the configuration result to provision the environment

    @app.route('/config')
    def config_result():
        config_yaml_dir = Path(path_app, "provision", "config.yaml")

        if conf_yaml.valid_conf():
            try:
                with open(config_yaml_dir, "w") as f:
                    conf = conf_yaml.get_conf()
                    f.write(conf)
                    return render_template('config-result.html',
                                           conf=conf_yaml.get_conf_model())

            except FileNotFoundError:
                value = "Failed to generate the configuration file!"
                return render_template('default.html', value=value)
        else:
            value = """The configuration for provisioning was not completed,
        return to the Home page to set up the provisioning environment."""
            return render_template('default.html', value=value)

    # Requesting provisioning API

    @app.route('/up')
    def provision_up():
        try:
            resquest = requests.get(f"{URL_API}/up")
            res_result = resquest.json()

            if 'error' in res_result:
                abort(404)

            elif res_result["provision"] == "up":
                # flash(f"Provisionamento realizado com sucesso", "success")
                value = "Provisioning successful!"
                return render_template('default.html', value=value)

        except requests.exceptions.ConnectionError:
            value = "Connection API Fail!"
            return render_template('default.html', value=value)

    @app.route('/down')
    def provision_down():
        try:
            resquest = requests.get(f"{URL_API}/down")
            res_result = resquest.json()

            if 'error' in res_result:
                abort(404)
            elif res_result["provision"] == "down":

                value = "Environment destroyed successfully!"
                return render_template('default.html', value=value)

        except requests.exceptions.ConnectionError:
            value = "Connection API Fail!"
            return render_template('default.html', value=value)

    @app.route('/results')
    def analysis_result():
        try:
            resquest = requests.get(f"{URL_API}/results")
            res_analysis_result = resquest.json()

            if 'error' in res_analysis_result:
                abort(404)

            return render_template('analysis-result.html',
                                   res_analysis_result=res_analysis_result, grafana=URL_GRAFANA)

        except requests.exceptions.ConnectionError:
            value = "Connection API Fail!"
            return render_template('default.html', value=value)

    @app.route('/execute')
    def execute_scenario():
        conf_dict = conf_yaml.conf_model_dict()
        try:
            if conf_dict[2]['model'] == 'sin':
                a = conf_dict[2]['a']
                p = conf_dict[2]['p']
                d = conf_dict[2]['d']
                l = conf_dict[2]['l']
                # print(a, p, d, l)
                resquest = requests.get(
                    f"{URL_API}/execute/model/sin?a={a}&p={p}&d={d}&l={l}")
                res_result = resquest.json()

            if conf_dict[2]['model'] == 'flashc':
                nl = conf_dict[2]['nl']
                sl = conf_dict[2]['sl']
                crd = conf_dict[2]['crd']
                # print(nl, sl, crd)
                resquest = requests.get(
                    f"{URL_API}/execute/model/flashc?nl={nl}&sl={sl}&crd={crd}")
                res_result = resquest.json()

            if 'error' in res_result:
                abort(404)
            elif res_result["provision"] == "executed":
                return redirect("/results")
        except requests.exceptions.ConnectionError:
            value = "Connection API Fail!"
            return render_template('default.html', value=value)

    @app.errorhandler(404)
    def not_found(error):
        value = error
        return render_template('default.html', value=value), 404
