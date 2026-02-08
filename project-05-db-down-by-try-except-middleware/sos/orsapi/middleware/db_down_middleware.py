from django.db.utils import OperationalError
from django.http import JsonResponse


class DatabaseDownMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        if isinstance(exception, OperationalError):
            res = {"result": {}, "success": False}
            res["result"]["message"] = "Database service temporarily unavailable"
            return JsonResponse(res, status=503)
        return None
