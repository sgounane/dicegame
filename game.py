from flask import Flask, render_template, request, redirect, session

app=Flask(__name__)
app.config["SECRET_KEY"]="my secret dfhf key"


@app.route("/")
def index():
    
    return render_template("index.html", username=session.get("username"))


@app.route("/game")
def game():
    if session.get("username"):
        scores=[10,16,25,28]
        return render_template("game.html", username=session.get("username"), scores=scores)
    return render_template("login.html")
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST" :
        session["username"]=request.form["name"]
        session["email"]=request.form["mail"]
        return  redirect("/game")

    elif session.get("username"):
        return  redirect("/game")


    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username")
    session.pop("email")
    return redirect("/")
app.run(debug=True, host="0.0.0.0", port=4444)