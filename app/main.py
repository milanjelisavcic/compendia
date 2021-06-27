from flask import Flask
from flask import request
from flask import send_file
from flask_cors import CORS

from pdf2docx import Converter

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST', 'GET'])
@app.route('/test/', methods=['POST', 'GET'])
def root():
    if request.method == 'POST':
        file = request.files['file']
        pdf_file = f"res/{file.filename}"
        file.save(pdf_file)

        cv = Converter(pdf_file)
        cv.convert(f'res/{file.filename}.docx')
        cv.close()
        
        try:
            return send_file(f'res/{file.filename}.docx', attachment_filename='convert.docx')
        except Exception as e:
            return str(e)


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
