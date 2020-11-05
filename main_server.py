from flask import Flask, render_template, request, make_response
from flask_sqlalchemy import SQLAlchemy


UPLOAD_FOLDER = "/"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    ip = db.Column(db.String(100), nullable=False)
class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(20), nullable=False)
    item = db.Column(db.String(20), nullable=False)
    type_trade = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    earth = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.String(100), nullable=False)


@app.route('/register', methods=["POST"])
def reg_user():
    data = request.form.to_dict()
    nick = data["nick"]
    password = data["password"]
    ip = request.environ['REMOTE_ADDR']
    user = Users(nick = nick, password = password, ip = ip)
    db.session.add(user)
    db.commit()
    return ("ok", 200)

@app.route('/login', methods=["POST"])
def login():
    data = request.form.to_dict()
    nick = data["nick"]
    password = data["password"]
    user = Users.query.filter_by(nick=nick).first()
    if (user.password == password):
        return ("ok",200)
    else:
        return("bad",200)
@app.route('/create_trade', methods=["POST"])
def create_trade():
    data = request.form.to_dict()
    nick = data["nick"]
    item = data["item"]
    type_trade = data["type_trade"]
    amount = data["amount"]
    price = data["price"]
    earth = data["earth"]
    trade = Trade(nick = nick, item = item, type_trade = type_trade, price = price, earth = earth, amount = amount)
    db.session.add(trade)
    db.session.commit()
    return ("ok", 200)



app.run(host="0.0.0.0", port="5555")