from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def login():    
    return render_template('login.html')

@app.route("/auth/", methods=["POST"])
def authenticate():    
    username = "mangosteen"
    password = "durian"
    if request.method == "POST":
        if request.form["username"]== username and request.form["password"] == password:
            return render_template('auth.html',res="succ")
        return render_template('auth.html',res="fail")
    else:
        return "no......"
        
if __name__ == '__main__':
    app.debug = True
    app.run()
  
