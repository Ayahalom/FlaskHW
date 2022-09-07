from flask import Flask, request
from physicsCalculations import calcThrowData

app = Flask(__name__)


@app.route("/")
def strangerFunction():
    return "<h1>hello stranger</h1>"


@app.route("/amit/")
def amitFunction():
    return "oh, it's Amit the melech"


@app.route("/throw/", methods=["GET", "POST"])
def calcThrow():
    if request.method == "POST":
        data = calcThrowData(10, 20)
        return f"dist is {data['distance']} [m]"
    else:
        data = calcThrowData(10, 30)
        return f"dist is {data['distance']} [m]"
