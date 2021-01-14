from flask import Flask, render_template
from config import Config
from routes import main
from flask_migrate import Migrate
from app.models import db


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(main.bp)
db.init_app(app)
migrate = Migrate(app, db)
