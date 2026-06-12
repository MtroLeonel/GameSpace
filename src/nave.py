import pygame
from interfaces import IControlador


class NaveEspacial:
    def __init__(
        self,
        ruta_imagen: str,
        x: float,
        y: float,
        velocidad: float,
        controlador: IControlador,
        angulo_inicial: float = 0,
    ):
        self.imagen_base = pygame.image.load(ruta_imagen).convert_alpha()
        self.angulo = angulo_inicial
        self.imagen = pygame.transform.rotate(self.imagen_base, self.angulo)

        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.velocidad = velocidad
        self.controlador = controlador

    def rotar_a(self, nuevo_angulo: float):
        centro = self.rect.center
        self.angulo = nuevo_angulo
        self.imagen = pygame.transform.rotate(self.imagen_base, self.angulo)
        self.rect = self.imagen.get_rect(center=centro)

    def actualizar(self):
        dir_x, dir_y = self.controlador.obtener_direccion()
        self.rect.x += dir_x * self.velocidad
        self.rect.y += dir_y * self.velocidad

    def dibujar(self, superficie: pygame.Surface):
        superficie.blit(self.imagen, self.rect)