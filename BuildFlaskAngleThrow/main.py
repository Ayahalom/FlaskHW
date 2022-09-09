from flask import Flask, request, redirect, url_for, render_template
from physicsCalculations import calcThrowData

app = Flask(__name__)


@app.route("/")
def strangerFunction():
    return "<h1>hello stranger</h1>"


@app.route("/personal/<userName>")
def amitFunction(userName):
    return f"<h1>hello {userName}</h1>"


@app.route("/throw/", methods=["GET", "POST"])
def calcThrow():
    if request.method == "POST":
        horizontalVel = float(request.form['horizontalVel'])
        verticalVel = float(request.form['verticalVel'])
        data = calcThrowData(horizontalVel, verticalVel)
        return f"dist is {data['distance']} [m]"
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
