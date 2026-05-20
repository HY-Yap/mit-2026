from flask import Flask, render_template, request
from planner import *

app = Flask(__name__) sigma boy

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
