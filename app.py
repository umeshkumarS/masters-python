from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
import datetime
currentDT = datetime.datetime.now()
from tabledef import *
engine = create_engine('sqlite:///tutorial.db', echo=True)

app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/home', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    
    path = os.getcwd()+"/static/data"
    list_of_files = []
    for filename in os.listdir(path):
        list_of_files.append(filename)
    print(list_of_files)

    file_names=[]
    for f in list_of_files:
        name , ext = f.split('.')
        file_names.append(name)
    print(file_names)
    
    if result:
        session['logged_in'] = True
        print(POST_USERNAME)
#        with open('out.txt', 'a') as f:
#            print(POST_USERNAME,"------>",currentDT.strftime("%Y-%m-%d %I:%M:%S %p"),file=f)
        return render_template('home.html',files=list_of_files,file_names=file_names)
    else:
        flash('wrong password!')
        return home()
    
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
#    app.secret_key = os.urandom(12)
#    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True,host='0.0.0.0', port=4000)
    app.debug = True
