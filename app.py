from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'abdullahi'
app.config['MYSQL_PASSWORD'] = 'Hei123'   
app.config['MYSQL_DB'] = 'flaskeDB'              


mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM products')
    products = cur.fetchall()
    cur.close()
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
