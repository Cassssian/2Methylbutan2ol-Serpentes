# type: ignore[import]
# pyright: ignore[import]
# pylint: disable=import-error
# ruff: noqa: F401, E402
# mypy: ignore-errors
# flake8: noqa: F401

import subprocess
import sys
import requests
def util():
    for i in ["pkg_resources", "packaging"]:
        try:
            __import__(i)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", i]) if not i=="pkg_resources" else subprocess.check_call([sys.executable, "-m", "pip", "install", "setuptools"])
        
util()

import pkg_resources
from packaging import version

def clv():
        current_version = pkg_resources.get_distribution("itmgr").version
        
        response = requests.get(f"https://pypi.org/pypi/itmgr/json")
        latest_version = response.json()["info"]["version"]
        
        is_latest = version.parse(current_version) >= version.parse(latest_version)

        
        
        return is_latest

def itmgr_dep():
    """
    Install and import necessary dependencies for the project.
    """
    try:
        __import__("itmgr")
        
        if not clv():
            if (result := input("\x1b[38;5;116mUne mise à jour a été trouvée, souhaitez-vous l'installer ? (y/n) : \x1b[0m")).lower() == 'y':
                subprocess.check_call([sys.executable, "-m", "pip", "install", "itmgr", "--upgrade"])
            else: 
                print("\x1b[38;5;196mLa mise à jour n'a pas été effectuée.\x1b[0m")

    except:
        subprocess.run(["pip", "install", "itmgr"])
    

itmgr_dep()
from itmgr import install_and_import

try:
    install_and_import(('os', True, False),
                        ('sqlite3', True, "sql"),
                        ('cv2', True, False),
                        ('astroid', True, False),
                        ('ast', True, False),
                        ('tokenize', True, False),
                        ('io', True, False),
                        ('traceback', True, False),
                        ('typing', ['Dict', 'List', 'Tuple'], False),
                        )
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
    install_and_import(('pygame', True, "pg"),
                        )
except:
    subprocess.run(["itmgr", "add", "opencv-python", "cv2"])
    install_and_import(('os', True, False),
                        ('sqlite3', True, "sql"),
                        ('cv2', True, False),
                        ('astroid', True, False),
                        ('ast', True, False),
                        ('tokenize', True, False),
                        ('io', True, False),
                        ('traceback', True, False),
                        ('typing', ['Dict', 'List', 'Tuple'], False),
                        )
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
    install_and_import(('pygame', True, "pg"),
                        )

