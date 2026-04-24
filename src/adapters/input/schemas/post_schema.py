POST_PROPERTIES = {
    "title": {
        "type": "string",
        "maxLength": 128
    },
    "content": {
        "type": "string",
    },
    "category": {
        "type": "string",
        "maxLength": 64
    },
    "tags": {
        "type": "array",
        "items": {
            "type": "string",
            "maxLength": 32
        }
    }
}

POST_BODY = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "type": "object",
    "required": ["title", "content", "category", "tags"],
    "properties": POST_PROPERTIES,
}

SINGLE_ITEM = {
    "type": "object",
    "required": ["id"],
    "properties": {
        "id": {
            "type": "string",
        },
    },
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

UPDATE_ITEM = {
    "type": "object",
    "required": ["pathParameters", "body"],
    "properties": {
        "pathParameters": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                },
            },
        },
        "body": {
            "type": "object",
            "properties": POST_PROPERTIES,
        },
    },
}
