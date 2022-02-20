from flask import *
import werkzeug
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'book/'

@app.route('/index')
def index():
    info={}
    info['name'] = 'name'
    return render_template('index.html', info = info)

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      filename = f.filename
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],str(filename)))
      return 'file uploaded successfully'

@app.route('/bookinfo')
def bookinfo():
    word = request.args.get('word')
    bookinfo={}
    bookinfo['word'] = word
    return render_template('bookinfo.html', info = bookinfo)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')