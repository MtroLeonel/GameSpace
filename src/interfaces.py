from abc import ABC, abstractmethod

class IControlador(ABC):
    @abstractmethod
    def obtener_direccion(self) -> tuple[float, float]:
        pass