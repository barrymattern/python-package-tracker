from app.shipping_form import Shipping_Form
from flask import (Flask, render_template, redirect)
from app.config import Config
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return 'Package Tracker'


@app.route('/new_package', methods=['GET', 'POST'])
def new_package():
    form = Shipping_Form()
    if (form.validate_on_submit()):
        return redirect('/')
    return render_template('shipping_request.html', form=form)
