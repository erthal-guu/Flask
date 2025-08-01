from flask import Flask, render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors  # 👈 isso é necessário para usar DictCursor

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'meu_banco'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
    cur.execute("SELECT * FROM produtos")
    produtos = cur.fetchall()
    cur.close()
    return render_template('index.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)
