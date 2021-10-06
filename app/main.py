from flask import Flask
from flask import render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', filenames=['test.txt'])


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
