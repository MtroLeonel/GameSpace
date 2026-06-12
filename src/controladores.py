import pygame
from interfaces import IControlador

class ControlTecladoPygame(IControlador):
    def obtener_direccion(self) -> tuple[float, float]:
        teclas = pygame.key.get_pressed()
        dir_x = 0
        if teclas[pygame.K_LEFT]: dir_x = -1
        if teclas[pygame.K_RIGHT]: dir_x = 1
        return (dir_x, 0)

class ControlIAEnemigo(IControlador):
    def obtener_direccion(self) -> tuple[float, float]:
        return (0, 1) # Siempre avanza hacia abajo