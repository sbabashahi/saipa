import time
import json

from django.http import HttpResponse


class BaseResponse:
    def send(self):
        status = self.__dict__.pop('status')
        return HttpResponse(
            json.dumps(self.__dict__),
            status=status,
            content_type="application/json"
        )


class ErrorResponse(BaseResponse):
    def __init__(self, message, dev_error=None, errors=None, status=400):
        self.message = message
        self.dev_error = dev_error
        self.errors = errors
        self.current_time = round(time.time())
        self.success = False
        self.status = status


class SuccessResponse(BaseResponse):
    def __init__(self, data=None, message=None, status=200, **kwargs):
        self.data = data
        self.message = message
        self.current_time = round(time.time())
        self.success = True
        self.index = kwargs['index'] if kwargs.get('index') is not None else None
        self.total = kwargs['total'] if kwargs.get('total') is not None else None
        self.status = status
