import pygame

from estado import EstadoJuego


class Boton:
    def __init__(self, x: int, y: int, w: int, h: int, texto: str, accion):
        self.rect = pygame.Rect(x, y, w, h)
        self.texto = texto
        self.accion = accion

    def dibujar(self, pantalla: pygame.Surface, fuente: pygame.font.Font):
        pygame.draw.rect(pantalla, (35, 35, 60), self.rect, border_radius=8)
        pygame.draw.rect(pantalla, (180, 180, 220), self.rect, 2, border_radius=8)
        texto_img = fuente.render(self.texto, True, (240, 240, 255))
        texto_rect = texto_img.get_rect(center=self.rect.center)
        pantalla.blit(texto_img, texto_rect)

    def click(self, pos_mouse: tuple[int, int]):
        if self.rect.collidepoint(pos_mouse):
            self.accion()


class UIJuego:
    def __init__(self, on_iniciar, on_pausar, on_reiniciar):
        self.fuente = pygame.font.SysFont("consolas", 28)
        self.fuente_btn = pygame.font.SysFont("consolas", 22)

        self.boton_iniciar = Boton(20, 20, 130, 40, "Iniciar", on_iniciar)
        self.boton_pausar = Boton(165, 20, 130, 40, "Pausar", on_pausar)
        self.boton_reiniciar = Boton(310, 20, 140, 40, "Reiniciar", on_reiniciar)

    def manejar_evento(self, evento: pygame.event.Event):
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            pos = pygame.mouse.get_pos()
            self.boton_iniciar.click(pos)
            self.boton_pausar.click(pos)
            self.boton_reiniciar.click(pos)

    def dibujar(self, pantalla: pygame.Surface, estado: EstadoJuego, puntos: int):
        puntaje_img = self.fuente.render(f"Puntos: {puntos}", True, (255, 255, 255))
        pantalla.blit(puntaje_img, (620, 20))

        if estado == EstadoJuego.GAME_OVER:
            over_img = self.fuente.render("GAME OVER", True, (255, 80, 80))
            pantalla.blit(over_img, (320, 280))
        elif estado == EstadoJuego.PAUSADO:
            pausa_img = self.fuente.render("PAUSADO", True, (255, 255, 120))
            pantalla.blit(pausa_img, (340, 280))
        elif estado == EstadoJuego.MENU:
            menu_img = self.fuente.render("MENU", True, (200, 220, 255))
            pantalla.blit(menu_img, (360, 280))

        self.boton_iniciar.dibujar(pantalla, self.fuente_btn)
        self.boton_pausar.dibujar(pantalla, self.fuente_btn)
        self.boton_reiniciar.dibujar(pantalla, self.fuente_btn)
