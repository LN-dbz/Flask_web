from flask_restful import Resource
from flask import request
from flaskr.database import to_json, db
from flaskr.database.teacher import Teacher


class TeacherApi(Resource):
    def get(self):
        page = request.values.get('page', type=int)
        limit = request.values.get('limit', type=int)
        status = request.values.get('status', 0, int)
        field = request.values.get('field', 'add_date')
        order = request.values.get('order', 'desc')
        # if not field:
        #     field = 'add_date'
        # if not field:
        #     field = 'desc'
        print(field, order)
        if order == 'desc':
            order_by_field = getattr(Teacher, field).desc()
        else:

            order_by_field = getattr(Teacher, field).asc()
        result = {'code': 0, 'msg': 'ok', 'data': [], 'count': Teacher.query.filter(Teacher.status == status).count()}
        for v in Teacher.query.filter(Teacher.status == status).order_by(order_by_field).paginate(page, limit, False).items:
            result['data'].append(to_json(v))
        return result

    def post(self):
        teacher = {
            'name': request.values.get('name'),
            'sex': request.values.get('sex'),
            'nation': request.values.get('nation'),
            'birth_date': request.values.get('birth_date'),
            'check_in': request.values.get('check_in'),
            'age': request.values.get('age', type=int),
            'working_years': request.values.get('working_years', type=int),
            'address': request.values.get('address'),
            'email': request.values.get('email'),
            'f_phone': request.values.get('f_phone'),
            'm_phone': request.values.get('m_phone'),
            'education': request.values.get('education'),
            'graduation': request.values.get('graduation')
        }
        teacher_id = request.values.getlist('teacher_id[]')
        del_type = request.values.get('del_type', '')
        if teacher_id:
            teacher_id = [int(__v) for __v in teacher_id]
            if del_type:
                status = request.values.get('status', 0, int)
                for __v in teacher_id:
                    Teacher.query.filter(Teacher.id == int(__v)).update({'status': status})
            else:
                del teacher['name']
                for __v in teacher_id:
                    Teacher.query.filter(Teacher.id == int(__v)).update(teacher)
        else:
            teacher = Teacher(**teacher)
            # 修改
            db.session.add(teacher)
        result = {'code': 0, 'msg': 'ok'}
        try:
            db.session.commit()
        except Exception as e:
            if 'UNIQUE' in str(e):
                result = {'code': -1, 'msg': '姓名重复！'}
            else:
                result = {'code': -1, 'msg': str(e)}
        return result
