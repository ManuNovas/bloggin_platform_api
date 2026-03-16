from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.utilities.validation import validator, SchemaValidationError
from aws_lambda_powertools.logging.logger import Logger
from json import loads, dumps

from .schemas.post_schema import STORE
from src.domain.dtos import PostDto
from src.application.ports.input import BlogInputPort


class BlogInputAdapter:
    input_port: BlogInputPort
    logger: Logger

    def __init__(self, input_port: BlogInputPort):
        self.input_port = input_port
        self.logger = Logger(service="BlogInputAdapter")

    def _generate_response(self, code: int, body) -> dict:
        return {
            "statusCode": code,
            "body": body
        }
    
    def _handle_validation_error(self, exception):
        return self._generate_response(400, exception)
    
    def _handle_error(self, exception):
        self.logger.error("An error ocurred", exception)
        return self._generate_response(500, "Internal Server Error")

    def create(self, event, context: LambdaContext):
        try:
            body = loads(event["body"])
            dto = PostDto(
                title=body["title"],
                content=body["content"],
                category=body["category"],
                tags=body["tags"],
            )
            post = self.input_port.create(dto)
            response = self._generate_response(201, dumps(post.__dict__))
        except SchemaValidationError as e:
            response = self._handle_validation_error(e)
        except Exception as e:
            response = self._handle_error(e)
        return response
