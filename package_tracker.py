from app.shipping_form import Shipping_Form
from flask import (Flask, render_template, redirect)
from app.config import Config
from flask_migrate import Migrate
from app.models import Package, db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    form = Shipping_Form()
    packages = Package.query.all()
    # package = {
    #     'package_id': packages[0].id,
    #     'package_sender': packages[0].sender
    # }
    return render_template('package_status.html', form=form, packages=packages)


@app.route('/new_package', methods=['GET', 'POST'])
def new_package():
    form = Shipping_Form()
    if (form.validate_on_submit()):
        data = form.data
        new_package = Package(sender=data["sender"],
                              recipient=data['recipient'],
                              origin=data['origin'],
                              destination=data['destination'],
                              location=data['origin'])
        db.session.add(new_package)
        db.session.commit()
        Package.advance_all_locations()
        return redirect('/')
    return render_template('shipping_request.html', form=form)
