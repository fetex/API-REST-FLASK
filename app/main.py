from re import S
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config["SQL_ALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/crea'
CORS(app)

db= SQLAlchemy(app)



@app.route('/')
def index():
    return "prueba"

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')
