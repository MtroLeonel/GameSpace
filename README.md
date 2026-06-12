# Juego Arcade Nave

Proyecto arcade 2D con Pygame orientado a objetos.

## Caracteristicas actuales

- Nave del jugador rotada 90 grados para apuntar a los enemigos.
- Enemigos con spawn aleatorio en X y velocidad variable.
- Botones de control: Iniciar, Pausar y Reiniciar.
- Estados del juego: Menu, Jugando, Pausado, Game Over.
- Colision jugador-enemigo con fin de partida.
- Puntaje acumulado por enemigo esquivado (+10).
- Soporte de fondo estatico o con scroll vertical.
- Soporte de audio por estado y sonido de colision.

## Controles

- Flecha izquierda: mover nave a la izquierda.
- Flecha derecha: mover nave a la derecha.
- Mouse: click en botones de UI.

## Estructura del proyecto

- src/main.py: orquestador principal del juego.
- src/nave.py: entidad NaveEspacial.
- src/controladores.py: entradas de teclado e IA enemiga.
- src/estado.py: enumeracion de estados del juego.
- src/enemigos.py: gestor de spawn y actualizacion de enemigos.
- src/marcador.py: manejo de puntos.
- src/colisiones.py: reglas de colision.
- src/ui.py: botones y HUD.
- src/fondo.py: render de fondo (color, imagen y scroll).
- src/audio_juego.py: reproduccion de musica y efectos.

## Requisitos

- Python 3.10+
- pygame==2.6.1

Instalacion de dependencias:

```bash
pip install -r src/requirements.txt
```

## Ejecucion

Desde la carpeta del proyecto:

```bash
cd src
python main.py
```

## Recursos opcionales (audio/fondo)

Coloca archivos en src/assets para activar estas funciones sin cambiar codigo:

- src/assets/menu_music.wav: musica de menu/pausa.
- src/assets/game_music.wav: musica de partida.
- src/assets/collision.wav: sonido al colisionar.
- src/assets/background.png: fondo de imagen.

Si los archivos no existen, el juego sigue funcionando sin audio o sin imagen de fondo.
