# DOCUMENTACION TECNICA

## 1. Objetivo

Este proyecto implementa un juego arcade de nave con arquitectura modular orientada a objetos para facilitar mantenimiento y extension.

## 2. Arquitectura por modulos

### src/main.py
- Clase JuegoArcadeNave.
- Responsabilidad: ciclo principal (eventos, update, render) y composicion de componentes.

### src/estado.py
- Enum EstadoJuego con los estados:
  - MENU
  - JUGANDO
  - PAUSADO
  - GAME_OVER

### src/nave.py
- Clase NaveEspacial.
- Responsabilidades:
  - Cargar sprite.
  - Rotar sprite preservando centro.
  - Actualizar posicion segun controlador.
  - Dibujar en pantalla.

### src/controladores.py
- ControlTecladoPygame: direccion del jugador.
- ControlIAEnemigo: movimiento vertical constante de enemigos.

### src/enemigos.py
- Clase GestorEnemigos.
- Responsabilidades:
  - Spawn temporizado de enemigos.
  - Posicion aleatoria en eje X.
  - Velocidad aleatoria por enemigo.
  - Eliminacion de enemigos fuera de pantalla.
  - Devolver puntos ganados por enemigos esquivados.

### src/marcador.py
- Clase Marcador.
- Responsabilidades:
  - Almacenar puntos.
  - Reiniciar puntaje.
  - Sumar puntos por regla.

### src/colisiones.py
- Clase GestorColisiones.
- Responsabilidad:
  - Evaluar colision entre nave del jugador y enemigos.

### src/ui.py
- Clase Boton.
- Clase UIJuego.
- Responsabilidades:
  - Dibujar botones de estado.
  - Procesar clicks de usuario.
  - Mostrar HUD (puntaje y estado visual).

### src/fondo.py
- Clase FondoJuego.
- Responsabilidades:
  - Render color base.
  - Render imagen de fondo opcional.
  - Scroll vertical opcional para animacion.

### src/audio_juego.py
- Clase AudioJuego.
- Responsabilidades:
  - Inicializar mixer de pygame.
  - Reproducir musica por estado.
  - Reproducir efectos (ej. colision).
  - Tolerar ausencia de archivos de audio.

## 3. Flujo de ejecucion

1. main.py construye todos los objetos de dominio y soporte.
2. El estado inicial es MENU.
3. UI procesa botones:
   - Iniciar -> JUGANDO.
   - Pausar -> PAUSADO.
   - Reiniciar -> MENU y limpia partida.
4. En JUGANDO:
   - Se mueve jugador.
   - Se generan y actualizan enemigos.
   - Se suman puntos por enemigos que salen de pantalla.
   - Se valida colision.
5. Si hay colision:
   - Estado pasa a GAME_OVER.
   - Se reproduce sonido de colision.
   - Se detiene musica de juego.

## 4. Extension futura

### Fondo estatico o en movimiento
- Ya soportado por FondoJuego.
- Para activar imagen:
  - Guardar src/assets/background.png.
  - Construir FondoJuego con ruta_imagen y velocidad_scroll > 0 para animado.

### Audio por estado
- Ya soportado por AudioJuego y main.py.
- Archivos esperados:
  - src/assets/menu_music.wav
  - src/assets/game_music.wav
  - src/assets/collision.wav

### Nuevas mecanicas
- Disparos: crear gestor_disparos.py y verificar colision disparo-enemigo.
- Niveles: escalar spawn_ms y velocidad por tiempo/puntaje.
- Vidas: crear clase SistemaVidas y cambiar condicion de game over.

## 5. Convenciones de diseno

- Cada modulo tiene una responsabilidad clara.
- main.py evita logica de bajo nivel y delega en gestores.
- Las reglas del juego viven en clases de dominio, no en funciones sueltas.
- El sistema tolera falta de assets opcionales para facilitar pruebas.

## 6. Validacion recomendada

- Ejecutar analisis de errores en VS Code.
- Probar flujo completo:
  1. Arranque en MENU.
  2. Iniciar partida.
  3. Pausar y reanudar.
  4. Reiniciar partida.
  5. Verificar suma de puntos.
  6. Verificar game over por colision.
  7. Verificar audio con y sin archivos en assets.
