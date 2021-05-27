from flask import Flask, render_template, request, redirect, session

app=Flask(__name__)
app.config["SECRET_KEY"]="my secret key"


@app.route("/")
def index():
    
    return render_template("index.html")


@app.route("/game")
def game():
    if session.get("logedin")==True:
        return render_template("game.html")
    return render_template("login.html")
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST" or session.get("logedin")==True:
        session["logedin"]=True
        return  redirect("/game")


    return render_template("login.html")


@app.route("/logout")
def logout():
    
    session["logedin"]=False
    return render_template("logout.html")
app.run(debug=True, host="0.0.0.0", port=4444)