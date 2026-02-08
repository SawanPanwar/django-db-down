from django.views.decorators.csrf import csrf_exempt
from django.db.utils import OperationalError
from django.http import JsonResponse
from .ctl.RoleCtl import RoleCtl
from .exception.application_exception import ApplicationException


@csrf_exempt
def action(request, page, action="get", id=0, pageNo=1):
    try:
        methodCall = page + "Ctl()." + action + "(request,{'id':id, 'pageNo':pageNo})"
        response = eval(methodCall)
        return response
    except ApplicationException as e:
        res = {"result": {}, "success": False}
        res["result"]["message"] = e.__str__()
        return JsonResponse(res)
    except OperationalError as e:
        res = {"result": {}, "success": False}
        res["result"]["message"] = "Database service temporarily unavailable"
        return JsonResponse(res, status=503)