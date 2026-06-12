import random
import pygame

from controladores import ControlIAEnemigo
from nave import NaveEspacial


class GestorEnemigos:
    def __init__(
        self,
        control_enemigo: ControlIAEnemigo,
        ancho_pantalla: int,
        alto_pantalla: int,
        ruta_imagen_enemigo: str,
        spawn_ms: int = 1000,
    ):
        self.control_enemigo = control_enemigo
        self.ancho_pantalla = ancho_pantalla
        self.alto_pantalla = alto_pantalla
        self.ruta_imagen_enemigo = ruta_imagen_enemigo
        self.spawn_ms = spawn_ms

        self.ultimo_spawn = pygame.time.get_ticks()
        self.enemigos: list[NaveEspacial] = []

    def reiniciar(self, tiempo_actual_ms: int):
        self.enemigos.clear()
        self.ultimo_spawn = tiempo_actual_ms

    def _crear_enemigo(self):
        enemigo = NaveEspacial(
            self.ruta_imagen_enemigo,
            0,
            -60,
            random.randint(2, 5),
            self.control_enemigo,
            angulo_inicial=0,
        )
        max_x = self.ancho_pantalla - enemigo.rect.width
        enemigo.rect.x = random.randint(0, max(0, max_x))
        self.enemigos.append(enemigo)

    def actualizar(self, tiempo_actual_ms: int) -> int:
        puntos_ganados = 0

        if tiempo_actual_ms - self.ultimo_spawn >= self.spawn_ms:
            self._crear_enemigo()
            self.ultimo_spawn = tiempo_actual_ms

        for enemigo in self.enemigos[:]:
            enemigo.actualizar()
            if enemigo.rect.top > self.alto_pantalla:
                self.enemigos.remove(enemigo)
                puntos_ganados += 1

        return puntos_ganados

    def dibujar(self, pantalla: pygame.Surface):
        for enemigo in self.enemigos:
            enemigo.dibujar(pantalla)
