import pygame
import sys
import io
import keyword
import re

# Initialisation de pygame
pygame.init()

# Constantes
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
FONT = pygame.font.Font(None, 24)
INDENT_SIZE = 3  
CURSOR_BLINK_SPEED = 500  


# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Executor avec Pygame")

# Zones de texte
input_box = pygame.Rect(50, 50, 700, 200)
output_box = pygame.Rect(50, 300, 700, 200)
button_rect = pygame.Rect(350, 520, 100, 40)

# Texte par défaut
code_text = "print('Hello, world!')"
output_text = ""
cursor_position = len(code_text)
cursor_visible = True
last_cursor_toggle = pygame.time.get_ticks()
code_longueur_avant_echap = 0
indente_ou_pas = False
nb_espace = 1

# Activer la répétition des touches
pygame.key.set_repeat(300, 50)


def highlight_keywords(text):
    tokens = re.split(r'(\W+)', text)  # Sépare les mots tout en conservant la ponctuation
    highlighted = []
    for token in tokens:
        if token in keyword.kwlist:  # Vérifie si le mot est un mot-clé Python
            highlighted.append((token, BLUE))
        else:
            highlighted.append((token, BLACK))
    return highlighted
    
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
                INDENT_SIZE = max(0, INDENT_SIZE-1)
                if INDENT_SIZE == 0:
                    indente_ou_pas = False
            elif event.key == pygame.K_DELETE:  # Supprime le caractère devant le curseur
                if cursor_position < len(code_text):
                    code_text = code_text[:cursor_position] + code_text[cursor_position + 1:]
            elif event.key == pygame.K_TAB:  # Insère 3 espaces quand on appuie sur "Tab"
                code_text = code_text[:cursor_position] + " " * INDENT_SIZE + code_text[cursor_position:]
                cursor_position += INDENT_SIZE
            elif event.key == pygame.K_RETURN:
                INDENT_SIZE = 0
                nb_espace = 0
                for i in range(code_longueur_avant_echap,len(code_text)):
                    if code_text[i] == " ":
                        nb_espace += 1
                    else:
                        break
                INDENT_SIZE = nb_espace
                if code_text[-1] == ":":
                    INDENT_SIZE += 3
                code_longueur_avant_echap = len(code_text)+1 
                
                while INDENT_SIZE % 3 != 0:
                    INDENT_SIZE -= 1

                code_text = code_text[:cursor_position] + "\n" + " " * INDENT_SIZE + code_text[cursor_position:]
                cursor_position += 1 + INDENT_SIZE
            elif event.key == pygame.K_LEFT:
                cursor_position = max(0, cursor_position - 1)
            elif event.key == pygame.K_RIGHT:
                cursor_position = min(len(code_text), cursor_position + 1)
            elif event.key == pygame.K_COLON:
                indente_ou_pas = True
                code_text = code_text[:cursor_position] + event.unicode + code_text[cursor_position:]
                cursor_position += 1
            else:
                code_text = code_text[:cursor_position] + event.unicode + code_text[cursor_position:]
                cursor_position += 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
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

    lines = code_text.split("\n")
    cursor_x, cursor_y = input_box.x + 5, input_box.y + 5  
    pos = 0
    for i, line in enumerate(lines):
        highlighted_tokens = highlight_keywords(line)
        x_offset = input_box.x + 5
        for token, color in highlighted_tokens:
            token_render = FONT.render(token, True, color)
            screen.blit(token_render, (x_offset, input_box.y + 5 + i * 20))
            x_offset += token_render.get_width()
        
        if pos <= cursor_position <= pos + len(line):
            cursor_x = input_box.x + 5 + FONT.size(line[:cursor_position - pos])[0]
            cursor_y = input_box.y + 5 + i * 20  
        pos += len(line) + 1  

    # Affichage du texte et positionnement du curseur
    lines = code_text.split("\n")
    display_text = ""
    cursor_x, cursor_y = input_box.x + 5, input_box.y + 5  
    for i, line in enumerate(lines):
        if len(display_text) <= cursor_position <= len(display_text) + len(line):
            cursor_x = input_box.x + 5 + FONT.size(line[:cursor_position - len(display_text)])[0]
            cursor_y = input_box.y + 5 + i * 20  
        display_text += line + "\n"
        screen.blit(FONT.render(line, True, BLACK), (input_box.x + 5, input_box.y + 5 + i * 20))

    # Dessiner le curseur
    if cursor_visible:
        pygame.draw.line(screen, BLACK, (cursor_x, cursor_y), (cursor_x, cursor_y + 20), 2)

    # Affichage de la sortie
    output_lines = output_text.split("\n")
    for i, line in enumerate(output_lines):
        screen.blit(FONT.render(line, True, BLACK), (output_box.x + 5, output_box.y + 5 + i * 20))

    pygame.display.flip()
    

pygame.quit()
sys.exit()
