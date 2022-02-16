from flask import *

app = Flask(__name__)

@app.route('/index')
def index():
    info={}
    info['name'] = 'name'
    return render_template('index.html', info = info)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')