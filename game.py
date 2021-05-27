from flask import Flask, render_template, request, redirect

app=Flask(__name__)

global logedin
logedin=False

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/game")
def game():
    global logedin
    if logedin==True:
        return render_template("game.html")
    return render_template("login.html")
@app.route("/login", methods=["POST","GET"])
def login():
    global logedin
    if request.method=="POST" or logedin==True:
        logedin=True
        return  redirect("/game")


    return render_template("login.html")


@app.route("/logout")
def logout():
    global logedin
    logedin=False
    return render_template("logout.html")
app.run(debug=True, host="0.0.0.0", port=4444)