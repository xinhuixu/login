from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def login():
    print request_header
    return render_template('login.html')

@app.route("/auth/", methods=["POST"])
def authenticate():    
    username = "mangosteen"
    password = "durian"
    if request.method == "POST":
        if request.form["username"]== username and request.form["password"] == password:
            return "ok"
        return "are you sure about this??"
    else:
        return "no......"
        
if __name__ == '__app__':
    app.run(debug = True)
