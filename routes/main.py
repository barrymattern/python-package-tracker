from flask import Blueprint, render_template


bp = Blueprint('main', __name__, url_prefix='')

@bp.route('/')
def packageTracker():
    return 'Package Tracker'

@bp.route('/new_package', methods=['GET', 'POST'])
def newPackage():
    return render_template('shipping_request.html')
