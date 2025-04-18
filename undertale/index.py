import pygame
import sys
import time
import subprocess

# Inicializar Pygame
pygame.init()

# Obtener la información de la pantalla del dispositivo
screen_info = pygame.display.Info()

# Definir el ancho y alto de la pantalla
width = screen_info.current_w
height = screen_info.current_h

# Colores
white = (255, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)

# Crear la ventana de Pygame en modo pantalla completa
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

# Establecer el título de la ventana
pygame.display.set_caption("Undertale")

# Inicializar el reproductor de música
pygame.mixer.init()

# Cargar y escalar la imagen de introducción
intro_image = pygame.image.load('images/undertale_letras.png')
intro_image_scaled = pygame.transform.scale(intro_image, (width, height))

# Pantalla de espera con música de intro
screen.fill(black)
screen.blit(intro_image_scaled, (0, 0))
pygame.display.flip()

# Reproducir la música de intro
intro_sound = pygame.mixer.Sound('sound/intro.mp3')
intro_sound.play()

# Mantener la imagen visible durante 3 segundos
start_time = time.time()
while time.time() - start_time < 3:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()

intro_sound.stop()

# Limpiar la pantalla después de la espera
screen.fill(black)
pygame.display.flip()

# Cargar y reproducir la música del menú
pygame.mixer.music.load('sound/undertale_menu.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Cargar las imágenes
image_top = pygame.image.load('images/pilares_menu.png')
image_bottom = pygame.image.load('images/toriel_menu.png')

# Redimensionar las imágenes
new_width_top = int(width * 0.3)
new_height_top = int(new_width_top * image_top.get_height() / image_top.get_width())
image_top = pygame.transform.scale(image_top, (new_width_top, new_height_top))

new_width_bottom = int(width * 0.4)
new_height_bottom = int(new_width_bottom * image_bottom.get_height() / image_bottom.get_width())
image_bottom = pygame.transform.scale(image_bottom, (new_width_bottom, new_height_bottom))

# Definir las propiedades de los botones
button_width = 150
button_height = 150
button_spacing = 20

button_x_jugar = (width - (2 * button_width + button_spacing)) // 2
button_x_salir = button_x_jugar + button_width + button_spacing
button_y = (height - button_height) // 2

button_text_color_default = white
button_text_color_selected = yellow

selected_button = "Jugar"

# Función para salir del programa
def salir():
    pygame.quit()
    sys.exit()

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                selected_button = "Jugar"
            elif event.key == pygame.K_RIGHT:
                selected_button = "Salir"
            elif event.key == pygame.K_RETURN:
                if selected_button == "Jugar":
                    pygame.mixer.music.pause()
                    subprocess.run(["python3", "undertale_juego.py"])
                    pygame.mixer.music.unpause()
                elif selected_button == "Salir":
                    salir()

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Dibujar botón "Jugar"
    font = pygame.font.Font(None, 36)
    jugar_text = font.render("Jugar", True, button_text_color_selected if selected_button == "Jugar" else button_text_color_default)
    screen.blit(jugar_text, (button_x_jugar + (button_width - jugar_text.get_width()) // 2, button_y))

    # Dibujar botón "Salir"
    salir_text = font.render("Salir", True, button_text_color_selected if selected_button == "Salir" else button_text_color_default)
    screen.blit(salir_text, (button_x_salir + (button_width - salir_text.get_width()) // 2, button_y))

    # Agregar texto centrado entre los botones y el borde de la ventana
    info_font = pygame.font.Font(None, 48)
    info_text = info_font.render("UNDERTALE", True, white)
    text_x = (width - info_text.get_width()) // 2
    text_y = button_y - (info_text.get_height() + 20)
    screen.blit(info_text, (text_x, text_y))

    # Agregar segundo texto centrado encima del primer texto
    second_info_text = info_font.render("LV1", True, white)
    second_text_x = (width - second_info_text.get_width()) // 2
    second_text_y = text_y - (second_info_text.get_height() + 10)
    screen.blit(second_info_text, (second_text_x, second_text_y))

    # Obtener el tamaño de las imágenes
    image_top_width, image_top_height = image_top.get_size()
    image_bottom_width, image_bottom_height = image_bottom.get_size()

    # Dibujar la imagen superior centrada
    screen.blit(image_top, ((width - image_top_width) // 2, 10))

    # Ajustar la posición de la imagen inferior
    image_bottom_y = height - image_bottom_height - 30
    screen.blit(image_bottom, ((width - image_bottom_width) // 2, image_bottom_y))

    # Agregar texto gris debajo de la imagen inferior
    bottom_text = info_font.render("UNDERTALE V1.00 PYTHON BY LUIS", True, (100, 100, 100))
    screen.blit(bottom_text, ((width - bottom_text.get_width()) // 2, image_bottom_y + image_bottom_height + 10))

    # Actualizar la pantalla
    pygame.display.flip()