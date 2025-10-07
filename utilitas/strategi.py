from abc import ABC, abstractmethod


class StrategiDasar(ABC):
    @abstractmethod
    def mulai_monitoring(self, interval: int):
        pass
