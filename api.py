from flask import Flask, jsonify
from flaskext.mysql import MySQL


app = Flask(__name__)


app.config['MYQSL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'andibasic'
app.config['MYSQL_DATABASE_DB'] = 'projekt'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'


mysql = MySQL(app)

mysql.init_app(app)


@app.route('/')
def home(): 
    #return render_template("index.html", token="Hello Flask+React")
    return jsonify({'poruka' : 'Dobrodosli na pocetnu stranicu'})



if __name__ == '__main__':
    app.run(debug=True)