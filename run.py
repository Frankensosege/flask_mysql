from flask import current_app
from flask_mysqldb import MySQL

db = MySQL()
if __name__ == '__main__':
    app = current_app()
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'host'
    app.config['MYSQL_PASSWORD'] = '1q2w3e4r!'
    app.config['MYSQL_DB'] = 'python_sample'
    app.secret_key = 'ABCDEF'

    db.init_app(app)
    current_app.run(debug=True, host='localhost', port=5000)