import views
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "20230314"
    views.configure(app)
    return app


if __name__ == '__main__':
    create_app().run(debug=True, host='0.0.0.0')
