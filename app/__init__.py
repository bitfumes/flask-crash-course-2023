from flask_sqlalchemy import SQLAlchemy

from app.blueprints import user, web
from flask import Flask

db = SQLAlchemy()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)
app.register_blueprint(web.bp)
app.register_blueprint(user.bp)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)


with app.app_context():
    db.create_all()
