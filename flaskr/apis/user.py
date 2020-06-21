from flask_restful import Resource
from flask import request
from flaskr.database import to_json
from flaskr.database.user import Users


class UserView(Resource):
    def get(self):
        page = request.values.get('page', type=int)
        limit = request.values.get('limit', type=int)
        result = {'code': 0, 'msg': 'ok', 'data': [], 'count': Users.query.count()}
        for v in Users.query.paginate(page, limit, False).items:
            result['data'].append(to_json(v))
        print()
        return result

    def post(self):
        json_data = request.get_json()
        return {'code': 204, 'msg': 'ok', 'data': []}



