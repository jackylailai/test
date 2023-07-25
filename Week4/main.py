from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key"  # 設定一個隨機的密鑰，用於加密 session

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signin", methods=["POST"])
def signin():
    # 驗證
    username = request.form.get("username")
    password = request.form.get("password")
    agree = request.form.get("agree")

    if not username or not password:
        return redirect(url_for("error", message="Please enter username and password"))

    if username == "test" and password == "test" and agree:
        session["username" ]= username#把名字存起來
        return redirect(url_for("member"))
    else:
        return redirect(url_for("error", message="Username or password is not correct"))


@app.route("/member")
def member():
    if "username" in session:
        username = session["username"]#把名字拉出來放在變數中導入首頁
        return render_template("member.html", username=username)
    
    return redirect(url_for('home'))

@app.route("/error")
def error():
    error_message = request.args.get("message")
    return render_template("error.html", error_message=error_message)

@app.route("/signout")
def signout():
    del session["username"]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True,port=3000)
