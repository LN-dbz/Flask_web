from functools import wraps
from flask import session, abort, redirect


def authority_verification(auth):
    """
    权限认证装饰器
    :param permission:
    :return:
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                print(session)
                print(*args, **kwargs)
                print(auth)
                # 获得用户角色
                # 判断 auth 是否在该角色内
                return f(*args, **kwargs)
            except:
                abort(403)
        return decorated_function
    return decorator

