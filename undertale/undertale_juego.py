import pygame
import sys

# Inicializar pygame
pygame.init()

# Obtener información de la pantalla del dispositivo
screen_info = pygame.display.Info()

# Configuración de la pantalla
width, height = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Juego")

# Colores
black = (0, 0, 0)

# Jugador
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height // 2 - player_size // 2
player_speed = 10

# Cargar imagen del jugador
player_image = pygame.image.load("images/corazon.png")
player_image = pygame.transform.scale(player_image, (player_size, player_size))

# Bucle principal del juego
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < height - player_size:
        player_y += player_speed

    # Limpiar la pantalla
    screen.fill(black)

    # Dibujar al jugador
    screen.blit(player_image, (player_x, player_y))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del juego
    clock.tick(60)