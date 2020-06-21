import os
from werkzeug.exceptions import HTTPException
from flask import Flask, jsonify
from flaskr.database import db

from flask_restful import Api

from flaskr.apis import ALL_API
from flaskr.views import ALL_VIEW


def create_app(test_config=None):
    # 创建flask实例  instance_relative_config 配置文件相对与flaskr 外层，存储信息不上传到版本库
    app = Flask(__name__, instance_relative_config=True)
    # 设置 密钥 与 数据库
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///../instance/data.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=True
    )

    if test_config is None:
        # 将已设置好的配置保存下来
        app.config.from_pyfile('config.py', silent=True)
    else:
        # 调用相应的配置
        app.config.from_mapping(test_config)
    try:
        # 创建相对文件夹
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 数据库初始化
    db.init_app(app)

    # 请求钩子，又称装饰器，还有一个名字，请求的中间件。作用第一次请求之前执行
    @app.before_first_request
    def create_tables():
        # 运行models，以创建不存在的表
        db.create_all()
        from .database.user import Users
        # user = Users(username='123', passwd='123', role='admin')
        # db.session.add(user)
        # db.session.commit()
    #     print(db.session.query(Users).all())
    # view 蓝图 的注册
    for view_obj in ALL_VIEW:
        app.register_blueprint(view_obj)

    # restful api 的注册
    api = Api(app)
    for api_obj in ALL_API:
        api.add_resource(api_obj['apis'], api_obj['endpoint'])

    # 异常处理
    @app.errorhandler(HTTPException)
    def handle_exception(e):
        return jsonify({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
    return app
