from src.errors.error_types.http_unprocessable_entity_error import HttpUnprocessableEntityError
from .error_handler import handle_errors


def test_handle_errors_http_unprocessable_entity():
    mock_error = HttpUnprocessableEntityError("field required")
    response = handle_errors(mock_error)

    assert response.status_code == 422
    assert response.body == {"errors": [{
        "name": "Unprocessable Entity",
        "detail": "field required"
    }]}


def test_handle_errors_http_server_error():
    mock_error = Exception("server error")
    response = handle_errors(mock_error)

    assert response.status_code == 500
    assert response.body == {"errors": [{
        "name": "Internal Server Error",
        "detail": "server error"
    }]}
