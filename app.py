from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def login():
    print request_header
    return render_template('login.html')

@app.route("/auth")
def authenticate():
    print
