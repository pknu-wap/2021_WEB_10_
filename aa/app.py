from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

db = pymysql.connect(host=, port=, user=, passwd=, db=, charset='utf8')
cur = db.cursor()

@app.route("/")
def start():
    return render_template('html/main.html')

@app.route("/register_front")
def register_front():
    return render_template('html/register.html')

@app.route("/register_back", methods=['POST'])
def register():
    user_name=request.form['user_name']
    user_yymmdd=request.form['user_yymmdd']
    user_email=request.form['user_email']
    user_id=request.form['user_id']
    user_pw=request.form['user_pw']
    user_chpw=request.form['user_chpw']

    sql_2="SELECT * FROM Join1"
    cur.execute(sql_2)
    rs2=cur.fetchall()
    a=0

    for i in rs2:
        if i[3] == user_id:
            a=1

    if a==1:
        return render_template('html/register.html')

    else:
        if user_pw == user_chpw:
            sql_3="INSERT INTO Join1 (name, yymmdd, id, pw, email) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(sql_3, (user_name, user_yymmdd, user_id, user_pw, user_email))
            db.commit()
        else:
            return render_template('html/register.html')

        return render_template('html/login.html')

    

@app.route("/login_front")
def login_front():
    return render_template('html/login.html')

@app.route("/login_back", methods=['post'])
def login():
    user_id=request.form['user_id']
    user_pw=request.form['user_pw']
    sql="SELECT pw FROM Join1 WHERE id=%s"
    cur.execute(sql, (user_id))
    rs = cur.fetchall()

    if user_pw == rs[0][0]:
        return render_template('html/main.html')
    else:
        return render_template('html/login.html')

if __name__ == "__main__":
    app.debug = True
    app.run()