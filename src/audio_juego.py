import os
import pygame


class AudioJuego:
    def __init__(self):
        self.disponible = True
        self.sonidos: dict[str, pygame.mixer.Sound] = {}
        self.musica_actual: str | None = None

        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
        except pygame.error:
            self.disponible = False

    def cargar_sonido(self, clave: str, ruta: str, volumen: float = 1.0):
        if not self.disponible or not os.path.exists(ruta):
            return

        try:
            sonido = pygame.mixer.Sound(ruta)
            sonido.set_volume(volumen)
            self.sonidos[clave] = sonido
        except pygame.error:
            return

    def reproducir_sonido(self, clave: str):
        if not self.disponible:
            return

        sonido = self.sonidos.get(clave)
        if sonido:
            sonido.play()

    def reproducir_musica(self, clave: str, ruta: str, volumen: float = 0.5, loop: bool = True):
        if not self.disponible or not os.path.exists(ruta):
            return

        if self.musica_actual == clave:
            return

        try:
            pygame.mixer.music.load(ruta)
            pygame.mixer.music.set_volume(volumen)
            pygame.mixer.music.play(-1 if loop else 0)
            self.musica_actual = clave
        except pygame.error:
            return

    def detener_musica(self):
        if not self.disponible:
            return

        pygame.mixer.music.stop()
        self.musica_actual = None
