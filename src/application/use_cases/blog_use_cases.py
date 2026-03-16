from aws_lambda_powertools import Logger
from datetime import datetime
from uuid import uuid4

from src.domain.dtos import PostDto
from src.domain.entities import Post
from src.application.ports.input import BlogInputPort
from src.application.ports.output import RepositoryOutputPort


class BlogUseCases(BlogInputPort):
    output_port: RepositoryOutputPort
    logger: Logger

    def __init__(self, output_port: RepositoryOutputPort):
        self.output_port = output_port
        self.logger = Logger(service="BlogUseCases")

    @staticmethod
    def _from_dict_to_post(entity: dict) -> Post:
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
            id=str(uuid4()),
            title=dto.title,
            content=dto.content,
            category=dto.category,
            tags=dto.tags,
            created_at=datetime.now().isoformat(),
            updated_at=None
        )
        self.output_port.create(post.__dict__)
        return post

    def list(self, term: str | None) -> list[Post]:
        entities = self.output_port.find_all()
        posts = []
        for entity in entities:
            if term is None or term in entity["title"]:
                post = self._from_dict_to_post(entity)
                posts.append(post)
        return posts

    def read(self, post_id: str) -> Post | None:
        entity = self.output_port.find_by_id(post_id)
        if entity is None:
            return None
        return self._from_dict_to_post(entity)

    def update(self, post_id: str, dto: PostDto) -> Post | None:
        post = self.read(post_id)
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
        self.output_port.update(post_id, entity)
        return post

    def delete(self, post_id: str) -> None:
        post = self.read(post_id)
        if post is not None:
            self.output_port.delete(post_id)
            self.logger.info(post.__dict__)
