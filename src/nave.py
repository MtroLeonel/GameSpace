import pygame
from interfaces import IControlador

class NaveEspacial:
    # Agregamos 'ruta_imagen' a los parámetros
    def __init__(self, ruta_imagen: str, x: float, y: float, velocidad: float, controlador: IControlador):
        # 1. Cargar la imagen desde el archivo PNG
        self.imagen = pygame.image.load(ruta_imagen).convert_alpha()
        
        # Opcional: Si los alumnos hicieron la imagen muy grande, el código puede achicarla
        # self.imagen = pygame.transform.scale(self.imagen, (64, 64))
        
        # 2. Obtener el rectángulo (hitbox) exacto del tamaño de la imagen
        self.rect = self.imagen.get_rect()
        
        # 3. Posicionar el rectángulo
        self.rect.x = x
        self.rect.y = y
        
        self.velocidad = velocidad
        self.controlador = controlador

    def actualizar(self):
        dir_x, dir_y = self.controlador.obtener_direccion()
        # Movemos el rectángulo en lugar de variables X e Y sueltas
        self.rect.x += dir_x * self.velocidad
        self.rect.y += dir_y * self.velocidad