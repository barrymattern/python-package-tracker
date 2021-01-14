from flask import Blueprint, render_template
from app.shipping_form import Shipping_Form

bp = Blueprint('main', __name__, url_prefix='')


@bp.route('/')
def packageTracker():
    return 'Package Tracker'

@bp.route('/new_package', methods=['GET', 'POST'])
def newPackage():
    form = Shipping_Form()
    return render_template('shipping_request.html', form=form)
