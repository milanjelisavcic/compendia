from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST', 'GET'])
def root():
    return "TBA"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
