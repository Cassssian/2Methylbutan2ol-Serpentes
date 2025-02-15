import pygame
import sys
import io

# Initialisation de pygame
pygame.init()

# Constantes
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
FONT = pygame.font.Font(None, 24)
INDENT_SIZE = 3  
CURSOR_BLINK_SPEED = 500  
LINE_HEIGHT = 20  # Hauteur d'une ligne de texte
VISIBLE_LINES = 10  # Nombre de lignes visibles dans la zone de texte

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Executor avec Pygame")

# Zones de texte
input_box = pygame.Rect(50, 50, 700, 200)
output_box = pygame.Rect(50, 300, 700, 200)
button_rect = pygame.Rect(350, 520, 100, 40)

# Texte
code_text = "print('Hello, world!')"
output_text = ""
cursor_position = len(code_text)
cursor_visible = True
last_cursor_toggle = pygame.time.get_ticks()
scroll_offset = 0  # Décalage pour le défilement vertical

# Activer la répétition des touches
pygame.key.set_repeat(300, 50)

# Boucle principale
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if cursor_position > 0:
                    code_text = code_text[:cursor_position - 1] + code_text[cursor_position:]
                    cursor_position -= 1
            elif event.key == pygame.K_DELETE:  
                if cursor_position < len(code_text):
                    code_text = code_text[:cursor_position] + code_text[cursor_position + 1:]
            elif event.key == pygame.K_TAB:  
                code_text = code_text[:cursor_position] + " " * INDENT_SIZE + code_text[cursor_position:]
                cursor_position += INDENT_SIZE
            elif event.key == pygame.K_RETURN:
                code_text = code_text[:cursor_position] + "\n" + code_text[cursor_position:]
                cursor_position += 1
            elif event.key == pygame.K_LEFT:
                cursor_position = max(0, cursor_position - 1)
            elif event.key == pygame.K_RIGHT:
                cursor_position = min(len(code_text), cursor_position + 1)
            elif event.key == pygame.K_UP:  
                scroll_offset = max(0, scroll_offset - 1)
            elif event.key == pygame.K_DOWN:  
                scroll_offset = min(len(code_text.split("\n")) - VISIBLE_LINES, scroll_offset + 1)
            else:
                code_text = code_text[:cursor_position] + event.unicode + code_text[cursor_position:]
                cursor_position += 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Molette vers le haut
                scroll_offset = max(0, scroll_offset - 1)
            elif event.button == 5:  # Molette vers le bas
                scroll_offset = min(len(code_text.split("\n")) - VISIBLE_LINES, scroll_offset + 1)
            elif button_rect.collidepoint(event.pos):
                try:
                    old_stdout = sys.stdout
                    sys.stdout = io.StringIO()
                    exec(code_text, {})
                    output_text = sys.stdout.getvalue()
                    sys.stdout = old_stdout
                except Exception as e:
                    output_text = str(e)

    # Gestion du clignotement du curseur
    current_time = pygame.time.get_ticks()
    if current_time - last_cursor_toggle > CURSOR_BLINK_SPEED:
        cursor_visible = not cursor_visible
        last_cursor_toggle = current_time

    # Affichage des zones
    pygame.draw.rect(screen, GRAY, input_box)
    pygame.draw.rect(screen, GRAY, output_box)
    pygame.draw.rect(screen, BLACK, button_rect)

    # Texte
    screen.blit(FONT.render("Zone de Code :", True, BLACK), (50, 30))
    screen.blit(FONT.render("Console :", True, BLACK), (50, 280))
    screen.blit(FONT.render("Exécuter", True, WHITE), (button_rect.x + 20, button_rect.y + 10))

    # Affichage des lignes visibles
    lines = code_text.split("\n")
    display_text = ""
    cursor_x, cursor_y = input_box.x + 5, input_box.y + 5  
    for i, line in enumerate(lines[scroll_offset:scroll_offset + VISIBLE_LINES]):
        actual_line_index = i + scroll_offset
        if len(display_text) <= cursor_position <= len(display_text) + len(line):
            cursor_x = input_box.x + 5 + FONT.size(line[:cursor_position - len(display_text)])[0]
            cursor_y = input_box.y + 5 + i * LINE_HEIGHT  
        display_text += line + "\n"
        screen.blit(FONT.render(line, True, BLACK), (input_box.x + 5, input_box.y + 5 + i * LINE_HEIGHT))

    # Dessiner le curseur
    if cursor_visible:
        pygame.draw.line(screen, BLACK, (cursor_x, cursor_y), (cursor_x, cursor_y + LINE_HEIGHT), 2)

    # Affichage de la sortie
    output_lines = output_text.split("\n")
    for i, line in enumerate(output_lines):
        screen.blit(FONT.render(line, True, BLACK), (output_box.x + 5, output_box.y + 5 + i * LINE_HEIGHT))

    pygame.display.flip()

pygame.quit()
sys.exit()
