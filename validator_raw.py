from cerberus import Validator

body = {
    "data": {
        "element1": '123',
        "element2": "hello world",
        "element3": "123",
    }
}

body_validator = Validator({
    "data": {
        "type": "dict",
        "schema": {
            "element1": {"type": "float", "required": True, "empty": False},
            "element2": {"type": "string", "required": True, "empty": True},
            "element3": {"type": "string", "required": False, "empty": False},
        }
    }
})

response = body_validator.validate(body)
print(response)
print(body_validator.errors)
