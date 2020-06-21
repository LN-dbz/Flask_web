from functools import wraps

from flaskr.database import db, to_json

class Users(db.Model):
    """定义数据模型"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    passwd = db.Column(db.String(80), unique=True)
    role = db.Column(db.String(120), unique=True, default='tourist')

    @classmethod
    def find_by_name(cls, username):
        return cls.query.filter_by(username=username).first()


from flask import session, abort, redirect
from flaskr.database.role_authority import role_list
# 权限认证装饰器
def authority_verification(auth):
    """
    权限认证装饰器
    :param permission:
    :return:
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'name' not in session:
                return redirect('/login')
            try:
                # 获得用户角色
                user_role = to_json(Users.find_by_name(session['name']))['role']
                user_role_list = role_list[user_role]
                if auth not in user_role_list and user_role != 'admin':
                    abort(403)
                return f(*args, **kwargs)
            except:
                abort(403)
        return decorated_function
    return decorator