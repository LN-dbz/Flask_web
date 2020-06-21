from flask import Blueprint, render_template, session, request, redirect
from flaskr.database.user import authority_verification, Users
user_view = Blueprint('user_view', __name__, url_prefix='/user')


@user_view.route('/', methods=['GET'])
@authority_verification('admin')
def one():
    return render_template('user/user.html')
