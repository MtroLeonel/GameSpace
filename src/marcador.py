class Marcador:
    def __init__(self, puntos_por_enemigo: int = 10):
        self.puntos_por_enemigo = puntos_por_enemigo
        self.puntos = 0

    def reiniciar(self):
        self.puntos = 0

    def sumar_enemigo_esquivado(self, cantidad: int = 1):
        self.puntos += self.puntos_por_enemigo * cantidad

    def sumar_puntos(self, puntos: int):
        self.puntos += puntos
