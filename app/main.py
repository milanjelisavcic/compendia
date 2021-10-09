from flask import Flask
from flask import render_template
from flask import request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    display_text = ''
    if request.method == 'POST':
        display_text = request.form['textbox']

    return render_template('index.html', display_text=display_text)


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
