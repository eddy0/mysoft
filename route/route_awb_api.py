from flask import (
    Blueprint,
    request,
    redirect,
    jsonify)

from models.awb import AWB
from route.helper import login_required
from utils import log

main = Blueprint('route_awb_api', __name__)

@login_required
@main.route('/add', methods=['POST'])
def add_awb():
    data = request.get_json()
    t = AWB.add(data)
    return jsonify(t)


@main.route('/<id>', methods=['PUT'])
def toggle_awb(id):
    t = AWB.toggle(id)
    return jsonify(t)


@main.route('/<id>', methods=['PATCH'])
def update_awb(id):
    form = request.get_json()
    t = AWB.update(id, **form)
    return jsonify(t)


@main.route('/<id>', methods=['DELETE'])
def delete_awb(id):
    t = AWB.delete(id)
    return jsonify(t)


@login_required
@main.route('/')
def awb_index():
    awbs = AWB.all()
    return jsonify(awbs)


@main.route('/all')
def awb_all():
    return redirect('/')


@main.route('/complete')
def awb_complete():
    awbs = AWB.all(complete=True)
    return jsonify(awbs)


@main.route('/uncomplete')
def awb_uncomplete():
    awbs = AWB.all(complete=False)
    return jsonify(awbs)

