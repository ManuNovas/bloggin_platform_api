class PostDto:
    title: str
    content: str
    category: str
    tags: list[str]

    def __init__(self, title: str, content: str, category: str, tags: list[str]):
        self.title = title
        self.content = content
        self.category = category
        self.tags = tags
