from os import getenv

from src.adapters.output import DynamoDBOutputAdapter
from src.application.use_cases import BlogUseCases
from src.adapters.input import BlogInputAdapter


def run(event, context) -> dict:
    table_name = getenv("POSTS_TABLE_NAME")
    repository_adapter = DynamoDBOutputAdapter(table_name)
    use_cases = BlogUseCases(repository_adapter)
    input_adapter = BlogInputAdapter(use_cases)
    return input_adapter.create(event)
