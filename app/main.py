from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask_cors import CORS

from pdf2docx import Converter

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST', 'GET'])
def root():
    if request.method == 'POST':
        file = request.files['file']

        cv = Converter(file)
        cv.convert(f'res/{file}.docx')
        cv.close()

    return "TBA"


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
