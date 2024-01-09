#!/usr/bin/python3

"""
AirnB clone - RESTful API
This file declares the Flask
application object
and registers blueprints from views

Additionally, it handles teardown
of the SQLAlchemy ORM and runs the app
"""
from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_db(self):
    """teardown"""
    storage.close()


if __name__ == '__main__':
    api_host = getenv('HBNB_API_HOST', '0.0.0.0')
    api_port = getenv('HBNB_API_PORT', 5000)

    app.run(host=api_host, port=api_port, threaded=True)
