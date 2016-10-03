from flask import Flask, request, render_template
import hashlib, csv

app = Flask(__name__)

@app.route("/")
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
        key = row[0]
        val = row[1]
        d[key] = val
    return d
        
    
def check(username, password):
    r = csv.reader(open("data/usr.csv","r"))
    d = csvToDict(r)
    if username in d:
        if d[username] == password:
            return "you did it. im so proud"
        else:
            return "wrong pw. good try"
    else:
        return "username not found. wyd? #take3sectoregister"
    
@app.route("/register/", methods=["POST"])
def register():
    return "0"
    
if __name__ == '__main__':
    app.debug = True
    app.run()
  
