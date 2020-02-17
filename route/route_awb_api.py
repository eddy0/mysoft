from flask import (
    Blueprint,
    request,
    redirect,
    jsonify)

from models.awb import AWB
from route.helper import login_required
from utils import log

main = Blueprint('route_awb_api', __name__)


@main.route('/add', methods=['POST'])
@login_required
def add_awb():
    data = request.get_json()
    t = AWB.add(data)
    return jsonify(data=t, errcode=0)


@main.route('/<id>', methods=['PUT'])
@login_required
def toggle_awb(id):
    t = AWB.toggle(id)
    return jsonify(data=t, errcode=0)


@main.route('/<id>', methods=['PATCH'])
@login_required
def update_awb(id):
    form = request.get_json()
    t = AWB.update(id, **form)
    return jsonify(data=t, errcode=0)


@main.route('/<id>', methods=['DELETE'])
@login_required
def delete_awb(id):
    log('delete')
    t = AWB.delete(id)
    return jsonify(data=t, errcode=0)


@main.route('/')
@login_required
def awb_index():
    awbs = AWB.all()
    return jsonify(data=awbs, errcode=0)


@main.route('/all')
@login_required
def awb_all():
    return redirect('/')


@main.route('/complete')
@login_required
def awb_complete():
    awbs = AWB.all(complete=True)
    return jsonify(data=awbs, errcode=0)


@main.route('/uncomplete')
@login_required
def awb_uncomplete():
    awbs = AWB.all(complete=False)
    return jsonify(data=awbs)

