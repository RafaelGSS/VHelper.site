from flask import jsonify, Response, request, Blueprint, render_template, redirect, url_for


bp = Blueprint('web',  __name__)


@bp.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@bp.route('/contato', methods=['GET'])
def contato():
	return render_template('contato.html')
