from flask import Blueprint, render_template, session, request, redirect
from flaskr.database.user import authority_verification, Users
test = Blueprint('test', __name__, url_prefix='/')


@test.route('/', methods=['POST', 'GET'])
@authority_verification('')
def one():
    return render_template('index.html')


@test.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.values.get('username')
        passwd = request.values.get('passwd')
        user = Users.query.filter_by(username=username, passwd=passwd).first()
        if user:
            session['name'] = username
            return redirect('/')
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')


@test.route('/sign_out')
def sign_out():
    session.clear()
    return redirect('/login')


