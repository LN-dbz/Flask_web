from flaskr.apis.user import UserView
from flaskr.apis.teacher import TeacherApi

ALL_API = [
    {'apis': UserView, 'endpoint': '/api/user'},
    {'apis': TeacherApi, 'endpoint': '/api/teacher'}
]