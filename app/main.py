from flask import Flask
from flask import render_template
from flask import request
from flask_cors import CORS

from compendia.summarizers.huggingface import summarize

app = Flask(__name__)
CORS(app)


@app.route('/summarize', methods=['POST'])
def summar(text):
    return summarize(text)


@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ''
    if request.method == 'POST':
        input_text = request.form['textbox']
        summary = summar(input_text)

    return render_template('index.html', display_text=summary)


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
