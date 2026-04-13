from os import getenv

from src.adapters.output import DynamoDBOutputAdapter
from src.application.use_cases import BlogUseCases
from src.adapters.input import BlogInputAdapter

table_name = getenv("POSTS_TABLE_NAME", "")
repository_adapter = DynamoDBOutputAdapter(table_name)
use_cases = BlogUseCases(repository_adapter)
input_adapter = BlogInputAdapter(use_cases)

def create(event, context):
    return input_adapter.create(event)

def get_all(event, context):
    return input_adapter.get_all(event)


def get_one(event, context):
    return input_adapter.get_one(event)
