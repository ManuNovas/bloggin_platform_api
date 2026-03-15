from abc import ABC, abstractmethod

from src.domain.dtos import PostDto
from src.domain.entities import Post


class BlogInputPort(ABC):
    @abstractmethod
    def create(self, dto: PostDto) -> Post:
        pass

    @abstractmethod
    def list(self, term: str | None) -> list[Post]:
        pass

    @abstractmethod
    def read(self, id: str) -> Post | None:
        pass

    @abstractmethod
    def update(self, id: str, dto: PostDto) -> Post | None:
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        pass
