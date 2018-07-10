import platform
import json

from flask import Flask, request
from werkzeug.utils import secure_filename


app = Flask(__name__)


@app.route('/', methods=['GET'])
def tester_app():
    
    return ("Hello World from {}".format(platform.node()),
                                         200,
                                         {"content-type": "text/plain"})


if __name__ == '__main__':
    app.run('0.0.0.0', port='7070')
