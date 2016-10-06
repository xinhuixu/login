from flask import Flask, request, render_template, session
import hashlib, csv, os

app = Flask(__name__)
app.secret_key = os.urandom(15)

@app.route("/login/")
def login():    
    return render_template('login.html')

@app.route("/auth/", methods=["POST"])
def authenticate():
    form = request.form
    if request.method == "POST":
        return render_template('auth.html',res=check(form["username"],form["password"]))
    else:
        return "wyd??"

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
        
    
def check(username, password):
    r = open("data/usr.csv","r")
    d = csvToDict(r)
    print d
    if username in d:
        print shhh(password)
        if d[username] == shhh(password)+"\n":
            return "you did it "+username+". im so proud"
        return "wrong pw "+username+". good try"
    else:
        return "username "+username+" not found. wyd? #take3sectoregister"

def shhh(password):
    return hashlib.sha224(password).hexdigest()

@app.route("/register/", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    
    password = shhh(password)

    r = open("data/usr.csv","r")
    d = csvToDict(r)
    w = open("data/usr.csv","a")
    
    if username in d:
        return "looks like "+username+" aint no new fella in town!"        
    else:
        w.write(username+","+password+"\n")
        return "got it "+username+" ;)"
    w.close()
    r.close()
    
    
if __name__ == '__main__':
    app.debug = True
    app.run()
  
