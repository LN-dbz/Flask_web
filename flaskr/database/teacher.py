from datetime import datetime
from flaskr.database import db


class Teacher(db.Model):
    """定义数据模型"""
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    account_name = db.Column(db.String(50), unique=True)
    # 如何二选一
    sex = db.Column(db.String(10))
    nation = db.Column(db.String(10))
    birth_date = db.Column(db.String(20))
    check_in = db.Column(db.String(20))
    age = db.Column(db.Integer)
    working_years = db.Column(db.Integer)
    address = db.Column(db.String(80))
    email = db.Column(db.String(50))
    f_phone = db.Column(db.String(50))
    m_phone = db.Column(db.String(50))
    education = db.Column(db.String(50))
    graduation = db.Column(db.String(50))

    status = db.Column(db.Integer, default=0)
    add_date = db.Column(db.String(50), default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


