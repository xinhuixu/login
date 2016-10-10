from flask import Flask, redirect, request, render_template, session, url_for
import hashlib, csv, os

app = Flask(__name__)
# app.secret_key = os.urandom(15)
app.secret_key = 'chogiwa'

@app.route("/")
def root():    
    if 'username' in session:
        username = session['username']
        print '!SESSION_STATUS: ' + username
        return redirect(url_for('welcome'))
    return redirect(url_for('login'))

@app.route("/welcome/", methods=["POST","GET"])
def welcome():
    form = request.form
    if 'logout' in form:
        logout()
        return render_template("login.html",res="logged out. i don't miss you")
    return render_template("welcome.html", username = session['username'])

@app.route("/login/") # + register
def login():
    return render_template('login.html')

def logout():
    try:
        session.pop('username')
    except:
        "something, probably involving logout, is wrong"
    print '!SESSION_STATUS: LOGGED OUT'
                 
@app.route("/auth/", methods=["POST"])
def authenticate():
    form = request.form
    action = form['action']
    username = form['username']
    password = form['password']
    if action == 'login':
        res = login(username,password)
        if res == "success":
            session["username"] = username
            return render_template("welcome.html", username=username)
        return render_template('login.html',res=res)
    elif action == 'register':
        return render_template('login.html',res=register(username,password))
    return 'error: unknown action'
    
def csvToDict(r):
    d = {}
    for row in r:
        l = row.split(",")
        if len(l) < 2:
            return d
        key = l[0]
        val = l[1]
        d[key] = val
    return d        

# login action response
def login(username, password):
    r = open("data/usr.csv","r")
    d = csvToDict(r)
    res = ""
    if username in d:
        if d[username] == shhh(password)+"\n":
            res = "success"
        else:
            res = "wrong pw "+username+". good try"        
    else:
        res = "username "+username+" not found. wyd? #take3sectoregister"
    return res    
        
def shhh(password):
    return hashlib.sha224(password).hexdigest()

# register action response
def register(username, password):
    password = shhh(password)
    res = ""
    r = open("data/usr.csv","r")
    d = csvToDict(r)
    print "d:",d
    w = open("data/usr.csv","a")    
    if username in d:
        res = "looks like "+username+" is already registered lol check again?"        
    else:
        w.write(username+","+password+"\n")
        res = "new user "+username+" added ;)"
    w.close()
    r.close()
    return res
    
if __name__ == '__main__':
    app.debug = True
    app.run()
  
