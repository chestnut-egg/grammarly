from flask import *

import db
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'book/'

@app.route('/login',methods=['GET','POST'])
def login():
    info = {}
    if request.method == 'POST':
        print("login")
        account = request.form.get("account")
        password = request.form.get("password")
        print(account)
        print(password)
        info['account'] = account
        return render_template('login.html', info=info)
    return render_template('login.html', info = info)

@app.route('/register',methods=['GET','POST'])
def register():
    info = {}
    if request.method == 'POST':
        print("register")
        account = request.form.get("account")
        password = request.form.get("password")
        print(account)
        print(password)
        info['account'] = account
        return render_template('login.html', info=info)
    return render_template('login.html', info = info)

@app.route('/index')
def index():
    info={}
    info['name'] = 'name'
    return render_template('index.html', info = info)

@app.route('/test')
def test():
    info={}
    info['name'] = 'name'
    return render_template('test.html', info = info)

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