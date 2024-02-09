from unittest.mock import patch
from src.views.http_types.http_response import HttpResponse
from src.views.http_types.http_request import HttpRequest
from src.drivers.barcode_handler import BarcodeHandler
from .tag_creator_view import TagCreatorView


@patch.object(BarcodeHandler, 'create_barcode')
def test_validate_and_create(mock_create_barcode):
    mock_value = '1234567890'
    mock_create_barcode.return_value = mock_value
    mock_http_request = HttpRequest(
        body={'product_code': mock_create_barcode.return_value})
    tag_creator_view = TagCreatorView()
    response = tag_creator_view.validate_and_create(mock_http_request)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body == {'data': {
        "type": "Tag Image",
        "count": 1,
        "path": f'{mock_value}.png'
    }}
