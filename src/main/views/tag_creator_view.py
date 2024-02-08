from src.main.views.http_types.http_request import HttpRequest
from src.main.views.http_types.http_response import HttpResponse
from src.main.controllers.tag_creator_controller import TagCreatorController


class TagCreatorView:
    def validate_and_create(self, http_request: HttpRequest):
        tag_creator_controller = TagCreatorController()

        body = http_request.body
        product_code = body['product_code']

        response = tag_creator_controller.create(product_code)

        return HttpResponse(status_code=200, body=response)