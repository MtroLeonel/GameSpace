import os
import pygame


class FondoJuego:
    def __init__(
        self,
        ancho: int,
        alto: int,
        color_fondo: tuple[int, int, int] = (20, 20, 40),
        ruta_imagen: str | None = None,
        velocidad_scroll: int = 0,
    ):
        self.ancho = ancho
        self.alto = alto
        self.color_fondo = color_fondo
        self.velocidad_scroll = velocidad_scroll
        self.offset_y = 0

        self.imagen = None
        if ruta_imagen and os.path.exists(ruta_imagen):
            cargada = pygame.image.load(ruta_imagen).convert()
            self.imagen = pygame.transform.scale(cargada, (self.ancho, self.alto))

    def actualizar(self):
        if self.imagen and self.velocidad_scroll > 0:
            self.offset_y = (self.offset_y + self.velocidad_scroll) % self.alto

    def dibujar(self, pantalla: pygame.Surface):
        if not self.imagen:
            pantalla.fill(self.color_fondo)
            return

        y1 = -self.offset_y
        y2 = y1 + self.alto
        pantalla.blit(self.imagen, (0, y1))
        pantalla.blit(self.imagen, (0, y2))
