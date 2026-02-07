from django.views.decorators.csrf import csrf_exempt
from django.db.utils import OperationalError
from django.http import JsonResponse
from .ctl.RoleCtl import RoleCtl


@csrf_exempt
def action(request, page, action="get", id=0, pageNo=1):
    try:
        methodCall = page + "Ctl()." + action + "(request,{'id':id, 'pageNo':pageNo})"
        response = eval(methodCall)
        return response
    except OperationalError as e:
        res = {"result": {}, "success": False}
        res["result"]["message"] = "Database service temporarily unavailable"
        return JsonResponse(res, status=503)
