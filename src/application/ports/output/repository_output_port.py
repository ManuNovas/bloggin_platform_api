from abc import ABC, abstractmethod


class RepositoryOutputPort(ABC):
    @abstractmethod
    def create(self, attributes: dict) -> bool:
        pass

    @abstractmethod
    def find_all(self) -> list[dict]:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> dict | None:
        pass

    @abstractmethod
    def update(self, id: str, attributes: dict) -> bool:
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        pass
