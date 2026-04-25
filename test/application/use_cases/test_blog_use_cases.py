from unittest import TestCase
from unittest.mock import MagicMock

from src.domain.dtos import PostDto
from src.application.use_cases import BlogUseCases
from src.adapters.output import DynamoDBOutputAdapter


class TestBlogUseCases(TestCase):
    use_cases: BlogUseCases

    def setUp(self):
        repository_adapter = DynamoDBOutputAdapter("posts_test")
        repository_adapter.create = MagicMock(return_value={
            "id": "76331198-1b78-11f1-9535-00155da91917",
            "title": "Black magic in Final Fantasy",
            "content": "This post explains the black magic spells in Final Fantasy",
            "category": "Black Magic",
            "tags": ["Final Fantasy", "Black Magic", "Spells"],
            "created_at": "2026-03-09T05:28:21+00:00",
            "updated_at": None
        })
        repository_adapter.find_all = MagicMock(return_value=[
            {
                "id": "76331198-1b78-11f1-9535-00155da91917",
                "title": "Black magic in Final Fantasy",
                "content": "This post explains the black magic spells in Final Fantasy",
                "category": "Black Magic",
                "tags": ["Final Fantasy", "Black Magic", "Spells"],
                "created_at": "2026-03-09T05:28:21+00:00",
                "updated_at": None
            },
            {
                "id": "215c8984-1b7b-11f1-bfe8-00155da91917",
                "title": "White magic in Final Fantasy",
                "content": "This post explains the white magic spells in Final Fantasy",
                "category": "White Magic",
                "tags": ["Final Fantasy", "White Magic", "Spells"],
                "created_at": "2026-03-09T05:28:21+00:00",
                "updated_at": None
            },
        ])
        repository_adapter.find_by_id = MagicMock(return_value={
            "id": "76331198-1b78-11f1-9535-00155da91917",
            "title": "Black magic in Final Fantasy",
            "content": "This post explains the black magic spells in Final Fantasy",
            "category": "Black Magic",
            "tags": ["Final Fantasy", "Black Magic", "Spells"],
            "created_at": "2026-03-09T05:28:21+00:00",
            "updated_at": None
        })
        repository_adapter.update = MagicMock(return_value={
            "id": "76331198-1b78-11f1-9535-00155da91917",
            "title": "Black magic in Final Fantasy",
            "content": "This post explains the black magic spells in Final Fantasy",
            "category": "Black Magic",
            "tags": ["Final Fantasy", "Black Magic", "Spells"],
            "created_at": "2026-03-09T05:28:21+00:00",
            "updated_at": "2026-03-09T06:03:41+00:00",
        })
        repository_adapter.delete = MagicMock(return_value={})
        self.use_cases = BlogUseCases(repository_adapter)

    def test_create(self):
        TITLE = "Black magic in Final Fantasy"
        CONTENT = "This post explains the black magic spells in Final Fantasy"
        CATEGORY = "Black Magic"
        TAGS = ["Final Fantasy", "Black Magic", "Spells"]
        dto = PostDto(
            title=TITLE,
            content=CONTENT,
            category=CATEGORY,
            tags=TAGS
        )
        result = self.use_cases.create(dto)
        self.assertTrue(result.id is not None)
        self.assertEqual(result.title, TITLE)
        self.assertEqual(result.content, CONTENT)
        self.assertEqual(result.category, CATEGORY)
        self.assertEqual(result.tags, TAGS)
        self.assertTrue(result.created_at is not None)
        self.assertTrue(result.updated_at is None)

    def test_list_without_term(self):
        term = None
        result = self.use_cases.list(term)
        self.assertTrue(len(result) == 2)
        self.assertEqual(result[0].title, "Black magic in Final Fantasy")
        self.assertEqual(result[1].title, "White magic in Final Fantasy")

    def test_list_with_term(self):
        term = "Black"
        self.use_cases.output_port.find_all = MagicMock(return_value=[
            {
                "id": "76331198-1b78-11f1-9535-00155da91917",
                "title": "Black magic in Final Fantasy",
                "content": "This post explains the black magic spells in Final Fantasy",
                "category": "Black Magic",
                "tags": ["Final Fantasy", "Black Magic", "Spells"],
                "created_at": "2026-03-09T05:28:21+00:00",
                "updated_at": None
            },
        ])
        result = self.use_cases.list(term)
        self.assertTrue(len(result) == 1)
        self.assertEqual(result[0].title, "Black magic in Final Fantasy")

    def test_read(self):
        ID = "76331198-1b78-11f1-9535-00155da91917"
        result = self.use_cases.read(ID)
        self.assertEqual(result.id, ID)

    def test_update(self):
        ID = "76331198-1b78-11f1-9535-00155da91917"
        TITLE = "Black magic in Final Fantasy"
        CONTENT = "This post explains the black magic spells in Final Fantasy"
        CATEGORY = "Black Magic"
        TAGS = ["Final Fantasy", "Black Magic", "Spells"]
        dto = PostDto(
            title=TITLE,
            content=CONTENT,
            category=CATEGORY,
            tags=TAGS
        )
        result = self.use_cases.update(ID, dto)
        self.assertEqual(result.id, ID)
        self.assertEqual(result.title, TITLE)
        self.assertEqual(result.content, CONTENT)
        self.assertEqual(result.category, CATEGORY)
        self.assertEqual(result.tags, TAGS)
        self.assertTrue(result.created_at is not None)
        self.assertTrue(result.updated_at is not None)

    def test_delete(self):
        ID = "76331198-1b78-11f1-9535-00155da91917"
        result = self.use_cases.delete(ID)
        self.assertEqual(result, None)
