# type: ignore[import]
# pyright: ignore[import]
# pylint: disable=import-error
# ruff: noqa: F401, E402
# mypy: ignore-errors
# flake8: noqa: F401

import subprocess
import sys

def util():
    for i in ["pkg_resources", "packaging", "requests"]:
        try:
            __import__(i)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", i]) if not i=="pkg_resources" else subprocess.check_call([sys.executable, "-m", "pip", "install", "setuptools"])
        
util()

import pkg_resources
import requests
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
                        ('random', True, False),
                        ('tkinter.filedialog', True, False),
                        ("numpy", True, 'np')
                        )
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
    install_and_import(('pygame', True, "pg"),
                        )
except:
    subprocess.run(["itmgr", "add", "opencv-python", "cv2"])
    install_and_import(('os', True, False),
                        ('sqlite3', True, "sql"),
                        ('cv2', True, False),
                        ('random', True, False),
                        ('tkinter.filedialog', True, False),
                        ("numpy", True, 'np')
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
        self.DARK_GREEN = (0, 128, 0)
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

        #----------------------- Easter egg ------------------------------------#
        self.click_sequence = []
        self.last_click_time = 0
        self.recipe_shown = False
        self.will_test_recipe = False
        self.recipe_scroll = 0
        self.text_angle = 0
        self.text_scale = 1.0
        self.text_direction = 1
        self.affiche = False
        self.mirror = False
        self.recipe_text = """CRUMBLE SALÉ AUX DEUX PATATES

    Temps de préparation : 20 minutes
    Temps de cuisson : 30 minutes
    Temps total : 50 minutes

    Pour 4 personnes :

    Ingrédients:

    - 2 patates douces
    - 1 pommes de terre
    - 15 cl de crème liquide ou semi-épaisse, ou 15cl de lait de coco
    - 1 oignon jaune
    - Sel
    - Paprika
    - Herbes de provence
    - Poivre
    - Muscade
    - Cumin
    - 2 Cuillères à soupe d'huile d'olive
    - 50 grammes de parmesan ( râpé )
    - 50 grammes de farine
    - 50 grammes de beurre

    Préparation:

    1. Préchauffer le four à 210°C

    2.  Éplucher et couper vos patates et patates douces en gros dés, et les faire cuire 5 minutes à l'eau bouillante salée.

    3. Pendant ce temps, émincer votre oignon et le faire dorer dans une grande poêle avec un peu d'huile d'olive

    4. Y ajouter ensuite les dés de patate et patate douce égouttés.

    5. Laisser mijoter à feu moyen doux, en remuant régulièrement, et assaisonner généreusement.

    6. Quand les légumes deviennent fondants (ils s'écrasent presque), couper le feu, ajouter la crème et mélanger.

    6. Pendant ce temps, mélanger du bout des doigts le beurre, la farine et le parmesan de sorte à obtenir une pâte à crumble.

    7. Beurrer un plat allant au four, y ajouter vos légumes, et disposer la pâte à crumble par dessus.

    8. Enfourner pour 12/15 minutes, puis 3 minutes en position grill.

    Bon appétit !"""

        #----------------------------------------------------------#

        #------------------ Crédits ------------------#
        self.credits_text = """
2METHYLBUTAN2OL-SERPENTES (Bases de Python)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EQUIPE DE DEVELOPPEMENT

Développeurs Principaux
• Enzo DUCCESCHI (Cassssian)
• Yaniss DUTHE

Design & Programmation
• Enzo DUCCESCHI (Cassssian)

Idée & Conception
• Enzo DUCCESCHI (Cassssian)
• Yaniss DUTHE

Sound Design & Composition musicales
• Enzo DUCCESCHI (Cassssian)
• Youtube

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

REMERCIMENTS SPECIAUX

Lycée Charles De Gaulle
Ingénieur de ITMGR (Cassssian)

Administration du Lycée Charles De Gaulle
Et surtout à M. LEBEL
sans qui cela n'aurait jamais pu se faire

Logiciels utilisés
Python Programming Language
Pygame Framework & Community
OS Library
Setuptools
Requests Library
Packaging Distribution Library
Subprocess Library
Sys Library
ITMGR Implementation
Tkinter GUI
SQLite3 Database
CV2 Image Processing
OpenCV Image Processing
Random Library
NumPy Library

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Une application créée avec coeur par

Enzo DUCCESCHI (Cassssian) & Yaniss DUTHE
Version 1.0

© 2024 Tout droit réservé.
Equipe de 2Methylbutan2ol-Serpentes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        #----------------------------------------------------------#


        #------------------ Texte pour les aides ------------------#
        self.dict_elements = {
            "Notions de base": [

                {"Utilité" : {
                        "text1" : "Quelques notions essentielles qui permettent de débuter la programmation en Python."}},
         
                {"Programme" : {
                    "text1" : "Un programme est un texte qui permet de commander un ordinateur. Dans notre cas, il s'agit de créer du code afin des fins spécifiques. Ce texte est composé d'instructions compréhensibles par l'ordinateur. Certaines sont spécifiques à des programmes et permettent de contrôler les instructions sur l'ordinateur (instruction additionner() par exemple), d'autres sont communes à tous les programmes en Python (voir la suite du mémo programmation). Une fois rédigé, le programme est exécuté par un interpréteur."}},

                {"Erreurs" : {
                    "text1" : "Les instructions d'un programme doivent être très précises et ne comporter aucune erreur, attention aux fautes de frappe ! En cas d'erreur, l'interpréteur signale un problème dans la console. Par exemple, la ligne de code erronée addition() provoque l'affichage d'une erreur :\n<error>> Ligne 1 : le nom 'addition()' n'est pas défini</error>\n\nIl faudra donc modifier le programme à partir de ce message d'erreur, puis relancer l'exécution jusqu'à ce que le programme soit correct."}},
        
                {"Structuration" : {
                    "text1" : "Un programme doit être structuré par des décalages de texte lors de l'utilisation de certaines instructions (if, while, for, etc.). On appelle cela l'indentation du code. Si l'indentation est mauvaise, le programme ne réalise pas ce que l'on veut et cela peut même provoquer des erreurs. Ces décalages s'effectuent avec la touche tabulation du clavier. A noter que l'éditeur de programme ajoute automatiquement des décalages lors de l'utilisation de certaines instructions."}},
        
                {"Commentaires" : {
                    "text1" : "Les lignes commençant par # ne sont pas prises en compte par l'interpréteur. Par exemple, la ligne de code <bold># Ceci est un commentaire</bold> n'a aucun effet. Ces lignes permettent de donner des explications dans le programme, on les appelle des commentaires. Les commentaires ne sont pas obligatoires mais ils peuvent aider à la compréhension des programmes par les autres programmeurs."}}
                ],

            "Variable": [
                {"Utilité" : {
                    "text1" : "Permet de garder en mémoire des informations au cours de l’exécution d'un programme."}},
                 
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
                ],

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
            
            elif self.mode == "answer":
                self.answer()

            elif self.mode == "exit":
                self.exit()

            pg.display.update()
            pg.display.flip()
            self.clock.tick(60)

    def credits(self):

        choix_list = ['Funky town low quality + _bassboosted_', 'Cucaracha', 'funky town low quality', 'Firewhole - maxwell, our beloved', 'maxwell']

        choix = random.randint(0, len(choix_list)-1)

        pg.mixer.music.load(f'./music/{choix_list[choix]}.mp3')

        # Split the text into lines
        credit_lines = self.credits_text.split('\n')
        scroll_speed = 2
        
        # Font settings
        font = pg.font.Font(None, 36)
        
        # Calculate total height of all text
        line_height = 40
        total_height = len(credit_lines) * line_height
        
        # Starting position (below screen)
        y_pos = self.screen.get_height() + 100
        
        # Create a surface for the entire credits
        credits_surface = pg.Surface((self.screen.get_width(), total_height), pg.SRCALPHA)
        
        try:
            frog_img = pg.image.load('./img/frog.png')
        except:
            frog_img = None
            
            # Add frog next to Cassssian
            if "Cassssian" in line and frog_img:
                # Scale frog to match font height
                frog_height = font.get_height()
                frog_scaled = pg.transform.scale(frog_img, (frog_height, frog_height))
                # Position frog after the text
                frog_pos = (text_rect.right + 10, text_rect.centery - frog_height//2)
                credits_surface.blit(frog_scaled, frog_pos)


        
        # Scroll position
        scroll_y = 0
        
        boucle = True

        video_credits = cv2.VideoCapture(f"./video/{choix_list[choix]}.mp4")
        pg.mixer.music.play(-1)

        while boucle:
            self.events = pg.event.get()

            ret, frame = video_credits.read()
            if not ret:
                video_credits.set(cv2.CAP_PROP_POS_FRAMES, 0)
                ret, frame = video_credits.read()

            frame = cv2.resize(frame, (self.screen_w, self.screen_h))

            center_y, center_x = frame.shape[0]//2, frame.shape[1]//2
            center_region = frame[center_y-5:center_y+5, center_x-5:center_x+5]
            avg_color = np.mean(center_region, axis=(0,1))
            
            # Create opposite color (255 - color)
            opposite_color = (255 - avg_color[2], 255 - avg_color[1], 255 - avg_color[0])


            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_surface = pg.surfarray.make_surface(frame)
            self.screen.blit(pg.transform.rotate(frame_surface, -90), (0, 0))

            # In the text rendering loop
            for i, line in enumerate(credit_lines):
                text_surface = font.render(line, True, opposite_color)
                text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, i * line_height))
                credits_surface.blit(text_surface, text_rect)
            
            # Draw the visible portion of credits
            self.screen.blit(credits_surface, (0, y_pos - scroll_y))
            
            # Update scroll position
            scroll_y += scroll_speed
            
            # Reset scroll when all text has scrolled
            if scroll_y > total_height + self.screen.get_height():
                scroll_y = 0
            
            pg.display.flip()

            for event in self.events:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        video_credits.release()
                        pg.mixer.music.stop()
                        self.mode = "menu"
                        boucle = False


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
            ("Réponse", "answer", self.screen_h // 2 + 55, self.GRAY),
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
                        lines.append(('bullet', '•', indent - 25)) if not ('bullet', '•', indent - 25) in lines else None
                    elif in_dash:
                        lines.append(('bullet', '-', indent - 25)) if not ('bullet', '-', indent - 25) in lines else None
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
            print(lines)
                
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
                                    if line[0] == 'surface':
                                        content_surface.blit(line[1], (LEFT_PANEL_WIDTH * 0.08, y_offset))
                                        y_offset += line[1].get_height()
                                    else:
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


    def answer(self):
        import math
        
        # Initialize angle for circular motion if not exists
        if not hasattr(self, 'circle_angle'):
            self.circle_angle = 0
        
        # Radius for circular motion (30% of screen width)
        radius = min(self.screen_w, self.screen_h) * 0.4
        
        # Center of the screen
        center_x = self.screen_w // 2
        center_y = self.screen_h // 2
        
        # Update angle
        self.circle_angle += 0.02
        
        # Calculate positions
        python_x = center_x + radius * math.cos(self.circle_angle)
        python_y = center_y + radius * math.sin(self.circle_angle)
        
        # Opposite position for images.png
        images_x = center_x + radius * math.cos(self.circle_angle + math.pi)
        images_y = center_y + radius * math.sin(self.circle_angle + math.pi)

        self.screen.fill(self.TEAL)
        
        if not self.recipe_shown:

            self.text_angle += 2 * self.text_direction
            self.text_scale = 1.0 + math.sin(pg.time.get_ticks() / 500) * 0.5

            if pg.time.get_ticks() % 60 == 0:
                self.text_direction = random.choice([-1, 1])
                self.mirror = random.choice([True, False])

            # Main text
            text = self.font.render("T'as cru quoi ?", True, self.WHITE)
            text = pg.transform.scale(text, (int(text.get_width() * self.text_scale), int(text.get_height() * self.text_scale)))
            if self.mirror:
                text = pg.transform.flip(text, True, False)
            text = pg.transform.rotate(text, self.text_angle)
            self.text_rect = text.get_rect(center=(center_x, center_y))
            self.screen.blit(text, self.text_rect)
            
            # # Python GIF
            # ret, frame = self.video.read()
            # if not ret:
            #     self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            #     ret, frame = self.video.read()
            
            # frame = cv2.resize(frame, (100, 100))
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # frame_surface = pg.surfarray.make_surface(frame)
            # frame_rect = frame_surface.get_rect(center=(python_x, python_y))
            # self.screen.blit(pg.transform.rotate(frame_surface, -90), frame_rect)

            # Images.png with random rotation
            try:
                img = pg.image.load('./img/yaniss.jpg').convert_alpha()  # Added convert_alpha()
                img = pg.transform.scale(img, (400, 150))
                img = pg.transform.rotate(img, self.circle_angle * 30)
                self.img_rect = img.get_rect(center=(python_x, python_y))
                self.screen.blit(img, self.img_rect)
            except:
                print("Image not found")
            
            # Images.png with random rotation
            try:
                img = pg.image.load('./img/enzo.jpg').convert_alpha()  # Added convert_alpha()
                img = pg.transform.scale(img, (400, 150))
                img = pg.transform.rotate(img, self.circle_angle * 30)
                self.img_rect2 = img.get_rect(center=(images_x, images_y))
                self.screen.blit(pg.transform.rotate(img, -90), self.img_rect2)
            except:
                print("Image not found")
        
        else:
            # Draw recipe
            self.screen.fill(self.BLACK)
            
            # Create recipe surface
            recipe_font = pg.font.Font(None, 28)
            recipe_lines = self.recipe_text.split('\n')
            
            total_height = len(recipe_lines) * 35
            recipe_surface = pg.Surface((self.screen_w - 100, total_height))
            recipe_surface.fill(self.BLACK)
            
            y = 0
            for line in recipe_lines:
                if line.startswith(('Ingrédients:', 'Préparation:', 'CRUMBLE')):
                    color = self.YELLOW
                else:
                    color = self.WHITE
                text = recipe_font.render(line, True, color)
                recipe_surface.blit(text, (10, y))
                y += 35
            
            # Calculate visible portion
            visible_height = self.screen_h - 100
            self.recipe_scroll = min(0, max(-(total_height - visible_height), self.recipe_scroll))

            try:
                crumble_img = pg.image.load('./img/crumble.jpg').convert_alpha()
                crumble_img = pg.transform.scale(crumble_img, (400, 200))  # Adjust size as needed
                recipe_surface.blit(crumble_img, (recipe_surface.get_width() - 420, 10))  # Position in top right with 20px padding
            except:
                print("Crumble image not found")


            crumble_rect = crumble_img.get_rect()
            crumble_rect.topleft = (recipe_surface.get_width() - 420, 10) # Add the actual position coordinates
            if crumble_rect.collidepoint(pg.mouse.get_pos()) and self.affiche:
                if pg.mouse.get_pressed()[0]:
                    save_path = filedialog.asksaveasfilename(
                        defaultextension=".png",
                        filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
                        title="Save Crumble Image"
                    )
                    if save_path:
                        pg.image.save(crumble_img, save_path)


            
            # Draw visible portion of recipe
            self.screen.blit(recipe_surface, (50, 50 + self.recipe_scroll))

            # Draw "Je teste" button
            button_rect = pg.Rect(self.screen_w//2 - 200, self.screen_h - 60, 400, 40)
            hover = button_rect.collidepoint(pg.mouse.get_pos())
            pg.draw.rect(self.screen, self.GREEN if not hover else self.DARK_GREEN, button_rect)
            button_text = self.font.render("Je teste cette recette !" if not self.will_test_recipe else "Recette testée !!!!!!!!!!!!", True, self.BLACK)
            button_text_rect = button_text.get_rect(center=button_rect.center)
            self.screen.blit(button_text, button_text_rect)
            
            # Handle button click
            if pg.mouse.get_pressed()[0]:
                if hover:
                    self.will_test_recipe = True
                    self.mode = "menu"
                    self.recipe_shown = False
            
            self.affiche = True
        
        for event in self.events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE and not self.recipe_shown:
                    self.mode = "menu"
                elif event.key == pg.K_ESCAPE and self.recipe_shown:
                    self.recipe_shown = False

            elif event.type == pg.MOUSEBUTTONDOWN and not self.recipe_shown:
                current_time = pg.time.get_ticks()
                mouse_pos = pg.mouse.get_pos()
                
                # Check yaniss.jpg click
                if self.img_rect.collidepoint(mouse_pos) and len(self.click_sequence) == 0:
                    self.click_sequence.append("yaniss")
                    self.last_click_time = current_time
                
                # Check text click
                elif self.text_rect.collidepoint(mouse_pos) and len(self.click_sequence) == 1:
                    self.click_sequence.append("text")
                
                # Check enzo.jpg click
                elif self.img_rect2.collidepoint(mouse_pos) and len(self.click_sequence) == 2:
                    if current_time - self.last_click_time <= 3000:  # 3 seconds
                        self.recipe_shown = True
                    self.click_sequence = []
            
            # Handle recipe scrolling
            elif event.type == pg.MOUSEWHEEL and self.recipe_shown:
                self.recipe_scroll += event.y * 20






    def exit(self):
        self.video.release()
        self.running = False
        pg.quit()
        os._exit(0)


if __name__ == "__main__":
    app = App()
