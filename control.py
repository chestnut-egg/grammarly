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
        print("获取账号")
        account = request.form.get("account")
        print(account)
        print("获取密码")
        password = request.form.get("password")
        print(password)
        info['account'] = account

        userinfo = db.select_user_by_account(account)
        if len(userinfo) == 0:
            info['wrong'] = "账号不存在"
            print("账号不存在")
            return render_template('login.html', info=info)
        else:
            realwd = userinfo[0]['password']
            print("真实密码")
            print(realwd)
            if password == realwd:
                print("登录成功")
                return render_template('index.html', info=info)
            else:
                info['wrong'] = "密码错误"
                print("密码错误")
                return render_template('login.html', info=info)

    return render_template('login.html', info = info)

@app.route('/register',methods=['GET','POST'])
def register():
    info = {}
    if request.method == 'POST':
        print("register")
        print("获取账号")
        account = request.form.get("account")
        print(account)
        print("获取密码")
        password = request.form.get("password")
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