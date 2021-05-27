from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/game")
def game():
    return render_template("game.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        return  render_template("game.html")
    return render_template("login.html")


@app.route("/logout")
def logout():
    return render_template("logout.html")
app.run(debug=True, port=4444)