from json import dumps
from unittest import TestCase
from unittest.mock import MagicMock

from domain.entities import Post
from src.adapters.output import DynamoDBOutputAdapter
from src.application.use_cases import BlogUseCases
from src.adapters.input import BlogInputAdapter


class TestInputAdapter(TestCase):
    adapter: BlogInputAdapter

    def setUp(self):
        output_adapter = DynamoDBOutputAdapter("posts")
        use_cases = BlogUseCases(output_adapter)
        use_cases.create = MagicMock(return_value=Post(
            id="d7ab9666-2108-11f1-b3b8-00155d366223",
            title="Black magic in Final Fantasy",
            content="What is Black magic in Final Fantasy?",
            category="Black Magic",
            tags=["Final Fantasy", "Black Magic"],
            created_at="2026-03-16 00:00:00",
            updated_at=None
        ))
        self.adapter = BlogInputAdapter(use_cases)

    def test_create(self):
        result = self.adapter.create({
            "body": dumps({
                "title": "Black magic in Final Fantasy",
                "content": "What is Black magic in Final Fantasy?",
                "category": "Black Magic",
                "tags": ["Final Fantasy", "Black Magic"],
            })
        })
        self.assertEqual(result, {
            "statusCode": 201,
            "body": dumps({
                "id": "d7ab9666-2108-11f1-b3b8-00155d366223",
                "title": "Black magic in Final Fantasy",
                "content": "What is Black magic in Final Fantasy?",
                "category": "Black Magic",
                "tags": ["Final Fantasy", "Black Magic"],
                "created_at": "2026-03-16 00:00:00",
                "updated_at": None
            })
        })
