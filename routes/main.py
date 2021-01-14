from flask import Blueprint, render_template
from app import shipping_form

bp = Blueprint('main', __name__, url_prefix='')


@bp.route('/')
def index():
    return 'Package Tracker'


@bp.route('/new_package', methods=['GET'. 'POST'])
def new_package():
    form = Shipping_Form()
    return render_template('shipping_request.html', form=form)
