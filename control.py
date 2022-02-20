from flask import *

import db
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
    bookinfo={}
    word = request.args.get('word')
    if word is not None:
        info = db.select_wordinfo_by_word(word)
        if len(info) != 0:
            bookinfo['word'] = info[0]['word']
            bookinfo['interpretation'] = info[0]['interpretation']
            bookinfo['imgurl'] = info[0]['imgurl']
            bookinfo['other'] = info[0]['other']
    return render_template('bookinfo.html', info = bookinfo)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')