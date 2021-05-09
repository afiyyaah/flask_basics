from dataclasses import dataclass
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@db/main"
CORS(app)

db = SQLAlchemy(app)
@dataclass
class User(db.Model):
    id: int 
    first_name: str
    last_name: str
    email: str
    mobile: str

    id = db.Column(db.Integer, primary_key= True, autoincrement = False)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    mobile = db.Column(db.String(100))

@app.route('/api/users')
def index():
    return jsonify(User.query.all())

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')