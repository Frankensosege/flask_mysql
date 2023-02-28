import pymysql
from flask import session, render_template, redirect, request, url_for, Blueprint
from .. import mysql
# from flask_mysqldb import MySQL

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/', methods=['GET', 'POST'])
def main():
    error = None

    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']

        print(type(mysql))
        conn = mysql.connection
        cursor = conn.cursor()

        sql = "SELECT id, user_name FROM userS WHERE id = '%s' AND passwd = '%s' " % (id, pw)

        # print(sql)
        # cursor.execute("set names utf8")
        cursor.execute(sql)

        data = cursor.fetchall()
        cursor.close()

        for row in data:
            data = row[0]
            name = row[1]

        if data:
            session['login_id'] = id
            print(url_for('main.home'))
            return redirect(url_for('main.home', name=name))
        else:
            error = 'invalid input data detected !'

    return render_template('main.html', error=error)

    @bp.route('/register.html', methods=['GET', 'POST'])
    def register():
        error = None
        if request.method == 'POST':
            id = request.form['regi_id']
            pw = request.form['regi_pw']

            conn = mysql.connection
            cursor = conn.cursor()

            sql = "INSERT INTO users VALUES ('%s', '%s')" % (id, pw)
            cursor.execute(sql)

            data = cursor.fetchall()

            if not data:
                conn.commit()
                return redirect(url_for('main'))
            else:
                conn.rollback()
                return "Register Failed"

            cursor.close()

        return render_template('register.html', error=error)

    @bp.route('/home.html/<name>', methods=['GET', 'POST'])
    def home(name):
        print('sdddddddddddddddddddddddddddddddddddddddddddddd')
        error = None
        return render_template('home.html', name=name)