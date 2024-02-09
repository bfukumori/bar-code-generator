from src.views.http_types.http_response import HttpResponse
from src.errors.error_types.http_unprocessable_entity_error import HttpUnprocessableEntityError


def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        return HttpResponse(
            status_code=error.status_code,
            body={"errors": [{
                "name": error.name,
                "detail": error.message
            }]})
    return HttpResponse(
        status_code=500,
        body={"errors": [{
            "name": "Internal Server Error",
            "detail": str(error)
        }]})
