import pygame
import sys
from controladores import ControlTecladoPygame, ControlIAEnemigo
from nave import NaveEspacial

pygame.init()
pantalla = pygame.display.set_mode((800, 600))
reloj = pygame.time.Clock()

control_jugador = ControlTecladoPygame()
control_enemigo = ControlIAEnemigo()

# AQUÍ PASAMOS EL ARCHIVO PNG A CADA NAVE
jugador = NaveEspacial("craft.png", 375, 500, 5, control_jugador)
enemigo = NaveEspacial("enemy.png", 375, 50, 2, control_enemigo)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    jugador.actualizar()
    enemigo.actualizar()

    # Pintamos el fondo (espacio)
    pantalla.fill((20, 20, 40)) 
    
    # EN LUGAR DE DIBUJAR UN RECTÁNGULO, USAMOS 'BLIT' PARA PEGAR LA IMAGEN
    # .blit() toma dos cosas: (Qué imagen pegar, En qué posición [usamos su rect])
    pantalla.blit(jugador.imagen, jugador.rect)
    pantalla.blit(enemigo.imagen, enemigo.rect)
    
    pygame.display.flip()
    reloj.tick(60)