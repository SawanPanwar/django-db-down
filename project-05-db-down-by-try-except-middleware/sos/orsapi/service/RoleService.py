from ..models import Role
from ..utility.DataValidator import DataValidator
from ..exception.application_exception import ApplicationException
from .BaseService import BaseService
from django.db import connection


class RoleService(BaseService):

    def search(self, params):
        try:
            pageNo = (params['pageNo'] - 1) * self.pageSize
            sql = 'select * from sos_role where 1=1'
            val = params.get('name', None)
            if (DataValidator.isNotNull(val)):
                sql += " and name like '" + val + "%%'"
            sql += " limit %s, %s"
            cursor = connection.cursor()
            cursor.execute(sql, [pageNo, self.pageSize])
            result = cursor.fetchall()
            columnName = ('id', 'name', 'description')
            res = {
                "data": [],
            }
            params["index"] = ((params['pageNo'] - 1) * self.pageSize)
            for x in result:
                print({columnName[i]: x[i] for i, _ in enumerate(x)})
                params['maxId'] = x[0]
                res['data'].append({columnName[i]: x[i] for i, _ in enumerate(x)})
            return res
        except Exception as e:
            raise ApplicationException("Unexpected error occurred while searching object")

    def get_model(self):
        return Role
