import pygame
import sys

# 1. INICIALIZACIÓN
pygame.init()
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Invasión Arcade - Python by Ninjaxleo")
reloj = pygame.time.Clock()

# 2. DEFINICIÓN DE LA CLASE (El Prefab)
class Personaje:
    def __init__(self, color, x, y, velocidad):
        self.color = color
        # pygame.Rect nos da la "caja de colisión" y posición
        self.rect = pygame.Rect(x, y, 50, 50) 
        self.velocidad = velocidad

    def dibujar(self, superficie):
        pygame.draw.rect(superficie, self.color, self.rect)

    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad

# 3. CREACIÓN DE OBJETOS (Instancias)
jugador = Personaje((0, 255, 0), 375, 500, 5) # Cuadrado Verde
enemigo = Personaje((255, 0, 0), 375, 50, 0)  # Cuadrado Rojo

# 4. EL BUCLE DEL JUEGO (Game Loop)
corriendo = True
while corriendo:
    # A. Leer eventos (si el usuario cierra la ventana)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # B. Lógica
    teclas = pygame.key.get_pressed()
    jugador.mover(teclas)

    # C. Renderizado (Dibujar)
    pantalla.fill((0, 0, 0)) # Pintar fondo negro
    jugador.dibujar(pantalla)
    enemigo.dibujar(pantalla)

    pygame.display.flip() # Actualizar pantalla
    reloj.tick(60)        # Limitar a 60 FPS

pygame.quit()
sys.exit()