class App:
    def __init__(self):
        #-------------------- Initialisation de l'application --------------------#
        self.conn = sql.connect("code.db")
        self.cur = self.conn.cursor()

        self.table_setup(self.cur, self.conn)

        pg.init()

        pg.mixer.init()

        self.clock = pg.time.Clock()

        self.screen_w, self.screen_h = pg.display.Info().current_w, pg.display.Info().current_h
        self.screen = pg.display.set_mode((self.screen_w, self.screen_h))
        pg.display.set_caption("2-Méthylbutan-2-ol Serpentes")
        self.font = pg.font.Font(None, 36)  # None utilise la police par défaut, 36 est la taille
        self.video = cv2.VideoCapture('./img/python.gif')
        #---------------------------------------------------------------------#

        #----------------- Variables pour la gestion du pgm ------------------#
        self.running = True
        self.mode = "menu"
        self.niv = 1
        self.acutal_time = 0
        self.time_limit = 1200
        self.shown_popup = False
        self.popup_text_show = False
        self.scroll_y = 0
        #---------------------------------------------------------------------#

        # ----------------- Couleurs ------------------#
        self.GRAY = (128, 128, 128)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.DARK_BLUE = (0, 0, 128)
        self.YELLOW = (255, 255, 0)
        self.ORANGE = (255, 165, 0)
        self.PURPLE = (128, 0, 128)
        self.PINK = (255, 192, 203)
        self.BROWN = (165, 42, 42)
        self.CYAN = (0, 255, 255)
        self.TEAL = (0, 128, 128)
        self.MAROON = (128, 0, 0)
        self.NAVY = (0, 0, 128)
        self.OLIVE = (128, 128, 0)
        self.TEAL = (0, 128, 128)
        #---------------------------------------------#

        #------------------ Variables pour l'affichage du jeu ------------------#
        self.popup_x = -self.screen_w * 0.4  # Start position off-screen
        self.target_x = 0  # Target position
        self.slide_speed = 30  # Animation speed
        self.popup_closing = False
        #-----------------------------------------------------------------------#

        #------------------ Texte pour les aides ------------------#
        self.dict_elements = {
            "Notions de base": 

                [{"Utilité" : "Quelques notions essentielles qui permettent de débuter la programmation en Python."},
         
                {"Programme" : "Un programme est un texte qui permet de commander un ordinateur. Dans notre cas, il s'agit de créer du code afin des fins spécifiques. Ce texte est composé d'instructions compréhensibles par l'ordinateur. Certaines sont spécifiques à des programmes et permettent de contrôler les instructions sur l'ordinateur (instruction additionner() par exemple), d'autres sont communes à tous les programmes en Python (voir la suite du mémo programmation). Une fois rédigé, le programme est exécuté par un interpréteur."},

                {"Erreurs" : "Les instructions d'un programme doivent être très précises et ne comporter aucune erreur, attention aux fautes de frappe ! En cas d'erreur, l'interpréteur signale un problème dans la console. Par exemple, la ligne de code erronée avance() provoque l'affichage d'une erreur :\n<error>> Ligne 1 : le nom 'avance()' n'est pas défini</error>\n\nIl faudra donc modifier le programme à partir de ce message d'erreur, puis relancer l'exécution jusqu'à ce que le programme soit correct."},
        
                {"Structuration" : "Un programme doit être structuré par des décalages de texte lors de l'utilisation de certaines instructions (if, while, for, etc.). On appelle cela l'indentation du code. Si l'indentation est mauvaise, le programme ne réalise pas ce que l'on veut et cela peut même provoquer des erreurs. Ces décalages s'effectuent avec la touche tabulation du clavier. A noter que l'éditeur de programme ajoute automatiquement des décalages lors de l'utilisation de certaines instructions."},
        
                {"Commentaires" : "Les lignes commençant par # ne sont pas prises en compte par l'interpréteur. Par exemple, la ligne de code <bold># Ceci est un commentaire</bold> n'a aucun effet. Ces lignes permettent de donner des explications dans le programme, on les appelle des commentaires. Les commentaires ne sont pas obligatoires mais ils peuvent aider à la compréhension des programmes par les autres programmeurs."}],

            "Variable": [
                {"Utilité" : "Permet de garder en mémoire des informations au cours de l’exécution d'un programme."},
                 
                 {
                     "Création" : {
                         "text1" : "Donne un nom à un espace mémoire qui pourra par la suite contenir des valeurs.", 
                         "table" : [["lkajajajaj", "img"],["zibed", '.img/images.png'],["dyfugihjo", "yfvubino"],["kalakaka", "lalakajajaja"]], 
                         "text2": "\n<bullet>Le nom de la variable est choisi par le programmeur, il doit être unique dans le programme et ne doit contenir ni espace ni accent.</bullet><bullet>En Python, une variable doit obligatoirement être initialisée à l'aide de l'opérateur = lors de sa création (par exemple intialisée à 0 comme ci-dessus)</bullet>."
                         }
                },
                
                {
                    "Modification" : {
                        "text1" : "Change la valeur contenue dans l'espace mémoire.",
                        "table" : [["lkajajajaj", "img"],["zibed", '.img/images.png'],["dyfugihjo", "yfvubino"],["kalakaka", "lalakajajaja"]]
                    }
                },
                
                {
                    "Utilisation" : {
                        "text1" : "Met à disposition d'une autre instruction la valeur contenue dans l'espace mémoire.",
                        "table" : [["lkajajajaj", "img"],["zibed", '.img/images.png'],["dyfugihjo", "yfvubino"],["kalakaka", "lalakajajaja"]]
                    }
                },
                
                {
                    "Type" : {
                        "text1" : "Une variable peut avoir différents types selon la nature des valeurs qu'elle contient. En Python, on trouve (entre autres) :<dash>des nombres entiers</dash><dash>des nombres décimaux</dash><dash>des chaînes de caractères (texte)</dash><dash>des booléens (Vrai ou Faux)</dash>",
                        "table" : [["lkajajajaj", "img"],["zibed", '.img/images.png'],["dyfugihjo", "yfvubino"],["kalakaka", "lalakajajaja"]],
                        "text2" : "\n<bullet>Le séparateur des nombres décimaux est le point (.)</bullet><bullet>Les chaînes de caractères doivent être entourées par des guillemets \"\".<bullet>Les variables de type booléen (qui n'existent pas en Scratch) peuvent prendre uniquement les valeurs True (vrai) ou False (faux)."
                    }
                }
                ]

            "Conditionnelle":

            [{"Utilité" : "Permet d'exécuter des instructions lorsque certaines conditions sont respectées."},
            ],

            "Boucle for":

            [{"Utilité" : "Permet de répéter des instructions un certain nombre de fois."}
            ],

            "Boucle while":

            [{"Utilité" : "Permet de répéter des instructions tant que certaines conditions sont respectées."},
            
            {"Répétition tant que..." : "Permet de répéter des instructions tant qu'une condition est vraie."},
            
            {
                "Title": {
                    "text1": "Your text content here",
                    "table": [["Header1", "Header2"], ["Data1", "Data2"]],
                    "text2" : "Lakakakakakaka"
                }
            }]
        }
        #----------------------------------------------------------#

        self.run()

    def table_setup(self, cur, conn):
        cur.execute("""CREATE TABLE IF NOT EXISTS CODE
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         photo TEXT NOT NULL,
                         prenom TEXT NOT NULL,
                         nom TEXT NOT NULL,
                         telephone TEXT NOT NULL,
                         emiel TEXT NOT NULL,
                         voiture TEXT NOT NULL)""")
        conn.commit()

    def run(self):
        while self.running:
            self.events = pg.event.get()
            if self.mode ==  "menu":
                self.menu()

            elif self.mode == "game":
                self.game()

            elif self.mode == "settings":
                self.settings()

            elif self.mode == "credits":
                self.credits()

            elif self.mode == "exit":
                self.exit()

            pg.display.update()
            pg.display.flip()
            self.clock.tick(60)


    def menu(self):
        for event in self.events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.mode = "exit"


        self.screen.fill((0, 0, 0))

        ret, frame = self.video.read()
        if not ret:
            self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = self.video.read()

        frame = cv2.resize(frame, (self.screen_w, self.screen_h))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_surface = pg.surfarray.make_surface(frame)
        self.screen.blit(pg.transform.rotate(frame_surface, -90), (0, 0))

        button_width = 200
        button_height = 50
        button_x = self.screen_w // 2 - button_width // 2
        
        buttons = [
            ("Commencer", "game", self.screen_h // 2 - 155, self.GRAY),
            ("Paramètres", "settings", self.screen_h // 2 - 85, self.GRAY),
            ("Crédits", "credits", self.screen_h // 2 - 15, self.GRAY),
            ("Niveau 3", "niveau_3", self.screen_h // 2 + 55, self.GRAY),
            ("Niveau 4", "niveau_4", self.screen_h // 2 + 125, self.GRAY),
            ("Quitter", "exit", self.screen_h // 2 + 195, self.RED)
        ]
        
        
        mouse_pos = pg.mouse.get_pos()
        mouse_click = pg.mouse.get_pressed()[0]
        
        for text, mode, y, color in buttons:
            button_rect = pg.Rect(button_x, y, button_width, button_height)
            hover = button_rect.collidepoint(mouse_pos)
            
            
            pg.draw.rect(self.screen, (200,10,60) if hover else color, button_rect)
            pg.draw.rect(self.screen, self.BLACK, button_rect, 2)
            
            
            text_surface = self.font.render(text, True, self.BLACK)
            text_rect = text_surface.get_rect(center=button_rect.center)
            self.screen.blit(text_surface, text_rect)
            
            
            if hover and mouse_click:
                self.mode = mode    


    def game(self):
        if self.niv == 1:
            self.niveau_1()
        elif self.niv == 2:
            self.niveau_2()
        elif self.niv == 3:
            self.niveau_3()
        elif self.niv == 4:
            self.niveau_4()
        elif self.niv == 5:
            self.niveau_5()

    def render_table(self, table_data, surface_width):
        cell_padding = 10
        row_height = 60
        col_width = surface_width // len(table_data[0]) - cell_padding * 2
        line_thickness = 2
        
        table_height = len(table_data) * row_height
        table_surface = pg.Surface((surface_width, table_height))
        table_surface.fill(self.BLACK)
        
        # Draw cells content
        for row_idx, row in enumerate(table_data):
            for col_idx, cell in enumerate(row):
                x = col_idx * (col_width + cell_padding * 2) + cell_padding
                y = row_idx * row_height + cell_padding
                
                if isinstance(cell, str) and cell.endswith(('.png', '.jpg', '.jpeg')):
                    try:
                        img = pg.image.load(cell)
                        img = pg.transform.scale(img, (col_width, row_height - cell_padding * 2))
                        table_surface.blit(img, (x, y))
                    except:
                        text = self.font.render("Image non trouvée", True, self.RED)
                        table_surface.blit(text, (x, y))
                else:
                    text = self.font.render(str(cell), True, self.WHITE)
                    text_rect = text.get_rect(midleft=(x, y + (row_height - cell_padding * 2) // 2))
                    table_surface.blit(text, text_rect)
        
        # Draw horizontal lines
        for row in range(len(table_data) + 1):
            y = row * row_height
            pg.draw.line(table_surface, self.WHITE, (0, y), (surface_width, y), line_thickness)
        
        # Draw vertical lines
        for col in range(len(table_data[0]) + 1):
            x = col * (col_width + cell_padding * 2)
            pg.draw.line(table_surface, self.WHITE, (x, 0), (x, table_height), line_thickness)
        
        pg.draw.line(table_surface, self.WHITE, (0, table_height - line_thickness), (surface_width, table_height - line_thickness), line_thickness)
        pg.draw.line(table_surface, self.WHITE, (surface_width - line_thickness, 0), (surface_width - line_thickness, table_height), line_thickness)
                    
        return table_surface


    def render_text_multiline(self, text, font, color, max_width):
        lines = []
        bullet_indent = 30


        for line in text.split('\n'):
            words = line.split(' ')
            current_line = []
            current_width = 0
            in_bullet = False
            in_dash = False

            
            i = 0
            while i < len(words):
                word = words[i]

                if '<bullet>' in word:
                    in_bullet = True
                    current_width = bullet_indent
                    word = word.replace('<bullet>', '')
                    
                
                elif '<dash>' in word:
                    in_dash = True
                    current_width = bullet_indent
                    word = word.replace('<dash>', '')

                if '</bullet>' in word:
                    in_bullet = False
                    word = word.replace('</bullet>', '')
                
                elif '</dash>' in word:
                    in_dash = False
                    word = word.replace('</dash>', '')

                # Handle error markup
                if '<error>' in word:
                    error_text = []
                    current_width = 0
                    while i < len(words) and '</error>' not in words[i]:
                        word_clean = words[i].replace('<error>', '')
                        word_surface = font.render(word_clean + ' ', True, self.WHITE)
                        word_width = word_surface.get_width()
                        
                        if current_width + word_width <= max_width:
                            error_text.append(word_clean)
                            current_width += word_width
                        else:
                            error_surface = font.render(' '.join(error_text), True, self.WHITE, self.RED)
                            lines.append(('surface', error_surface))
                            error_text = [word_clean]
                            current_width = word_width
                        i += 1
                        
                    if i < len(words):
                        word_clean = words[i].replace('</error>', '')
                        error_text.append(word_clean)
                        i += 1
                        
                    error_surface = font.render(' '.join(error_text), True, self.WHITE, self.RED)
                    lines.append(('surface', error_surface))
                    continue
                    
                # Handle bold markup
                if '<bold>' in word:
                    bold_text = []
                    current_width = 0
                    while i < len(words) and '</bold>' not in words[i]:
                        word_clean = words[i].replace('<bold>', '')
                        word_surface = font.render(word_clean + ' ', True, self.WHITE)
                        word_width = word_surface.get_width()
                        
                        if current_width + word_width <= max_width:
                            bold_text.append(word_clean)
                            current_width += word_width
                        else:
                            bold_surface = font.render(' '.join(bold_text), True, self.WHITE)
                            pg.draw.rect(bold_surface, self.WHITE, bold_surface.get_rect(), 2)
                            lines.append(('surface', bold_surface))
                            bold_text = [word_clean]
                            current_width = word_width
                        i += 1
                        
                    if i < len(words):
                        word_clean = words[i].replace('</bold>', '')
                        bold_text.append(word_clean)
                        i += 1
                        
                    bold_surface = font.render(' '.join(bold_text), True, self.WHITE)
                    pg.draw.rect(bold_surface, self.WHITE, bold_surface.get_rect(), 2)
                    lines.append(('surface', bold_surface))
                    continue
                
                word_surface = font.render(word + ' ', True, color)
                word_width = word_surface.get_width()
                
                if current_width + word_width <= max_width:
                    current_line.append(word)
                    current_width += word_width
                else:
                    indent = bullet_indent if in_bullet else 0
                    if in_bullet and current_line:
                        lines.append(('bullet', '•', indent - 25))
                    elif in_dash:
                        lines.append(('bullet', '-', indent - 25))
                    lines.append(('text', ' '.join(current_line), indent))
                    current_line = [word]
                    current_width = word_width
                i += 1
                
            if current_line:
                indent = bullet_indent if in_bullet else 0
                if in_bullet:
                    lines.append(('bullet', '•', indent - 25))
                elif in_dash:
                    lines.append(('bullet', '-', indent - 25))
                lines.append(('text', ' '.join(current_line), indent))
                
        return lines

    def draw_scrollable_popup(self, popup_text, scroll_y):
        LEFT_PANEL_WIDTH = self.screen_w * 0.4
        popup_surface = pg.Surface((LEFT_PANEL_WIDTH, self.screen_h))
        content_surface = pg.Surface((LEFT_PANEL_WIDTH, self.screen_h * 2))  # Larger surface for content
        
        popup_surface.fill(self.BLACK)
        content_surface.fill(self.BLACK)
        
        # Calculate total content height
        max_width = LEFT_PANEL_WIDTH * 0.84
        total_height = 40  # Start with header height
        
        if not popup_text == "Erreur, element introuvable":
            for elmt in popup_text:
                for title, content in elmt.items():
                    total_height += 50  # Title height + spacing
                    if isinstance(content, dict):
                        for key, value in content.items():
                            if isinstance(value, str):
                                lines = self.render_text_multiline(value, self.font, self.WHITE, max_width)
                                total_height += len(lines) * 30 + 20
                            elif key == 'table':
                                table_rows = len(value)
                                total_height += table_rows * 60 + 20
                    else:
                        lines = self.render_text_multiline(content, self.font, self.WHITE, max_width)
                        total_height += len(lines) * 30 + 20
        
        # Limit scroll
        max_scroll = min(0, self.screen_h - total_height)
        scroll_y = max(max_scroll, min(0, scroll_y))
        
        # Draw content on content surface
        y_offset = 60 + scroll_y
        if not popup_text == "Erreur, element introuvable":
            for elmt in popup_text:
                for title, content in elmt.items():
                    # Title
                    title_surface = pg.Surface((LEFT_PANEL_WIDTH * 0.8, 40))
                    title_surface.fill(self.BLUE)
                    title_text = self.font.render(title, True, self.WHITE)
                    title_text_rect = title_text.get_rect(center=((LEFT_PANEL_WIDTH * 0.8)/2, 20))
                    title_surface.blit(title_text, title_text_rect)
                    content_surface.blit(title_surface, (LEFT_PANEL_WIDTH * 0.1, y_offset))
                    y_offset += 50

                    if isinstance(content, dict):
                        for key, value in content.items():
                            if isinstance(value, str):
                                lines = self.render_text_multiline(value, self.font, self.WHITE, max_width)
                                for line in lines:
                                    text_surface = self.font.render(line[1], True, self.WHITE)
                                    content_surface.blit(text_surface, (LEFT_PANEL_WIDTH * 0.08, y_offset))
                                    y_offset += 30
                            elif key == 'table':
                                table_surface = self.render_table(value, max_width)
                                content_surface.blit(table_surface, (LEFT_PANEL_WIDTH * 0.08, y_offset))
                                y_offset += table_surface.get_height()
                    else:
                        lines = self.render_text_multiline(content, self.font, self.WHITE, max_width)
                        for line in lines:
                            text_surface = self.font.render(line[1], True, self.WHITE)
                            content_surface.blit(text_surface, (LEFT_PANEL_WIDTH * 0.08, y_offset))
                            y_offset += 30
                    y_offset += 20
        else:
            error_surface = pg.Surface((LEFT_PANEL_WIDTH, self.screen_h - 40))
            error_surface.fill(self.RED)
            error_text = self.font.render("Erreur, element introuvable", True, self.WHITE)
            error_text_rect = error_text.get_rect(center=(LEFT_PANEL_WIDTH /2, (self.screen_h - 40)/2))
            error_surface.blit(error_text, error_text_rect)
            content_surface.blit(error_surface, (0, 40))
        
        # Draw scrolled content
        popup_surface.blit(content_surface, (0, 0))
        
        # Draw fixed header
        header_surface = pg.Surface((LEFT_PANEL_WIDTH, 40))
        header_surface.fill(self.BLUE)
        header_text = self.font.render(self.popup_text_show, True, self.WHITE)
        header_text_rect = header_text.get_rect(topleft=(10, 12))
        header_surface.blit(header_text, header_text_rect)
        popup_surface.blit(header_surface, (0, 0))
        
        return popup_surface, scroll_y



    def niveau_1(self):
        # Constants for layout
        LEFT_PANEL_WIDTH = self.screen_w * 0.4
        RIGHT_PANEL_WIDTH = self.screen_w * 0.6
        CONSOLE_HEIGHT = self.screen_h * 0.3
        EDITOR_HEIGHT = self.screen_h - CONSOLE_HEIGHT

        mos_pos = pg.mouse.get_pos()
        
        # Colors for syntax highlighting (customizable)
        self.syntax_colors = {
            'keywords': (86, 156, 214),    # blue
            'strings': (206, 145, 120),    # orange
            'comments': (87, 166, 74),     # green
            'numbers': (181, 206, 168),    # light green
            'background': (30, 30, 30),    # dark gray
            'text': (212, 212, 212)        # light gray
        }

        for event in self.events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if not self.popup_text_show and not self.shown_popup:
                        self.mode = "menu"
                    else:
                        self.popup_closing = True


        # Clear screen
        self.screen.fill(self.BLACK)

        # Draw left panel
        left_panel = pg.Surface((LEFT_PANEL_WIDTH, self.screen_h))
        left_panel.fill((40, 40, 40))
        
        # Instructions area
        instructions = [
            "Consignes:",
            "1. Écrivez une fonction qui...",
            "2. Utilisez les variables...",
            "3. Affichez le résultat...",
            "",
            "Conseils:",
            "- Pensez à initialiser...",
            "- N'oubliez pas de..."
        ]
        
        for i, line in enumerate(instructions):
            text = self.font.render(line, True, self.WHITE)
            left_panel.blit(text, (20, 20 + i * 30))

        # Buttons at bottom of left panel
        buttons = [
           ("Notions de base", (self.screen_w * 0.02, self.screen_h * 0.5), "Notions essentielles pour débuter"),
            ("Variable", (self.screen_w * 0.02, self.screen_h * 0.6), "Garder des informations en mémoire"),
            ("Conditionnelle", (self.screen_w * 0.02, self.screen_h * 0.7), "Exécuter selon certains conditions"),
            ("Boucle for", (self.screen_w * 0.02, self.screen_h * 0.8), "Répéter un certain nombre de fois"),
            ("Boucle while", (self.screen_w * 0.02, self.screen_h * 0.9), "Répéter selon une condition")
        ]

        for text, pos, alt_text in buttons:

            hover = pos[0] + (LEFT_PANEL_WIDTH - pos[0]*2) > mos_pos[0] > pos[0] and pos[1] + 40 > mos_pos[1] > pos[1]

            button_surface = pg.Surface((LEFT_PANEL_WIDTH - pos[0]*2, 40))
            button_surface.fill(self.BLUE if not hover else self.DARK_BLUE)

            text_surface = self.font.render(alt_text, True, self.WHITE) if hover else self.font.render(text, True, self.WHITE)

            text_rect = text_surface.get_rect(center=((LEFT_PANEL_WIDTH - pos[0]*2)/2, 20))
            button_surface.blit(text_surface, text_rect)
            left_panel.blit(button_surface, pos)

            if hover and pg.mouse.get_pressed()[0] and not self.shown_popup and not self.popup_text_show:
                self.shown_popup = True
                self.popup_text_show = text
                self.scroll_y = 0         

        # Draw right panel
        right_panel = pg.Surface((RIGHT_PANEL_WIDTH, self.screen_h))
        right_panel.fill((30, 30, 30))

        # Code editor area
        editor_surface = pg.Surface((RIGHT_PANEL_WIDTH - 20, EDITOR_HEIGHT - 60))
        editor_surface.fill(self.syntax_colors['background'])
        
        # Play controls
        play_button = pg.Surface((40, 40))
        play_button.fill(self.GREEN)
        pg.draw.polygon(play_button, self.WHITE, [(10, 10), (30, 20), (10, 30)])
        
        # Speed slider
        slider_surface = pg.Surface((200, 10))
        slider_surface.fill(self.GRAY)
        
        # Console/Output area
        console_surface = pg.Surface((RIGHT_PANEL_WIDTH - 20, CONSOLE_HEIGHT - 20))
        console_surface.fill((20, 20, 20))
        
        # Variable trace table
        table_headers = ["Variable", "Type", "Valeur"]
        table_surface = pg.Surface((RIGHT_PANEL_WIDTH - 40, CONSOLE_HEIGHT - 60))
        table_surface.fill((50, 50, 50))
        
        for i, header in enumerate(table_headers):
            header_text = self.font.render(header, True, self.WHITE)
            table_surface.blit(header_text, (20 + i * (RIGHT_PANEL_WIDTH - 40) // 3, 10))

        # Add components to right panel
        right_panel.blit(editor_surface, (10, 10))
        right_panel.blit(play_button, (10, EDITOR_HEIGHT - 50))
        right_panel.blit(slider_surface, (60, EDITOR_HEIGHT - 45))
        right_panel.blit(console_surface, (10, EDITOR_HEIGHT))
        right_panel.blit(table_surface, (20, EDITOR_HEIGHT + 40))

        # Add panels to main screen
        self.screen.blit(left_panel, (0, 0))
        self.screen.blit(right_panel, (LEFT_PANEL_WIDTH, 0))

        if self.shown_popup and self.popup_text_show:
            for event in self.events:
                if event.type == pg.MOUSEWHEEL:
                    self.scroll_y += event.y * 30

            popup_text = self.dict_elements.get(self.popup_text_show, "Erreur, element introuvable")
            popup_surface, self.scroll_y = self.draw_scrollable_popup(popup_text, self.scroll_y)     

            if self.popup_closing:
                self.popup_x -= self.slide_speed
                if self.popup_x <= -self.screen_w * 0.4:
                    self.popup_x = -self.screen_w * 0.4
                    self.shown_popup = False
                    self.popup_text_show = False
                    self.popup_closing = False
            else:
                if self.popup_x < self.target_x:
                    self.popup_x += self.slide_speed
                    if self.popup_x > self.target_x:
                        self.popup_x = self.target_x
            
            self.screen.blit(popup_surface, (self.popup_x, 0))
        else:
            self.popup_x = -self.screen_w * 0.4



        # Draw separator
        pg.draw.line(self.screen, self.WHITE, (LEFT_PANEL_WIDTH, 0), (LEFT_PANEL_WIDTH, self.screen_h), 2)

    def niveau_2(self):
        # Constants for layout
        LEFT_PANEL_WIDTH = self.screen_w * 0.4
        RIGHT_PANEL_WIDTH = self.screen_w * 0.6
        CONSOLE_HEIGHT = self.screen_h * 0.3
        EDITOR_HEIGHT = self.screen_h - CONSOLE_HEIGHT
        
        # Colors for syntax highlighting (customizable)
        self.syntax_colors = {
            'keywords': (86, 156, 214),    # blue
            'strings': (206, 145, 120),    # orange
            'comments': (87, 166, 74),     # green
            'numbers': (181, 206, 168),    # light green
            'background': (30, 30, 30),    # dark gray
            'text': (212, 212, 212)        # light gray
        }

        for event in self.events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.mode = "menu"

        # Clear screen
        self.screen.fill(self.BLACK)

        # Draw left panel
        left_panel = pg.Surface((LEFT_PANEL_WIDTH, self.screen_h))
        left_panel.fill((40, 40, 40))
        
        # Instructions area
        instructions = [
            "Consignes:",
            "1. Écrivez une fonction qui...",
            "2. Utilisez les variables...",
            "3. Affichez le résultat...",
            "",
            "Conseils:",
            "- Pensez à initialiser...",
            "- N'oubliez pas de..."
        ]
        
        for i, line in enumerate(instructions):
            text = self.font.render(line, True, self.WHITE)
            left_panel.blit(text, (20, 20 + i * 30))

        # Buttons at bottom of left panel
        buttons = [
            ("Notions de base", (20, self.screen_h - 150), "Notions essentielles pour débuter"),
            ("Variable", (150, self.screen_h - 150), "Garder des informations en mémoire"),
            ("Conditionelle", (280, self.screen_h - 150), "Exécuter selon certains conditions"),
            ("Boucle for", (410, self.screen_h - 150), "Répéter un certain nombre de fois"),
            ("Boucle while", (540, self.screen_h - 150), "Répéter selon une condition")
        ]

        for text, pos, alt_text in buttons:
            button_surface = pg.Surface((100, 40))
            button_surface.fill(self.GRAY)
            text_surface = self.font.render(text, True, self.BLACK)
            text_rect = text_surface.get_rect(center=(50, 20))
            button_surface.blit(text_surface, text_rect)
            left_panel.blit(button_surface, pos)

        # Draw right panel
        right_panel = pg.Surface((RIGHT_PANEL_WIDTH, self.screen_h))
        right_panel.fill((30, 30, 30))

        # Code editor area
        editor_surface = pg.Surface((RIGHT_PANEL_WIDTH - 20, EDITOR_HEIGHT - 60))
        editor_surface.fill(self.syntax_colors['background'])
        
        # Play controls
        play_button = pg.Surface((40, 40))
        play_button.fill(self.GREEN)
        pg.draw.polygon(play_button, self.WHITE, [(10, 10), (30, 20), (10, 30)])
        
        # Speed slider
        slider_surface = pg.Surface((200, 10))
        slider_surface.fill(self.GRAY)
        
        # Console/Output area
        console_surface = pg.Surface((RIGHT_PANEL_WIDTH - 20, CONSOLE_HEIGHT - 20))
        console_surface.fill((20, 20, 20))
        
        # Variable trace table
        table_headers = ["Variable", "Type", "Valeur"]
        table_surface = pg.Surface((RIGHT_PANEL_WIDTH - 40, CONSOLE_HEIGHT - 60))
        table_surface.fill((50, 50, 50))
        
        for i, header in enumerate(table_headers):
            header_text = self.font.render(header, True, self.WHITE)
            table_surface.blit(header_text, (20 + i * (RIGHT_PANEL_WIDTH - 40) // 3, 10))

        # Add components to right panel
        right_panel.blit(editor_surface, (10, 10))
        right_panel.blit(play_button, (10, EDITOR_HEIGHT - 50))
        right_panel.blit(slider_surface, (60, EDITOR_HEIGHT - 45))
        right_panel.blit(console_surface, (10, EDITOR_HEIGHT))
        right_panel.blit(table_surface, (20, EDITOR_HEIGHT + 40))

        # Add panels to main screen
        self.screen.blit(left_panel, (0, 0))
        self.screen.blit(right_panel, (LEFT_PANEL_WIDTH, 0))

        # Draw separator
        pg.draw.line(self.screen, self.WHITE, (LEFT_PANEL_WIDTH, 0), (LEFT_PANEL_WIDTH, self.screen_h), 2)

    def niveau_3(self):
        # Constants for layout
        LEFT_PANEL_WIDTH = self.screen_w * 0.4
        RIGHT_PANEL_WIDTH = self.screen_w * 0.6
        CONSOLE_HEIGHT = self.screen_h * 0.3
        EDITOR_HEIGHT = self.screen_h - CONSOLE_HEIGHT
        
        # Colors for syntax highlighting (customizable)
        self.syntax_colors = {
            'keywords': (86, 156, 214),    # blue
            'strings': (206, 145, 120),    # orange
            'comments': (87, 166, 74),     # green
            'numbers': (181, 206, 168),    # light green
            'background': (30, 30, 30),    # dark gray
            'text': (212, 212, 212)        # light gray
        }

        for event in self.events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.mode = "menu"

        # Clear screen
        self.screen.fill(self.BLACK)

        # Draw left panel
        left_panel = pg.Surface((LEFT_PANEL_WIDTH, self.screen_h))
        left_panel.fill((40, 40, 40))
        
        # Instructions area
        instructions = [
            "Consignes:",
            "1. Écrivez une fonction qui...",
            "2. Utilisez les variables...",
            "3. Affichez le résultat...",
            "",
            "Conseils:",
            "- Pensez à initialiser...",
            "- N'oubliez pas de..."
        ]
        
        for i, line in enumerate(instructions):
            text = self.font.render(line, True, self.WHITE)
            left_panel.blit(text, (20, 20 + i * 30))

        # Buttons at bottom of left panel
        buttons = [
            ("Notions de base", (20, self.screen_h - 150), "Notions essentielles pour débuter"),
            ("Variable", (150, self.screen_h - 150), "Garder des informations en mémoire"),
            ("Conditionelle", (280, self.screen_h - 150), "Exécuter selon certains conditions"),
            ("Boucle for", (410, self.screen_h - 150), "Répéter un certain nombre de fois"),
            ("Boucle while", (540, self.screen_h - 150), "Répéter selon une condition")
        ]

        for text, pos, alt_text in buttons:
            button_surface = pg.Surface((100, 40))
            button_surface.fill(self.GRAY)
            text_surface = self.font.render(text, True, self.BLACK)
            text_rect = text_surface.get_rect(center=(50, 20))
            button_surface.blit(text_surface, text_rect)
            left_panel.blit(button_surface, pos)

        # Draw right panel
        right_panel = pg.Surface((RIGHT_PANEL_WIDTH, self.screen_h))
        right_panel.fill((30, 30, 30))

        # Code editor area
        editor_surface = pg.Surface((RIGHT_PANEL_WIDTH - 20, EDITOR_HEIGHT - 60))
        editor_surface.fill(self.syntax_colors['background'])
        
        # Play controls
        play_button = pg.Surface((40, 40))
        play_button.fill(self.GREEN)
        pg.draw.polygon(play_button, self.WHITE, [(10, 10), (30, 20), (10, 30)])
        
        # Speed slider
        slider_surface = pg.Surface((200, 10))
        slider_surface.fill(self.GRAY)
        
        # Console/Output area
        console_surface = pg.Surface((RIGHT_PANEL_WIDTH - 20, CONSOLE_HEIGHT - 20))
        console_surface.fill((20, 20, 20))
        
        # Variable trace table
        table_headers = ["Variable", "Type", "Valeur"]
        table_surface = pg.Surface((RIGHT_PANEL_WIDTH - 40, CONSOLE_HEIGHT - 60))
        table_surface.fill((50, 50, 50))
        
        for i, header in enumerate(table_headers):
            header_text = self.font.render(header, True, self.WHITE)
            table_surface.blit(header_text, (20 + i * (RIGHT_PANEL_WIDTH - 40) // 3, 10))

        # Add components to right panel
        right_panel.blit(editor_surface, (10, 10))
        right_panel.blit(play_button, (10, EDITOR_HEIGHT - 50))
        right_panel.blit(slider_surface, (60, EDITOR_HEIGHT - 45))
        right_panel.blit(console_surface, (10, EDITOR_HEIGHT))
        right_panel.blit(table_surface, (20, EDITOR_HEIGHT + 40))

        # Add panels to main screen
        self.screen.blit(left_panel, (0, 0))
        self.screen.blit(right_panel, (LEFT_PANEL_WIDTH, 0))

        # Draw separator
        pg.draw.line(self.screen, self.WHITE, (LEFT_PANEL_WIDTH, 0), (LEFT_PANEL_WIDTH, self.screen_h), 2)

    def niveau_4(self):
        # Constants for layout
        LEFT_PANEL_WIDTH = self.screen_w * 0.4
        RIGHT_PANEL_WIDTH = self.screen_w * 0.6
        CONSOLE_HEIGHT = self.screen_h * 0.3
        EDITOR_HEIGHT = self.screen_h - CONSOLE_HEIGHT
        
        # Colors for syntax highlighting (customizable)
        self.syntax_colors = {
            'keywords': (86, 156, 214),    # blue
            'strings': (206, 145, 120),    # orange
            'comments': (87, 166, 74),     # green
            'numbers': (181, 206, 168),    # light green
            'background': (30, 30, 30),    # dark gray
            'text': (212, 212, 212)        # light gray
        }

        for event in self.events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.mode = "menu"

        # Clear screen
        self.screen.fill(self.BLACK)

        # Draw left panel
        left_panel = pg.Surface((LEFT_PANEL_WIDTH, self.screen_h))
        left_panel.fill((40, 40, 40))
        
        # Instructions area
        instructions = [
            "Consignes:",
            "1. Écrivez une fonction qui...",
            "2. Utilisez les variables...",
            "3. Affichez le résultat...",
            "",
            "Conseils:",
            "- Pensez à initialiser...",
            "- N'oubliez pas de..."
        ]
        
        for i, line in enumerate(instructions):
            text = self.font.render(line, True, self.WHITE)
            left_panel.blit(text, (20, 20 + i * 30))

        # Buttons at bottom of left panel
        buttons = [
            ("Notions de base", (20, self.screen_h - 150), "Notions essentielles pour débuter"),
            ("Variable", (150, self.screen_h - 150), "Garder des informations en mémoire"),
            ("Conditionelle", (280, self.screen_h - 150), "Exécuter selon certains conditions"),
            ("Boucle for", (410, self.screen_h - 150), "Répéter un certain nombre de fois"),
            ("Boucle while", (540, self.screen_h - 150), "Répéter selon une condition")
        ]

        for text, pos, alt_text in buttons:
            button_surface = pg.Surface((100, 40))
            button_surface.fill(self.GRAY)
            text_surface = self.font.render(text, True, self.BLACK)
            text_rect = text_surface.get_rect(center=(50, 20))
            button_surface.blit(text_surface, text_rect)
            left_panel.blit(button_surface, pos)

        # Draw right panel
        right_panel = pg.Surface((RIGHT_PANEL_WIDTH, self.screen_h))
        right_panel.fill((30, 30, 30))

        # Code editor area
        editor_surface = pg.Surface((RIGHT_PANEL_WIDTH - 20, EDITOR_HEIGHT - 60))
        editor_surface.fill(self.syntax_colors['background'])
        
        # Play controls
        play_button = pg.Surface((40, 40))
        play_button.fill(self.GREEN)
        pg.draw.polygon(play_button, self.WHITE, [(10, 10), (30, 20), (10, 30)])
        
        # Speed slider
        slider_surface = pg.Surface((200, 10))
        slider_surface.fill(self.GRAY)
        
        # Console/Output area
        console_surface = pg.Surface((RIGHT_PANEL_WIDTH - 20, CONSOLE_HEIGHT - 20))
        console_surface.fill((20, 20, 20))
        
        # Variable trace table
        table_headers = ["Variable", "Type", "Valeur"]
        table_surface = pg.Surface((RIGHT_PANEL_WIDTH - 40, CONSOLE_HEIGHT - 60))
        table_surface.fill((50, 50, 50))
        
        for i, header in enumerate(table_headers):
            header_text = self.font.render(header, True, self.WHITE)
            table_surface.blit(header_text, (20 + i * (RIGHT_PANEL_WIDTH - 40) // 3, 10))

        # Add components to right panel
        right_panel.blit(editor_surface, (10, 10))
        right_panel.blit(play_button, (10, EDITOR_HEIGHT - 50))
        right_panel.blit(slider_surface, (60, EDITOR_HEIGHT - 45))
        right_panel.blit(console_surface, (10, EDITOR_HEIGHT))
        right_panel.blit(table_surface, (20, EDITOR_HEIGHT + 40))

        # Add panels to main screen
        self.screen.blit(left_panel, (0, 0))
        self.screen.blit(right_panel, (LEFT_PANEL_WIDTH, 0))

        # Draw separator
        pg.draw.line(self.screen, self.WHITE, (LEFT_PANEL_WIDTH, 0), (LEFT_PANEL_WIDTH, self.screen_h), 2)

    def niveau_5(self):
        # Constants for layout
        LEFT_PANEL_WIDTH = self.screen_w * 0.4
        RIGHT_PANEL_WIDTH = self.screen_w * 0.6
        CONSOLE_HEIGHT = self.screen_h * 0.3
        EDITOR_HEIGHT = self.screen_h - CONSOLE_HEIGHT
        
        # Colors for syntax highlighting (customizable)
        self.syntax_colors = {
            'keywords': (86, 156, 214),    # blue
            'strings': (206, 145, 120),    # orange
            'comments': (87, 166, 74),     # green
            'numbers': (181, 206, 168),    # light green
            'background': (30, 30, 30),    # dark gray
            'text': (212, 212, 212)        # light gray
        }

        for event in self.events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.mode = "menu"

        # Clear screen
        self.screen.fill(self.BLACK)

        # Draw left panel
        left_panel = pg.Surface((LEFT_PANEL_WIDTH, self.screen_h))
        left_panel.fill((40, 40, 40))
        
        # Instructions area
        instructions = [
            "Consignes:",
            "1. Écrivez une fonction qui...",
            "2. Utilisez les variables...",
            "3. Affichez le résultat...",
            "",
            "Conseils:",
            "- Pensez à initialiser...",
            "- N'oubliez pas de..."
        ]
        
        for i, line in enumerate(instructions):
            text = self.font.render(line, True, self.WHITE)
            left_panel.blit(text, (20, 20 + i * 30))

        # Buttons at bottom of left panel
        buttons = [
            ("Notions de base", (20, self.screen_h - 150), "Notions essentielles pour débuter"),
            ("Variable", (150, self.screen_h - 150), "Garder des informations en mémoire"),
            ("Conditionelle", (280, self.screen_h - 150), "Exécuter selon certains conditions"),
            ("Boucle for", (410, self.screen_h - 150), "Répéter un certain nombre de fois"),
            ("Boucle while", (540, self.screen_h - 150), "Répéter selon une condition")
        ]

        for text, pos, alt_text in buttons:
            button_surface = pg.Surface((100, 40))
            button_surface.fill(self.GRAY)
            text_surface = self.font.render(text, True, self.BLACK)
            text_rect = text_surface.get_rect(center=(50, 20))
            button_surface.blit(text_surface, text_rect)
            left_panel.blit(button_surface, pos)

        # Draw right panel
        right_panel = pg.Surface((RIGHT_PANEL_WIDTH, self.screen_h))
        right_panel.fill((30, 30, 30))

        # Code editor area
        editor_surface = pg.Surface((RIGHT_PANEL_WIDTH - 20, EDITOR_HEIGHT - 60))
        editor_surface.fill(self.syntax_colors['background'])
        
        # Play controls
        play_button = pg.Surface((40, 40))
        play_button.fill(self.GREEN)
        pg.draw.polygon(play_button, self.WHITE, [(10, 10), (30, 20), (10, 30)])
        
        # Speed slider
        slider_surface = pg.Surface((200, 10))
        slider_surface.fill(self.GRAY)
        
        # Console/Output area
        console_surface = pg.Surface((RIGHT_PANEL_WIDTH - 20, CONSOLE_HEIGHT - 20))
        console_surface.fill((20, 20, 20))
        
        # Variable trace table
        table_headers = ["Variable", "Type", "Valeur"]
        table_surface = pg.Surface((RIGHT_PANEL_WIDTH - 40, CONSOLE_HEIGHT - 60))
        table_surface.fill((50, 50, 50))
        
        for i, header in enumerate(table_headers):
            header_text = self.font.render(header, True, self.WHITE)
            table_surface.blit(header_text, (20 + i * (RIGHT_PANEL_WIDTH - 40) // 3, 10))

        # Add components to right panel
        right_panel.blit(editor_surface, (10, 10))
        right_panel.blit(play_button, (10, EDITOR_HEIGHT - 50))
        right_panel.blit(slider_surface, (60, EDITOR_HEIGHT - 45))
        right_panel.blit(console_surface, (10, EDITOR_HEIGHT))
        right_panel.blit(table_surface, (20, EDITOR_HEIGHT + 40))

        # Add panels to main screen
        self.screen.blit(left_panel, (0, 0))
        self.screen.blit(right_panel, (LEFT_PANEL_WIDTH, 0))

        # Draw separator
        pg.draw.line(self.screen, self.WHITE, (LEFT_PANEL_WIDTH, 0), (LEFT_PANEL_WIDTH, self.screen_h), 2)   


    def exit(self):
        self.video.release()
        self.running = False
        pg.quit()
        os._exit(0)


if __name__ == "__main__":
    app = App()
