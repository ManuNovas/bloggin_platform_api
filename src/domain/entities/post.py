class Post:
    id: str
    title: str
    content: str
    category: str
    tags: list[str]
    created_at: str
    update_at: str | None

    def __init__(self, id: str, title: str, content: str, category: str, tags: list[str], created_at: str, updated_at: str | None):
        self.id = id
        self.title = title
        self.content = content
        self.category = category
        self.tags = tags
        self.created_at = created_at
        self.update_at = updated_at

