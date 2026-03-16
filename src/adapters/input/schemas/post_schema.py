STORE = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "Post store schema for blogging platform",
    "description": "The root schema comprises the entire JSON document.",
    "examples": [
        {
            "title": "Black magic in Final Fantasy",
            "content": "This post explains the black magic spells in Final Fantasy",
            "category": "Black Magic",
            "tags": ["Final Fantasy", "Black Magic", "Spells"]
        }
    ],
    "required": ["title", "content", "category", "tags"],
    "properties": {
        "title": {
            "$id": "#/properties/title",
            "type": "string",
            "examples": ["Black magic in Final Fantasy"],
            "maxLength": 128
        },
        "content": {
            "$id": "#/properties/content",
            "type": "string",
            "examples": ["This post explains the black magic spells in Final Fantasy"]
        },
        "category": {
            "$id": "#/properties/category",
            "type": "string",
            "examples": ["Black Magic"],
            "maxLength": 64
        },
        "tags": {
            "$id": "#/properties/tags",
            "type": "array",
            "items": {
                "$id": "#/properties/tags/items",
                "type": "string",
                "examples": ["Final Fantasy", "Black Magic", "Spells"],
                "maxLength": 32
            }
        }
    }
}

LIST = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "Post list schema for blogging platform",
    "description": "The root schema comprises the entire JSON document.",
    "examples": [
        {
            "term": "Black"
        }
    ],
    "required": [],
    "properties": {
        "term": {
            "$id": "#/properties/term",
            "type": "string",
            "examples": ["Black"],
            "maxLength": 128
        }
    }
}