from unittest import TestCase
from unittest.mock import MagicMock

from src.adapters.output import DynamoDBOutputAdapter
from src.application.use_cases import BlogUseCases
from src.adapters.input import BlogInputAdapter


class TestInputAdapter(TestCase):
    adapter: BlogInputAdapter

    def setUp(self):
        output_adapter = DynamoDBOutputAdapter("posts")
        use_cases = BlogUseCases(output_adapter)
        self.adapter = BlogInputAdapter(use_cases)
