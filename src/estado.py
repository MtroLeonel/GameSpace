from enum import Enum, auto


class EstadoJuego(Enum):
    MENU = auto()
    JUGANDO = auto()
    PAUSADO = auto()
    GAME_OVER = auto()
