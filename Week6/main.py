from flask import Flask, render_template, redirect, url_for, request, session
import mysql.connector
import os
from dotenv import load_dotenv

# 載入.env文件中的環境變數
load_dotenv()
# 從環境變數中讀取資料庫配置
db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_DATABASE"),
}

connection = mysql.connector.connect(**db_config)
# 建立游標
print("ready to print,用來確認有無成功資料庫")
cursor = connection.cursor()
cursor.execute("USE website")
cursor.execute("SHOW TABLES")
# 取得查詢結果
tables = cursor.fetchall()
for table in tables:
    print(table[0])

app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key"  # 設定一個隨機的密鑰，用於加密 session

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/signup", methods=["POST"])
def signup():
    name = request.form.get("fullname")
    username = request.form.get("username")
    password = request.form.get("password")
    if not name or not username or not password:
        return redirect(url_for("error", message="請填寫完整資訊"))
    query = "SELECT * FROM member WHERE username=%s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    if result:
        return redirect(url_for("error", message="帳號已經被註冊"))
    query = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, username, password))
    connection.commit()
    return render_template("home.html")
@app.route("/signin", methods=["POST"])
def signin():
    # 驗證
    username = request.form.get("username")
    password = request.form.get("password")
    if not username or not password:
        return redirect(url_for("error", message="請填寫帳號和密碼"))
    query = "SELECT * FROM member WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    if result:
        session["username" ]= username#把帳號用session存起來
        return redirect(url_for("member"))
    else:
        return redirect(url_for("error", message="帳號或密碼輸入錯誤"))


@app.route("/member")
def member():
    if "username" in session:
        username = session["username"]
        query_name = "SELECT name FROM member WHERE username = %s"
        cursor.execute(query_name, (username,))
        user_name = cursor.fetchone()[0]
        # username = session["username"]#把帳號拉出來放在變數中導入首頁
        query = "SELECT member.name, message.content FROM message JOIN member ON message.member_id = member.id ORDER BY message.time DESC"
        cursor.execute(query)
        messages = cursor.fetchall()
        for i in messages:
            print("message",i)
        return render_template("member.html", messages=messages, name=user_name)
    return redirect(url_for('home'))
@app.route("/createMessage", methods=["POST"])
def create_message():
    if "username" in session:
        username = session["username"]
        content = request.form.get("comment")
        
        if content:
            query = "SELECT id FROM member WHERE username = %s"
            cursor.execute(query, (username,))
            member_id = cursor.fetchone()[0]
        
            insert_query = "INSERT INTO message (member_id, content) VALUES (%s, %s)"
            cursor.execute(insert_query, (member_id, content))
            connection.commit()

            return redirect(url_for("member"))
        else:
            return redirect(url_for("error", message="請輸入留言"))
    else:
        return redirect("/")
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

cursor.close()
connection.close()





