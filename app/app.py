import views
from flask import Flask


def create_app():
    app = Flask(__name__)
    views.configure(app)
    return app


if __name__ == '__main__':
    create_app().run(debug=True, host='0.0.0.0')
