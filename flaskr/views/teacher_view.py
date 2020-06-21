from flask import Blueprint, render_template, session, request, redirect
from flaskr.database.user import authority_verification, Users
teacher_view = Blueprint('teacher_view', __name__, url_prefix='/teacher')


@teacher_view.route('/', methods=['GET'])
@authority_verification('admin')
def one():
    return render_template('teacher/teacher.html')
