from abc import ABC, abstractmethod


class GameObject(ABC):
    @abstractmethod
    def say(self) -> str:
        pass
