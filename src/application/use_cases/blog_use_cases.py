from aws_lambda_powertools import Logger
from datetime import datetime
from uuid import uuid4

from src.domain.dtos import PostDto
from src.domain.entities import Post
from src.application.ports.input import BlogInputPort
from src.application.ports.output import RepositoryOutputPort


class BlogUseCases(BlogInputPort):
    outputPort: RepositoryOutputPort
    logger: Logger

    def __init__(self, outputPort: RepositoryOutputPort):
        self.outputPort = outputPort
        self.logger = Logger(service="BlogUseCases")

    def _from_dict_to_post(self, entity: dict) -> Post:
        return Post(
            id = entity["id"],
            title = entity["title"],
            content = entity["content"],
            category = entity["category"],
            tags = entity["tags"],
            created_at = entity["created_at"],
            updated_at = entity["updated_at"],
        )
    
    def create(self, dto: PostDto) -> Post:
        post = Post(
            id=uuid4(),
            title=dto.title,
            content=dto.content,
            category=dto.category,
            tags=dto.tags,
            created_at=datetime.now().isoformat(),
            updated_at=None
        )
        self.outputPort.create(post.__dict__)
        return post

    def list(self, term: str | None) -> list[Post]:
        entities = self.outputPort.find_all()
        posts = []
        for entity in entities:
            if term is None or term in entity["title"]:
                post = self._from_dict_to_post(entity)
                posts.append(post)
        return posts
    
    def read(self, id: str) -> Post | None:
        entity = self.outputPort.find_by_id(id)
        if entity is None:
            return None
        return self._from_dict_to_post(entity)
    
    def update(self, id: str, dto: PostDto) -> Post | None:
        post = self.read(id)
        if post is None:
            return None
        post.title = dto.title
        post.content = dto.content
        post.category = dto.category
        post.tags = dto.tags
        post.updated_at = datetime.now().isoformat()
        entity = {}
        for key, value in post.__dict__.items():
            if key not in ["id"]:
                entity[key] = value
        self.outputPort.update(id, entity)
        return post
    
    def delete(self, id: str) -> None:
        post = self.read(id)
        if post is not None:
            self.outputPort.delete(id)
            self.logger.info(msg="Deleted post", extra={ post: post.__dict__ })
