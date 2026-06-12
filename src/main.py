import pygame
import sys
import os

from audio_juego import AudioJuego
from colisiones import GestorColisiones
from controladores import ControlTecladoPygame, ControlIAEnemigo
from enemigos import GestorEnemigos
from estado import EstadoJuego
from fondo import FondoJuego
from marcador import Marcador
from nave import NaveEspacial
from ui import UIJuego


class JuegoArcadeNave:
    def __init__(self):
        pygame.init()
        self.ancho = 800
        self.alto = 600
        self.pantalla = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption("Arcade Nave")
        self.reloj = pygame.time.Clock()

        self.base_dir = os.path.dirname(__file__)
        self.assets_dir = os.path.join(self.base_dir, "assets")

        self.control_jugador = ControlTecladoPygame()
        self.control_enemigo = ControlIAEnemigo()

        self.estado = EstadoJuego.MENU
        self.marcador = Marcador(puntos_por_enemigo=1)
        fondo_ruta = os.path.join(self.assets_dir, "background.png")
        self.fondo = FondoJuego(
            self.ancho,
            self.alto,
            color_fondo=(20, 20, 40),
            ruta_imagen=fondo_ruta,
            velocidad_scroll=0,
        )
        self.audio = AudioJuego()

        self.gestor_enemigos = GestorEnemigos(
            self.control_enemigo,
            self.ancho,
            self.alto,
            os.path.join(self.base_dir, "enemy.png"),
            spawn_ms=1000,
        )
        self.gestor_colisiones = GestorColisiones()

        # Rotamos 90 grados para que la nave apunte hacia los enemigos.
        self.jugador = NaveEspacial(
            os.path.join(self.base_dir, "craft.png"),
            375,
            500,
            5,
            self.control_jugador,
            angulo_inicial=90,
        )

        self.ui = UIJuego(self.iniciar, self.pausar, self.reiniciar)
        self._cargar_audio_base()
        self._actualizar_musica_por_estado()

    def _cargar_audio_base(self):
        self.audio.cargar_sonido(
            "colision",
            os.path.join(self.assets_dir, "impactv2_725546__whatchar__dsgnimpt_sci-fimpact9_whatley_impacts.wav"),
            volumen=0.9,
            #colision_854111__artninja__custom_unlimited_bladeworks_berserker_roar_sound_05132026.wav
        )

    def _actualizar_musica_por_estado(self):
        if self.estado in (EstadoJuego.MENU, EstadoJuego.PAUSADO):
            self.audio.reproducir_musica(
                "menu",
                os.path.join(self.assets_dir, "inicio_pausa_856033__loudkevin__remedy-loop.mp3"),
                volumen=0.5,
            )
        elif self.estado == EstadoJuego.JUGANDO:
            self.audio.reproducir_musica(
                "juego",
                os.path.join(self.assets_dir, "play_855292__thebigyoshi__synthwave-high-tech-loop.wav"),
                volumen=0.5,
            )
        elif self.estado == EstadoJuego.GAME_OVER:
            self.audio.detener_musica()

    def iniciar(self):
        if self.estado != EstadoJuego.GAME_OVER:
            self.estado = EstadoJuego.JUGANDO
            self._actualizar_musica_por_estado()

    def pausar(self):
        if self.estado == EstadoJuego.JUGANDO:
            self.estado = EstadoJuego.PAUSADO
            self._actualizar_musica_por_estado()

    def reiniciar(self):
        self.estado = EstadoJuego.MENU
        self.marcador.reiniciar()
        self.gestor_enemigos.reiniciar(pygame.time.get_ticks())
        self.jugador.rect.x = 375
        self.jugador.rect.y = 500
        self._actualizar_musica_por_estado()

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.ui.manejar_evento(evento)

    def actualizar(self):
        self.fondo.actualizar()

        if self.estado != EstadoJuego.JUGANDO:
            return

        self.jugador.actualizar()

        if self.jugador.rect.left < 0:
            self.jugador.rect.left = 0
        if self.jugador.rect.right > self.ancho:
            self.jugador.rect.right = self.ancho

        ahora = pygame.time.get_ticks()
        puntos_ganados = self.gestor_enemigos.actualizar(ahora)
        if puntos_ganados:
            self.marcador.sumar_puntos(puntos_ganados)

        if self.gestor_colisiones.jugador_vs_enemigos(self.jugador, self.gestor_enemigos.enemigos):
            self.estado = EstadoJuego.GAME_OVER
            self.audio.reproducir_sonido("colision")
            self._actualizar_musica_por_estado()

    def dibujar(self):
        self.fondo.dibujar(self.pantalla)

        self.jugador.dibujar(self.pantalla)
        self.gestor_enemigos.dibujar(self.pantalla)
        self.ui.dibujar(self.pantalla, self.estado, self.marcador.puntos)

        pygame.display.flip()

    def ejecutar(self):
        while True:
            self.manejar_eventos()
            self.actualizar()
            self.dibujar()
            self.reloj.tick(60)


if __name__ == "__main__":
    juego = JuegoArcadeNave()
    juego.ejecutar()