from aws_lambda_powertools.logging.logger import Logger
from aws_lambda_powertools.utilities.validation import validate, SchemaValidationError
from json import loads, dumps

from src.adapters.input.schemas.post_schema import POST_BODY, GET_ITEM
from src.domain.dtos import PostDto
from src.application.ports.input import BlogInputPort


class BlogInputAdapter:
    input_port: BlogInputPort
    logger: Logger

    def __init__(self, input_port: BlogInputPort):
        self.input_port = input_port
        self.logger = Logger(service="BlogInputAdapter")

    @staticmethod
    def _generate_response(code: int, body) -> dict:
        return {
            "statusCode": code,
            "body": dumps(body)
        }
    
    def _handle_error(self, exception):
        self.logger.error(exception)
        return self._generate_response(500, "Internal Server Error")

    def create(self, event):
        try:
            body = loads(event["body"])
            validate(body, POST_BODY)
            dto = PostDto(
                title=body["title"],
                content=body["content"],
                category=body["category"],
                tags=body["tags"],
            )
            post = self.input_port.create(dto)
            response = self._generate_response(201, post.__dict__)
        except SchemaValidationError as e:
            response = self._generate_response(400, e.validation_message)
        except Exception as e:
            response = self._handle_error(e)
        return response
    
    def get_all(self, event):
        posts = self.input_port.list(None)
        body = []
        for post in posts:
            body.append(post.__dict__)
        return self._generate_response(200, body)

    def get_one(self, event):
        try:
            path_parameters = loads(event["pathParameters"])
            validate(path_parameters, GET_ITEM)
            post = self.input_port.read(path_parameters["id"])
            response = self._generate_response(200, post.__dict__)
        except SchemaValidationError as e:
            response = self._generate_response(400, e.validation_message)
        except Exception as e:
            response = self._handle_error(e)
        return response
