from unittest import TestCase
from unittest.mock import MagicMock

from src.adapters.output import DynamoDBOutputAdapter


class TestDynamoDBOutputAdapter(TestCase):
    adapter: DynamoDBOutputAdapter

    def setUp(self):
        self.adapter = DynamoDBOutputAdapter("posts")

    def test_create(self):
        created_item = {
            "id": "76331198-1b78-11f1-9535-00155da91917",
            "title": "Black magic in Final Fantasy",
            "content": "This post explains the black magic spells in Final Fantasy",
            "category": "Black Magic",
            "tags": ["Final Fantasy", "Black Magic", "Spells"],
            "createdAt": "2026-03-09T05:28:21+00:00",
        }
        self.adapter.table.put_item = MagicMock(return_value={
            "Attributes": created_item
        })
        dto = {
            "title": "Black magic in Final Fantasy",
            "content": "This post explains the black magic spells in Final Fantasy",
            "category": "Black Magic",
            "tags": ["Final Fantasy", "Black Magic", "Spells"],
        }
        result = self.adapter.create(dto)
        self.assertTrue(dto["title"], result["title"])

    def test_find_all(self):
        items = [
            {
                "id": "76331198-1b78-11f1-9535-00155da91917",
                "title": "Black magic in Final Fantasy",
                "content": "This post explains the black magic spells in Final Fantasy",
                "category": "Black Magic",
                "tags": ["Final Fantasy", "Black Magic", "Spells"],
                "createdAt": "2026-03-09T05:28:21+00:00",
            },
            {
                "id": "215c8984-1b7b-11f1-bfe8-00155da91917",
                "title": "White magic in Final Fantasy",
                "content": "This post explains the white magic spells in Final Fantasy",
                "category": "White Magic",
                "tags": ["Final Fantasy", "White Magic", "Spells"],
                "createdAt": "2026-03-09T05:28:21+00:00",
            },
        ]
        self.adapter.table.scan = MagicMock(return_value={
            "Items": items,
        })
        result = self.adapter.find_all()
        self.assertEqual(result, items)

    def test_find_by_id(self):
        item = {
            "id": "76331198-1b78-11f1-9535-00155da91917",
            "title": "Black magic in Final Fantasy",
            "content": "This post explains the black magic spells in Final Fantasy",
            "category": "Black Magic",
            "tags": ["Final Fantasy", "Black Magic", "Spells"],
            "createdAt": "2026-03-09T05:28:21+00:00",
        }
        self.adapter.table.get_item = MagicMock(return_value={
            "Item": item
        })
        result = self.adapter.find_by_id("76331198-1b78-11f1-9535-00155da91917")
        self.assertEqual(result, item)

    def test_update(self):
        item = {
            "id": "76331198-1b78-11f1-9535-00155da91917",
            "title": "Black magic in Final Fantasy",
            "content": "This post explains the black magic spells in Final Fantasy",
            "category": "Black Magic",
            "tags": ["Final Fantasy", "Black Magic", "Spells"],
            "createdAt": "2026-03-09T05:28:21+00:00",
            "updatedAt": "2026-03-09T06:03:41+00:00",
        }
        self.adapter.table.update_item = MagicMock(return_value={
            "Item": item,
        })
        dto = {
            "title": "Black magic in Final Fantasy",
            "content": "This post explains the black magic spells in Final Fantasy",
            "category": "Black Magic",
            "tags": ["Final Fantasy", "Black Magic", "Spells"],
        }
        result = self.adapter.update("76331198-1b78-11f1-9535-00155da91917", dto)
        self.assertEqual(result, item)

    def test_delete(self):
        self.adapter.table.delete_item = MagicMock(return_value={})
        result = self.adapter.delete("76331198-1b78-11f1-9535-00155da91917")
        self.assertEqual(result, None)
