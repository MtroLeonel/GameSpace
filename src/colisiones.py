from nave import NaveEspacial


class GestorColisiones:
    @staticmethod
    def jugador_vs_enemigos(jugador: NaveEspacial, enemigos: list[NaveEspacial]) -> bool:
        return any(enemigo.rect.colliderect(jugador.rect) for enemigo in enemigos)
