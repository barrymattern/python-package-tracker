from flask import Blueprint, render_template, redirect
from app.shipping_form import Shipping_Form
from app.models import Package, db

bp = Blueprint('main', __name__, url_prefix='')


@bp.route('/')
def packageTracker():
    return '<a href="/new_package">Add Package</a>'

@bp.route('/new_package', methods=['GET', 'POST'])
def newPackage():
    form = Shipping_Form()
    if (form.validate_on_submit()):
        data = form.data
        new_package = Package(sender=data['sender'], recipient=data['recipient'], origin=data['origin'], destination=data['destination'], location=data['origin'])
        db.session.add(new_package)
        db.session.commit()
        return redirect('/')
    return render_template('shipping_request.html', form=form)
