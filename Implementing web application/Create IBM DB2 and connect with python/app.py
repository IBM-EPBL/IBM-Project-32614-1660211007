from flask import Flask, render_template,request,flash,redirect,url_for,session

import ibm_db


app = Flask(__name__)

app.secret_key='a'

connection = ibm_db.connect("DATABASE=bludb ; HOSTNAME=54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud; PORT= 32733; SECURITY=SSL; SSLServerertificate=/Users/pradeep/PycharmProjects/Flask SQLite/certificate.crt; UID=ssr73017; PWD=zQUhCA8HIIVl8nxT;",'','' )


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
 if request.method == 'POST':
     try:
      username = request.form['username']
      mail = request.form['mail']
      contact = request.form['contact']
      password = request.form['password']
      query = "INSERT INTO USERS VALUES(?,?,?,?)"
      stmt = ibm_db.prepare(connection, query)
      ibm_db.bind_param(stmt, 1, username)
      ibm_db.bind_param(stmt, 2, mail)
      ibm_db.bind_param(stmt, 3, contact)
      ibm_db.bind_param(stmt, 4, password)
      ibm_db.execute(stmt)
      flash("Registered  Successfully","success")
     except:
         flash("Error in Insert Operation", "danger")
     finally:
         return redirect(url_for("index"))
         con.close()
 return render_template('register.html')




@app.route('/login', methods=['GET', 'POST'])
def login():
 global userid
 if request.method == "POST":
    username = request.form['username']
    password = request.form['password']
    query = "SELECT * FROM USERS where username=? and password=?"
    stmt = ibm_db.prepare(connection, query)
    ibm_db.bind_param(stmt, 1, username)
    ibm_db.bind_param(stmt, 2, password)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)
    if account:
        session['Loggedin'] = True
        session['id'] = account['USERNAME']
        session['username'] = account['USERNAME']
        return render_template('customer.html')
    else:
        flash("Oops Username and Password Mismatch", "danger")
        return redirect(url_for("index"))



@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)