from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def to_json(inst):
    return {c.name: getattr(inst, c.name) for c in inst.__table__.columns}
