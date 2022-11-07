import json
from werkzeug.wrappers import Response


def custom_response(message=None, data={}, status_code=200, error=False):
    response = Response()
    response.mimetype = 'application/json'
    response.charset = 'utf-8'
    response.status_code = status_code
    status = "error" if error else "success"
    response.data = json.dumps(
        {"message": message, "status": status, "data": data}, default=str)
    return response
