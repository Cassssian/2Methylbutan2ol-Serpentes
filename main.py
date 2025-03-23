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
                        ("numpy", True, 'np'),
                        ("io", True, False),
                        ('math', True, False),
                        ('re', True, False)
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
                        ("numpy", True, 'np'),
                        ("io", True, False),
                        ('math', True, False),
                        ('re', True, False)
                        )
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
    install_and_import(('pygame', True, "pg"),
                        )

class App:
    def __init__(self):
        #-------------------- Initialisation de l'application --------------------#

        pg.init()

        pg.mixer.init()

        self.clock = pg.time.Clock()

        self.screen_w, self.screen_h = pg.display.Info().current_w, pg.display.Info().current_h
        self.screen = pg.display.set_mode((self.screen_w, self.screen_h))
        pg.display.set_caption("2-Méthylbutan-2-ol Serpentes")
        self.font = pg.font.Font(None, 36)  # None utilise la police par défaut, 36 est la taille
        self.video = cv2.VideoCapture('./img/python.gif')
        self.boom_video = None
        self.boom_pos = None
        self.boom_size = (100, 100)
        pg.key.set_repeat(300, 50)
        #---------------------------------------------------------------------#

        #----------------- Variables pour la gestion du pgm ------------------#
        self.running = True
        self.mode = "menu"
        self.niv = "fini"
        self.shown_popup = False
        self.popup_text_show = False
        self.scroll_y = 0
        self.music_settings = False
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
• Enzo DUCCESCHI (Firewhole)
• Youtube

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

REMERCIMENTS SPECIAUX

Lycée Charles De Gaulle
Ingénieur de ITMGR (Cassssian)

Administration du Lycée Charles De Gaulle
Et surtout à M. LEBEL
sans qui cela n'aurait jamais pu se faire

Bibliothèques et logiciels utilisés
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
Io Library
Math Library
Re (Regular Expression) Library
Visual Studio Code
Github
Git

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Une application créée avec coeur par

Enzo DUCCESCHI (Cassssian) & Yaniss DUTHE
Version 1.0

© 2024 Tout droit réservé.
Equipe de 2Methylbutan2ol-Serpentes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""        
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
                         "table" : [["./img/scratchLogo.png", "./img/pythonLogo.png"], ["Exemple", "Exemple"],["./img/createVariableFR.png", './img/1.png']], 
                         "text2": "\n• Le nom de la variable est choisi par le programmeur, il doit être unique dans le programme et ne doit contenir ni espace ni accent.  \n• En Python, une variable doit obligatoirement être initialisée à l'aide de l'opérateur = lors de sa création (par exemple intialisée à 0 comme ci-dessus)."
                         }
                },
                
                {
                    "Modification" : {
                        "text1" : "Change la valeur contenue dans l'espace mémoire.",
                        "table" : [["./img/scratchLogo.png", "./img/pythonLogo.png"], ["Exemple", "Exemple"], ["./img/mettre_variable.png", './img/2.png'],["Exemple", "Exemple"],["./img/variable_avec_fonction.png", './img/3.png']]
                    }
                },
                
                {
                    "Utilisation" : {
                        "text1" : "Met à disposition d'une autre instruction la valeur contenue dans l'espace mémoire.",
                        "table" : [["./img/scratchLogo.png", "./img/pythonLogo.png"],["Exemple", 'Exemple'],["./img/utilisation_fonction_variables.png", './img/20.png']]
                    }
                },
                
                {
                    "Type" : {
                        "text1" : "Une variable peut avoir différents types selon la nature des valeurs qu'elle contient. En Python, on trouve (entre autres) :<dash>des nombres entiers</dash><dash>des nombres décimaux</dash><dash>des chaînes de caractères (texte)</dash><dash>des booléens (Vrai ou Faux)</dash>",
                        "table" : [["./img/scratchLogo.png", "./img/pythonLogo.png"],["Exemple", 'Exemple'],["./img/type_variable.png", './img/4.png']],
                        "text2" : "• Le séparateur des nombres décimaux est le point (.)  \n• Les chaînes de caractères doivent être entourées par des guillemets \"\".\n• Les variables de type booléen (qui n'existent pas en Scratch) peuvent prendre uniquement les valeurs True (vrai) ou False (faux)."
                    }
                }
                ],

            "Conditionnelle":

            [{"Utilité" : {
                "text1" : "Permet d'exécuter des instructions lorsque certaines conditions sont respectées."}},
            {"Conditionnelle à une branche" : {
                "text1" : "Permet d'exécuter des instructions si une condition est vraie.",
                "table" : [["./img/scratchLogo.png", "./img/pythonLogo.png"], ["Modèle", "Modèle"], ["./img/img_condition.png", './img/5.png'], ["Exemples", "Exemples"], ["./img/img_big_conditions.png", './img/6.png']],
                "text2" : "\n• Attention !!!!! pour tester une égalité on utilise un double égal ==.  \n• Les instructions dans la branche if (corps) doivent être décalées à l'aide de la touche tabulation."}},
            
            {"Conditionnelle à deux branches" : {
                "text1" : "Permet d'exécuter des instructions si une condition est vraie et d'autres instructions sinon (si la condition est fausse).",
                "table" : [["./img/scratchLogo.png", "./img/pythonLogo.png"], ["Modèle", "Modèle"], ["./img/img_condition_2.png", './img/7.png'], ["Exemples", "Exemples"], ["./img/img_big_condition_2.png", './img/8.png']],
                "text2" : "\n• Les instructions dans les branches if et else (corps) doivent être décalées à l'aide de la touche tabulation."}},
            
            {"À trois branches ou plus" : {
                "text1" : "Permet d'exécuter des instructions différentes en fonction de différentes conditions.",
                "table" : [["./img/scratchLogo.png", "./img/pythonLogo.png"], ["Modèle", "Modèle"], ["./img/img_condition_3.png", './img/9.png'], ["Exemples", "Exemples"], ["./img/img_big_condition_3.png", './img/10.png']],
                "text2" : "\n• Il est possible d'ajouter autant de branches elif (contraction de else et if) que l'on souhaite.  \n• La branche else n'est pas obligatoire, une conditionnelle peut n'avoir que des branches if et elif.  \n• Les instructions dans les branches if, elif et else (corps) doivent être décalées à l'aide de la touche tabulation."}},
            ],

            "Boucle for":

            [{"Utilité" : {
                "text1" : "Permet de répéter des instructions un certain nombre de fois."}},

            {"Répétition simple" : {
                "text1" : "Permet de répéter des instructions un certain nombre de fois donné.",
                "table" : [["./img/scratchLogo.png", "./img/pythonLogo.png"], ["Modèle", "Modèle"], ["./img/img_boucle_1.png", './img/11.png'], ["Exemples", "Exemples"], ["./img/img_big_boucle_1.png",'./img/12.png']],
                "text2" : "\n• nombre entre parenthèses dans range(nombre) indique le nombre de répétitions des instruction.  \n• Les instructions répétées dans la boucle (corps) doivent être décalées à l'aide de la touche tabulation."}},
            
            {"Avec compteur (commence à zéro)" : {
                "text1" : "Permet de répéter des instructions un certain nombre de fois tout en mettant à jour automatiquement une variable compteur qui est initialisée à zéro.",
                "table" : [["./img/scratchLogo.png", "./img/pythonLogo.png"], ["Modèle", "Modèle"], ["./img/img_boucle_2.png", './img/13.png'], ["Exemples", "Exemples"], ["./img/img_big_boucle_2.png", './img/14.png']],
                "text2" : "\n• Le nombre entre parenthèses dans range(nombre) indique le nombre de répétitions des instructions.  \n• La variable compteur est automatiquement initialisée à 0 et automatiquement augmentée de 1 à la fin de chaque tour de boucle (sauf au dernier).  \n• La variable compteur peut être utilisée dans les instructions répétées dans la boucle. "}},

            {"Avec compteur (début pas à zéro)" : {
                "text1" : "Permet de répéter des instructions un certain nombre de fois tout en mettant à jour automatiquement une variable compteur.",
                "table" : [["./img/scratchLogo.png", "./img/pythonLogo.png"], ["Modèle", "Modèle"], ["./img/img_boucle_3.png", './img/15.png'], ["Exemples", "Exemples"], ["./img/img_big_boucle_3.png", './img/16.png']],
                "text2" : "\n• La variable compteur est automatiquement initialisée à n1 (3 dans l'exemple) et automatiquement augmenté de 1 à la fin de chaque tour de boucle (sauf au dernier).  \n• Attention !!!! Les répétitions s'arrêtent lorsque le compteur atteint n2-1 (6 dans l'exemple: 7-1 ). "
            }}],

            "Boucle while":

            [{"Utilité" : {
                "text1" : "Permet de répéter des instructions tant que certaines conditions sont respectées."}},
            
            {"Répétition tant que..." : {
                "text1" : "Permet de répéter des instructions tant qu'une condition est vraie.",
                "table" : [["./img/scratchLogo.png", "./img/pythonLogo.png"], ["Modèle", "Modèle"], ["./img/img_while.png", './img/18.png'], ["Exemples", "Exemples"], ["./img/img_whilee.png", './img/19.png']],
                "text2" : "\n• La boucle continue de tourner tant que la condition est vraie et elle s'arrête dès qu'elle devient fausse.  \n• Attention !!!! en Python la boucle tourne tant que la condition est vraie, en Scratch la boucle s'arrête quand la condition est vraie.  \n• Les instructions répétées dans la boucle (corps) doivent être décalées à l'aide de la touche tabulation."}}]
        }
        #----------------------------------------------------------#

        #------------------------- Code ---------------------------#
        self.code_text = []  # Liste des lignes de code
        self.scroll_offset = 0
        self.syntax_colors = {
            'keywords': (86, 156, 214),     # bleu
            'fonctions': (220, 220, 170),   # jaune
            'strings': (206, 145, 120),     # orange 
            'comments': (87, 166, 74),      # vert
            'numbers': (181, 206, 168),     # vert clair
            'background': (30, 30, 30),     # gris foncé
            'operators': (102, 100, 255),   # bleu bzr
            'arg_used': (0, 191, 255),      # bleu clair
            'arg_unused': (0, 0, 139),      # bleu foncé
        }
        self.cursor_timer = 0
        self.cursor_visible = True
        self.space_number = [0]
        self.show_trace = False
        self.show_console = True
        self.output = None
        self.text_error = False
        self.code_text = ["re = input('Entrez un nombre : ')", "print(re)"]
        self.indent = 3
        self.cursor_pos = [len(self.code_text[0]), 0]
        self.selected_text = None
        self.selection_start = None
        self.selection_end = None
        self.internal_clipboard = None
        self.code_longueur_avant_echap = 0
        self.console_scroll_y = 0
        self.code_scroll_y = 0
        self.show_art = False
        self.password_active = False
        self.password_text = ""
        self.color_picker_active = False
        self.selected_syntax_element = None
        self.main_color_value = 0
        self.brightness_value = 0.5
        self.saturation_value = 1.0
        self.value_value = 1.0
        self.verif_result = False
        self.fin = False
        #----------------------------------------------------------#
        self.run()

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

            if pg.mouse.get_pressed()[0]:
                self.boom_video = cv2.VideoCapture('./img/boom.gif')
                self.boom_pos = pg.mouse.get_pos()

            if self.boom_video and self.show_art:
                ret, frame = self.boom_video.read()
                if ret:
                    frame = cv2.resize(frame, self.boom_size)
                    # Convert to RGBA to handle transparency
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                    
                    # Create mask for white pixels
                    white_mask = np.all(frame[:,:,:3] > 250, axis=2)
                    # Set alpha channel to 0 for white pixels
                    frame[white_mask, 3] = 0
                    
                    frame = frame.transpose((1, 0, 2))
                    
                    # Create surface with alpha channel
                    frame_surface = pg.Surface(self.boom_size, pg.SRCALPHA)
                    pg.surfarray.pixels_alpha(frame_surface)[:] = frame[:,:,3]
                    pg.surfarray.pixels3d(frame_surface)[:] = frame[:,:,:3]
                    
                    frame_rect = frame_surface.get_rect(center=self.boom_pos)
                    self.screen.blit(frame_surface, frame_rect)
                else:
                    self.boom_video.release()
                    self.boom_video = None

            pg.display.update()
            pg.display.flip()
            self.clock.tick(60)

    def draw_color_picker(self):
        if not self.selected_syntax_element:
            # Draw element selection list
            elements = list(self.syntax_colors.keys())
            list_width = 300
            list_height = len(elements) * 40 + 20
            list_x = (self.screen_w - list_width) // 2
            list_y = (self.screen_h - list_height) // 2
            
            list_surface = pg.Surface((list_width, list_height))
            list_surface.fill((40, 40, 40))
            
            for i, element in enumerate(elements):
                button_rect = pg.Rect(10, i * 40 + 10, list_width - 20, 30)
                color = self.syntax_colors[element]
                pg.draw.rect(list_surface, color, button_rect)
                text = self.font.render(element, True, self.WHITE)
                text_rect = text.get_rect(center=button_rect.center)
                list_surface.blit(text, text_rect)
                
                # Handle click
                mouse_pos = pg.mouse.get_pos()
                relative_pos = (mouse_pos[0] - list_x, mouse_pos[1] - list_y)
                if pg.mouse.get_pressed()[0] and button_rect.collidepoint(relative_pos):
                    self.selected_syntax_element = element
            
            self.screen.blit(list_surface, (list_x, list_y))
            return

        # Color picker dimensions
        picker_width = 600
        picker_height = 400
        picker_x = (self.screen_w - picker_width) // 2
        picker_y = (self.screen_h - picker_height) // 2
        
        picker_surface = pg.Surface((picker_width, picker_height))
        picker_surface.fill((40, 40, 40))

        # Main gradient area
        gradient_width = picker_width - 100
        gradient_height = picker_height - 100
        gradient_surface = pg.Surface((gradient_width, gradient_height))
        
        # Draw gradient
        for x in range(gradient_width):
            for y in range(gradient_height):
                saturation = x / gradient_width * 100
                value = (gradient_height - y) / gradient_height * 100
                color = pg.Color(0)
                color.hsva = (self.main_color_value * 360, saturation, value, 100)
                gradient_surface.set_at((x, y), color)
        
        picker_surface.blit(gradient_surface, (50, 30))

        # Vertical hue slider with arrow
        slider_width = 20
        color_height = picker_height - 60
        for i in range(color_height):
            hue = i / color_height
            color = pg.Color(0)
            color.hsva = (hue * 360, 100, 100, 100)
            pg.draw.line(picker_surface, color, (picker_width - 30, i + 30), 
                        (picker_width - 30 + slider_width, i + 30))
        
        # Draw vertical arrow
        arrow_y = 30 + (self.main_color_value * color_height)
        arrow_points = [(picker_width - 40, arrow_y),
                    (picker_width - 35, arrow_y - 5),
                    (picker_width - 35, arrow_y + 5)]
        pg.draw.polygon(picker_surface, self.WHITE, arrow_points)

        # Horizontal brightness slider with arrow
        brightness_height = 20
        for i in range(gradient_width):
            brightness = i / gradient_width
            color = pg.Color(0)
            color.hsva = (self.main_color_value * 360, 100, brightness * 100, 100)
            pg.draw.line(picker_surface, color, (50 + i, picker_height - 30),
                        (50 + i, picker_height - 30 + brightness_height))
        
        # Draw horizontal arrow
        arrow_x = 50 + (self.brightness_value * gradient_width)
        arrow_points = [(arrow_x, picker_height - 40),
                    (arrow_x - 5, picker_height - 35),
                    (arrow_x + 5, picker_height - 35)]
        pg.draw.polygon(picker_surface, self.WHITE, arrow_points)

        # Draw selection circle in gradient
        circle_x = int(50 + (self.saturation_value * gradient_width))
        circle_y = int(30 + ((1 - self.value_value) * gradient_height))
        pg.draw.circle(picker_surface, self.WHITE, (circle_x, circle_y), 5, 2)

        # Handle mouse interaction
        mouse_pos = pg.mouse.get_pos()
        relative_pos = (mouse_pos[0] - picker_x, mouse_pos[1] - picker_y)
        
        if pg.mouse.get_pressed()[0]:
            # Vertical hue slider
            if (picker_width - 30 <= relative_pos[0] <= picker_width - 10 and 
                30 <= relative_pos[1] <= picker_height - 30):
                self.main_color_value = (relative_pos[1] - 30) / color_height
                
            # Main gradient area
            elif (50 <= relative_pos[0] <= 50 + gradient_width and 
                30 <= relative_pos[1] <= 30 + gradient_height):
                self.saturation_value = (relative_pos[0] - 50) / gradient_width
                self.value_value = 1 - ((relative_pos[1] - 30) / gradient_height)
                
                # Update color
                color = pg.Color(0)
                color.hsva = (self.main_color_value * 360, 
                            self.saturation_value * 100,
                            self.value_value * 100, 100)
                self.syntax_colors[self.selected_syntax_element] = color

        # Draw current color preview and element name
        current_color = self.syntax_colors[self.selected_syntax_element]
        pg.draw.rect(picker_surface, current_color, (50, picker_height - 80, 100, 30))
        element_text = self.font.render(self.selected_syntax_element, True, self.WHITE)
        picker_surface.blit(element_text, (160, picker_height - 75))

        self.screen.blit(picker_surface, (picker_x, picker_y))


    def settings(self):
        # Charger la vidéo et la musique une seule fois au début
        if not hasattr(self, 'settings_video'):
            self.settings_video = cv2.VideoCapture("./img/bob.mp4")
            pg.mixer.music.load("./music/Firewhole - maxwell, our beloved.mp3")
            pg.mixer.music.play(-1)
            self.music_settings = True

        settings_surface = pg.Surface((self.screen_w, self.screen_h))
        settings_surface.fill((0, 0, 0))
        self.screen.blit(settings_surface, (0,0))

        # Lire la frame suivante
        ret, frame = self.settings_video.read()
        if not ret:
            self.settings_video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = self.settings_video.read()

        frame = cv2.resize(frame, (self.screen_w, self.screen_h))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_surface = pg.surfarray.make_surface(frame)
        self.screen.blit(pg.transform.rotate(pg.transform.flip(frame_surface, False, True), -90), (0, 0))

        # Add volume slider
        slider_width = 300
        slider_height = 10
        slider_x = (self.screen_w - slider_width) // 2
        slider_y = self.screen_h * 0.8
        art_button_rect = pg.Rect((self.screen_w - 300) // 2, self.screen_h * 0.9, 300, 40)
        pg.draw.rect(self.screen, self.BLUE if not self.show_art else self.DARK_BLUE, art_button_rect)
        art_text = self.font.render("Mode Artistique", True, self.WHITE)
        art_rect = art_text.get_rect(center=art_button_rect.center)
        self.screen.blit(art_text, art_rect)
        
        # Draw slider background
        pg.draw.rect(self.screen, self.GRAY, (slider_x, slider_y, slider_width, slider_height))
        
        # Get current volume and calculate position
        current_volume = pg.mixer.music.get_volume()
        handle_x = slider_x + (slider_width * current_volume)
        
        # Draw slider handle
        handle_size = 20
        handle_rect = pg.Rect(handle_x - handle_size//2, slider_y - handle_size//2 + slider_height//2, handle_size, handle_size)
        pg.draw.rect(self.screen, self.WHITE, handle_rect)
        
        # Volume text
        volume_text = self.font.render(f"Volume: {int(current_volume * 100)}%", True, self.WHITE)
        text_rect = volume_text.get_rect(center=(self.screen_w//2, slider_y - 30))
        self.screen.blit(volume_text, text_rect)

        color_button_rect = pg.Rect((self.screen_w - 350) // 2, self.screen_h * 0.6, 350, 40)
        pg.draw.rect(self.screen, self.BLUE if not self.color_picker_active else self.DARK_BLUE, 
                    color_button_rect)
        color_text = self.font.render("Personnaliser les couleurs", True, self.WHITE)
        color_rect = color_text.get_rect(center=color_button_rect.center)
        self.screen.blit(color_text, color_rect)
        
        # Handle volume control
        if pg.mouse.get_pressed()[0]:
            mouse_x = pg.mouse.get_pos()[0]
            if slider_x <= mouse_x <= slider_x + slider_width:
                new_volume = (mouse_x - slider_x) / slider_width
                new_volume = max(0, min(1, new_volume))
                pg.mixer.music.set_volume(new_volume)

            if color_button_rect.collidepoint(pg.mouse.get_pos()):
                self.color_picker_active = True
        
        if self.color_picker_active:
            self.draw_color_picker()

        for event in self.events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if not self.color_picker_active:
                        self.music_settings = False
                        pg.mixer.music.stop()
                        self.mode = "menu"
                        self.settings_video.release()
                        delattr(self, 'settings_video')
                    else:
                        self.color_picker_active = False

        if self.password_active:
            # Draw popup background
            popup_rect = pg.Rect((self.screen_w - 400) // 2, (self.screen_h - 200) // 2, 400, 200)
            pg.draw.rect(self.screen, (50, 50, 50), popup_rect)
            
            # Draw password input box
            input_rect = pg.Rect(popup_rect.centerx - 150, popup_rect.centery - 20, 300, 40)
            pg.draw.rect(self.screen, self.WHITE, input_rect, 2)
            
            # Render password text
            password_surface = self.font.render(self.password_text, True, self.WHITE)
            self.screen.blit(password_surface, (input_rect.x + 5, input_rect.y + 5))
            
            # Handle password input
            for event in self.events:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        if self.password_text == "La galouche":
                            self.show_art = not self.show_art
                        self.password_active = False
                        self.password_text = ""
                    elif event.key == pg.K_BACKSPACE:
                        self.password_text = self.password_text[:-1]
                    else:
                        self.password_text += event.unicode

        # Handle button click
        mouse_pos = pg.mouse.get_pos()
        if pg.mouse.get_pressed()[0]:
            if art_button_rect.collidepoint(mouse_pos) and not self.password_active:
                self.password_active = True

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
        elif self.niv == "fini":
            self.niveau_fini()

    def render_table(self, table_data, surface_width):
        cell_padding = 10
        col_width = surface_width // len(table_data[0]) - cell_padding * 2
        line_thickness = 2
        
        # First pass: calculate row heights
        row_heights = []
        for row in table_data:
            max_height = 60  # Minimum row height
            for cell in row:
                if isinstance(cell, str):
                    if cell.endswith(('.png', '.jpg', '.jpeg')):
                        try:
                            img = pg.image.load(cell)
                            # Calculate scaled height maintaining aspect ratio
                            aspect_ratio = img.get_height() / img.get_width()
                            scaled_height = min(col_width * aspect_ratio, 200)  # Max height of 200px
                            max_height = max(max_height, scaled_height + cell_padding * 2)
                        except:
                            text = self.font.render("Image non trouvée", True, self.RED)
                            max_height = max(max_height, text.get_height() + cell_padding * 2)
                    else:
                        text = self.font.render(str(cell), True, self.WHITE)
                        max_height = max(max_height, text.get_height() + cell_padding * 2)
            row_heights.append(max_height)
        
        # Calculate total table height
        table_height = sum(row_heights)
        table_surface = pg.Surface((surface_width, table_height))
        table_surface.fill(self.BLACK)
        
        # Draw cells content
        current_y = 0
        for row_idx, row in enumerate(table_data):
            for col_idx, cell in enumerate(row):
                x = col_idx * (col_width + cell_padding * 2) + cell_padding
                y = current_y + cell_padding
                
                if isinstance(cell, str) and cell.endswith(('.png', '.jpg', '.jpeg')):
                    try:
                        img = pg.image.load(cell)
                        # Scale image maintaining aspect ratio
                        aspect_ratio = img.get_height() / img.get_width()
                        scaled_width = min(col_width, img.get_width())
                        scaled_height = scaled_width * aspect_ratio
                        
                        if scaled_height > row_heights[row_idx] - cell_padding * 2:
                            scaled_height = row_heights[row_idx] - cell_padding * 2
                            scaled_width = scaled_height / aspect_ratio
                        
                        img = pg.transform.scale(img, (int(scaled_width), int(scaled_height)))
                        # Center the image in the cell
                        img_x = x + (col_width - scaled_width) / 2
                        img_y = y + (row_heights[row_idx] - cell_padding * 2 - scaled_height) / 2
                        table_surface.blit(img, (img_x, img_y))
                    except:
                        text = self.font.render("Image non trouvée", True, self.RED)
                        text_rect = text.get_rect(midleft=(x, y + row_heights[row_idx]/2))
                        table_surface.blit(text, text_rect)
                else:
                    if isinstance(cell, str) and cell.startswith('code :'):
                        # Extract code from cell
                        code = cell[6:].strip()  # Remove 'code :' prefix
                        
                        # Create syntax highlighted surface
                        tokens = self.tokenize_line(code)
                        code_surface = pg.Surface((col_width, row_heights[row_idx] - cell_padding * 2))
                        code_surface.fill(self.RED)
                        
                        x = cell_padding
                        for token, color in tokens:
                            text = self.font.render(token, True, self.syntax_colors.get(color, self.WHITE))
                            code_surface.blit(text, (x, cell_padding))
                            x += text.get_width()
                        
                        # Add click detection
                        cell_rect = pg.Rect(col_idx * (col_width + cell_padding * 2) + cell_padding,
                                        current_y + cell_padding,
                                        col_width,
                                        row_heights[row_idx] - cell_padding * 2)
                        
                        # if cell_rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
                        #     self.code_text.append(code)
                        #     self.cursor_pos = [len(self.code_text)-1, len(code)]
                        
                        table_surface.blit(code_surface, (col_idx * (col_width + cell_padding * 2) + cell_padding, 
                                                        current_y + cell_padding))

                    else:
                        text = self.font.render(str(cell), True, self.WHITE)
                        text_rect = text.get_rect(midleft=(x, y + row_heights[row_idx]/2))
                        table_surface.blit(text, text_rect)
            
            # Draw horizontal lines
            pg.draw.line(table_surface, self.WHITE, (0, current_y), (surface_width, current_y), line_thickness)
            current_y += row_heights[row_idx]
        
        # Draw final horizontal line
        pg.draw.line(table_surface, self.WHITE, (0, table_height - line_thickness), 
                    (surface_width, table_height - line_thickness), line_thickness)
        
        # Draw vertical lines
        for col in range(len(table_data[0]) + 1):
            x = col * (col_width + cell_padding * 2)
            pg.draw.line(table_surface, self.WHITE, (x, 0), (x, table_height), line_thickness)
        
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
                                table_surface = self.render_table(value, max_width)
                                total_height += table_surface.get_height()
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

        if total_height > self.screen_h:
            scrollbar_height = (self.screen_h / total_height) * self.screen_h
            scrollbar_pos = (-scroll_y / total_height) * self.screen_h            
            # Draw scrollbar handle with rounded corners
            pg.draw.rect(popup_surface, (100, 100, 100), 
                        (LEFT_PANEL_WIDTH - 10, scrollbar_pos, 8, scrollbar_height),
                        border_radius=4)

        
        # Draw fixed header
        header_surface = pg.Surface((LEFT_PANEL_WIDTH, 40))
        header_surface.fill(self.BLUE)
        header_text = self.font.render(self.popup_text_show, True, self.WHITE)
        header_text_rect = header_text.get_rect(topleft=(10, 12))
        header_surface.blit(header_text, header_text_rect)
        popup_surface.blit(header_surface, (0, 0))

        return popup_surface, scroll_y

    def handle_code_editor(self, editor_surface, events):
        if not self.code_text:
            self.code_text = [""]
        line_height = 25
        
        # Calculate cursor x position based on text width
        try:
            current_line = self.code_text[self.cursor_pos[1]]
        except:
            current_line = self.code_text[max(0,self.cursor_pos[1] - 1)]
        text_before_cursor = current_line[:self.cursor_pos[0]]
        cursor_x = 40 + self.font.size(text_before_cursor)[0]
        cursor_y = self.cursor_pos[1] * line_height

        # Handle mouse clicks for cursor positioning
        mouse_pos = pg.mouse.get_pos()
        editor_rect = editor_surface.get_rect()
        if pg.mouse.get_pressed()[0] and editor_rect.collidepoint(mouse_pos):
            # Convert mouse position to relative editor coordinates
            click_x = mouse_pos[0] - (self.screen_w * 0.4 + 50)  # Adjust for left panel and margin
            click_y = mouse_pos[1] - 10  # Adjust for top margin
            
            # Calculate line number from y position
            clicked_line = min(len(self.code_text) - 1, max(0, click_y // 25))
            
            # Calculate character position from x position
            line_content = self.code_text[clicked_line]
            test_pos = 0
            
            # Find position by measuring text width until we exceed click position
            while test_pos <= len(line_content):
                if self.font.size(line_content[:test_pos])[0] > click_x:
                    break
                test_pos += 1
            
            # Update cursor position
            self.cursor_pos = [test_pos - 1, clicked_line]
            self.selection_start = None
            self.selection_end = None


            
        # Handle keyboard events
        for event in events:

            if event.type == pg.KEYDOWN:

                # Raccourcis
                
                # Gestion de la sélection avec Shift
                if event.mod & pg.KMOD_SHIFT:
                    if event.key == pg.K_LEFT:
                        if self.selection_start is None:
                            self.selection_start = self.cursor_pos[0]
                        self.cursor_pos[0] = max(0, self.cursor_pos[0] - 1)
                        self.selection_end = self.cursor_pos[0]
                        
                    elif event.key == pg.K_RIGHT:
                        if self.selection_start is None:
                            self.selection_start = self.cursor_pos[0]
                        self.cursor_pos[0] = min(len(self.code_text[self.cursor_pos[1]]), self.cursor_pos[0] + 1)
                        self.selection_end = self.cursor_pos[0]
                        
                    elif event.key == pg.K_HOME:
                        if self.selection_start is None:
                            self.selection_start = self.cursor_pos[0]
                        self.cursor_pos[0] = 0
                        self.selection_end = self.cursor_pos[0]
                        
                    elif event.key == pg.K_END:
                        if self.selection_start is None:
                            self.selection_start = self.cursor_pos[0]
                        self.cursor_pos[0] = len(self.code_text[self.cursor_pos[1]])
                        self.selection_end = self.cursor_pos[0]

                # Ctrl+A pour tout sélectionner
                elif event.mod & pg.KMOD_CTRL and event.key == pg.K_a:
                    self.selection_start = 0
                    self.selection_end = len(self.code_text[self.cursor_pos[1]])
                    self.cursor_pos[0] = self.selection_end

                # Ctrl+C pour copier
                elif event.mod & pg.KMOD_CTRL and event.key == pg.K_c:
                    if self.selection_start is not None and self.selection_end is not None:
                        start = min(self.selection_start, self.selection_end)
                        end = max(self.selection_start, self.selection_end)
                        selected_text = self.code_text[self.cursor_pos[1]][start:end]
                        self.internal_clipboard = selected_text

                # Ctrl+V pour coller
                elif event.mod & pg.KMOD_CTRL and event.key == pg.K_v:
                    if self.internal_clipboard is not None:
                        if self.selection_start is not None:
                            start = min(self.selection_start, self.selection_end)
                            end = max(self.selection_start, self.selection_end)
                            self.code_text[self.cursor_pos[1]] = (
                                self.code_text[self.cursor_pos[1]][:start] +
                                self.internal_clipboard +
                                self.code_text[self.cursor_pos[1]][end:]
                            )
                            self.cursor_pos[0] = start + len(self.internal_clipboard)
                        else:
                            self.code_text[self.cursor_pos[1]] = (
                                self.code_text[self.cursor_pos[1]][:self.cursor_pos[0]] +
                                self.internal_clipboard +
                                self.code_text[self.cursor_pos[1]][self.cursor_pos[0]:]
                            )
                            self.cursor_pos[0] += len(self.internal_clipboard)
                        self.selection_start = None
                        self.selection_end = None                
                
                if event.key == pg.K_RETURN:
                    # Add new line with indentation
                    self.indent = 0
                    nb_espace = 0
                    for j in range(self.code_longueur_avant_echap,len(self.code_text)):
                        for i in range(0,len(self.code_text[j])):
                            if self.code_text[self.cursor_pos[1]][i] == " ":
                                nb_espace += 1
                            else:
                                break
                    self.indent = nb_espace
                    if self.code_text[self.cursor_pos[1]].strip() and self.code_text[self.cursor_pos[1]].strip()[-1] == ":":
                        self.indent += 3
                    self.code_longueur_avant_echap = len(self.code_text)
                    
                    while self.indent % 3 != 0:
                        self.indent -= 1

                    self.code_text.insert(self.cursor_pos[1] + 1, " " * self.indent) if self.cursor_pos[0] == len(self.code_text[self.cursor_pos[1]]) else self.code_text.insert(self.cursor_pos[1] + 1, " " * self.indent + self.code_text[self.cursor_pos[1]][self.cursor_pos[0]:])
                    self.code_text[self.cursor_pos[1]] = self.code_text[self.cursor_pos[1]][:self.cursor_pos[0]] if not self.cursor_pos[0] == len(self.code_text[self.cursor_pos[1]]) else self.code_text[self.cursor_pos[1]]
                    self.cursor_pos[0] = self.indent
                    self.cursor_pos[1] += 1
                    
                elif event.key == pg.K_TAB:
                    self.code_text[self.cursor_pos[1]] = self.code_text[self.cursor_pos[1]][:self.cursor_pos[0]] + " " * 3 + self.code_text[self.cursor_pos[1]][self.cursor_pos[0]:]
                    self.cursor_pos[0] += 3
                
                elif event.key == pg.K_HOME:
                    if not (event.mod & pg.KMOD_SHIFT):
                        self.cursor_pos[0] = 0
                    
                elif event.key == pg.K_BACKSPACE:
                    if self.selection_start is not None and self.selection_end is not None:
                        start = min(self.selection_start, self.selection_end)
                        end = max(self.selection_start, self.selection_end)
                        self.code_text[self.cursor_pos[1]] = (
                            self.code_text[self.cursor_pos[1]][:start] +
                            self.code_text[self.cursor_pos[1]][end:]
                        )
                        self.cursor_pos[0] = start
                        self.selection_start = None
                        self.selection_end = None
                    
                    else : 
                        if self.cursor_pos[0] > 0:
                            self.code_text[self.cursor_pos[1]] = self.code_text[self.cursor_pos[1]][:self.cursor_pos[0] - 1] + self.code_text[self.cursor_pos[1]][self.cursor_pos[0]:]
                            self.cursor_pos[0] = max(0, self.cursor_pos[0] - 1)
                        else:
                            if self.cursor_pos[0] == 0 and len(self.code_text) > 1:
                                # Delete previous line and move cursor to end of previous line and move the code to the end of previous line
                                code = self.code_text.pop(self.cursor_pos[1])
                                self.code_text[self.cursor_pos[1] - 1] = self.code_text[self.cursor_pos[1] - 1] + code
                                self.cursor_pos[0] = len(self.code_text[self.cursor_pos[1] - 1])
                                self.cursor_pos[1] = max(0, self.cursor_pos[1] - 1)
                                
                elif event.key == pg.K_LEFT:
                    if not (event.mod & pg.KMOD_SHIFT):  # If Shift is not pressed
                        self.selection_start = None
                        self.selection_end = None

                        if self.cursor_pos[0] == 0 and self.cursor_pos[1] > 1:
                            self.cursor_pos = [len(current_line) - 1, max(0, self.cursor_pos[1] - 1)]
                        else:
                            self.cursor_pos[0] = max(0, self.cursor_pos[0] - 1)
                    
                elif event.key == pg.K_RIGHT:
                    if not (event.mod & pg.KMOD_SHIFT):  # If Shift is not pressed
                        self.selection_start = None
                        self.selection_end = None

                        if self.cursor_pos[0] < len(self.code_text[self.cursor_pos[1]]):
                            self.cursor_pos[0] += 1
                        elif len(self.code_text) > 2 and self.cursor_pos[1] < len(self.code_text) - 1:
                            self.cursor_pos = [0, min(len(self.code_text), self.cursor_pos[1] + 1)]
                        else:
                            pass

                elif event.key == pg.K_UP:
                    if not (event.mod & pg.KMOD_SHIFT):  # If Shift is not pressed
                        self.selection_start = None
                        self.selection_end = None

                        if self.cursor_pos[1] > 0:
                            self.cursor_pos[1] = max(self.cursor_pos[1] - 1, 0)

                elif event.key == pg.K_DOWN:
                    if not (event.mod & pg.KMOD_SHIFT):  # If Shift is not pressed
                        self.selection_start = None
                        self.selection_end = None

                        if self.cursor_pos[1] < len(self.code_text) - 1:
                            self.cursor_pos[1] = min(self.cursor_pos[1] + 1, len(self.code_text[self.cursor_pos[1]]))

                elif event.key == pg.K_DELETE:
                    if self.selection_start is not None and self.selection_end is not None:
                        start = min(self.selection_start, self.selection_end)
                        end = max(self.selection_start, self.selection_end)
                        self.code_text[self.cursor_pos[1]] = (
                            self.code_text[self.cursor_pos[1]][:start] +
                            self.code_text[self.cursor_pos[1]][end:]
                        )
                        self.cursor_pos[0] = start
                        self.selection_start = None
                        self.selection_end = None
                    
                    else:
                        if self.cursor_pos[0] < len(self.code_text[self.cursor_pos[1]]):
                            self.code_text[self.cursor_pos[1]] = self.code_text[self.cursor_pos[1]][:self.cursor_pos[0]] + self.code_text[self.cursor_pos[1]][self.cursor_pos[0] + 1:]
                            
                        # If cursor at end of line, move first word of next line to cursor
                        if self.cursor_pos[0] == len(self.code_text[self.cursor_pos[1]]):
                            if self.cursor_pos[1] < len(self.code_text) - 1:
                                self.code_text[self.cursor_pos[1]] += self.code_text[self.cursor_pos[1] + 1].split(" ")[0]
                                next_line = self.code_text.pop(self.cursor_pos[1] + 1).split(" ")
                                next_line.pop(0)
                
                elif event.key == pg.K_END:
                    self.cursor_pos[0] = len(self.code_text[self.cursor_pos[1]])

                elif event.unicode.isalnum() or event.unicode in [' ', '.', '_', '(', ')', '[', ']', '{', '}', ':', '"', "'", '+', '-', '*', '/', '%', '=', '<', '>', '!', '?', ',', ';']:
                    # Add character
                    current_line = self.code_text[self.cursor_pos[1]]
                    self.code_text[self.cursor_pos[1]] = (
                        current_line[:self.cursor_pos[0]] + 
                        event.unicode + 
                        current_line[self.cursor_pos[0]:]
                    )
                    self.cursor_pos[0] += 1
        # Display line numbers
        for i in range(len(self.code_text)):
            line_num = self.font.render(str(i+1), True, (150, 150, 150))
            editor_surface.blit(line_num, (5, i * line_height))
            
        for i, line in enumerate(self.code_text):
            current_line = ''
            tokens = self.tokenize_line(line)
            text_width = 0
            for token, color in tokens:
                text = self.font.render(token, True, color)
                text_width = self.font.size(current_line)[0]
                editor_surface.blit(text, (40 + text_width, i * line_height))
                current_line += token


        if self.selection_start is not None and self.selection_end is not None:
            start_x = 40 + self.font.size(self.code_text[self.cursor_pos[1]][:min(self.selection_start, self.selection_end)])[0]
            end_x = 40 + self.font.size(self.code_text[self.cursor_pos[1]][:max(self.selection_start, self.selection_end)])[0]
            selection_rect = pg.Rect(
                start_x,
                self.cursor_pos[1] * line_height,
                end_x - start_x,
                line_height
            )
            selection_surface = pg.Surface((end_x - start_x, line_height))
            selection_surface.fill((100, 100, 150))
            selection_surface.set_alpha(128)
            editor_surface.blit(selection_surface, (start_x, self.cursor_pos[1] * line_height))


                
        # Cursor display
        self.cursor_timer += 1
        if self.cursor_timer >= 30:
            self.cursor_visible = not self.cursor_visible
            self.cursor_timer = 0
            
        if self.cursor_visible:
            pg.draw.line(editor_surface, (255,255,255), 
                    (cursor_x, cursor_y), 
                    (cursor_x, cursor_y + line_height))
                    
        # Scroll handling
        total_height = len(self.code_text) * line_height
        if total_height > editor_surface.get_height():
            scroll_height = editor_surface.get_height() * (editor_surface.get_height() / total_height)
            scroll_pos = (-self.scroll_offset / total_height) * editor_surface.get_height()
            pg.draw.rect(editor_surface, (100,100,100), 
                        (editor_surface.get_width()-10, scroll_pos, 10, scroll_height), border_radius=4)

    def tokenize_line(self, line):
        """Analyse lexicale basique pour la coloration syntaxique"""
        # Définition des motifs pour la coloration syntaxique
        KEYWORDS = [
    'False','None','True','and','as','assert','async','await','break','class','continue','def','del','elif','else','except','finally','for','from','global','if','import','in','is','lambda','nonlocal','not','or','pass','raise','return','try','while','with','yield'
]
        KEYWORDS_PATTERN = r'\b(' + '|'.join(KEYWORDS) + r')\b'

        STRING_PATTERN = r'(\".*?\"|\'.*?\')'

        FUNCTION_PATTERN = r'\b\w+(?=\()'

        COMMENT_PATTERN = r'#[^\n]*'

        NUMBER_PATTERN = r'\b\d+\.?\d*\b'

        ARG_PATTERN = r'def \w+\((.*?)\):'

        OPERATOR_PATTERN = r'[-+*/=<>!&|^%~]'

        parts = [(line, (255, 255, 255))]  # Texte par défaut en blanc

        # Appliquer les motifs de coloration
        for pattern, color_key in [
            (STRING_PATTERN, 'strings'),
            (COMMENT_PATTERN, 'comments'),
            (KEYWORDS_PATTERN, 'keywords'),
            (FUNCTION_PATTERN, 'fonctions'),
            (NUMBER_PATTERN, 'numbers')
        ]:
            new_parts = []
            for text, color in parts:
                start = 0
                for match in re.finditer(pattern, text):
                    new_parts.append((text[start:match.start()], color))
                    new_parts.append((match.group(), self.syntax_colors[color_key]))
                    start = match.end()
                new_parts.append((text[start:], color))
            parts = new_parts

        # Coloration des opérateurs en ignorant les chaînes
        new_parts = []
        for text, color in parts:
            if color == self.syntax_colors['strings']:
                new_parts.append((text, color))
                continue
            start = 0
            for match in re.finditer(OPERATOR_PATTERN, text):
                new_parts.append((text[start:match.start()], color))
                new_parts.append((match.group(), self.syntax_colors['operators']))
                start = match.end()
            new_parts.append((text[start:], color))
        parts = new_parts
        
        # Gestion des arguments des fonctions
        for func_match in re.finditer(ARG_PATTERN, line):
            args = func_match.group(1).split(',')
            arg_names = [arg.strip().split('=')[0] for arg in args if arg.strip()]
            for arg in arg_names:
                pattern = rf'\b{arg}\b'
                color_key = 'arg_unused'
                if re.search(pattern, line[func_match.end():]):
                    color_key = 'arg_used'
                new_parts = []
                for text, color in parts:
                    start = 0
                    for match in re.finditer(pattern, text):
                        new_parts.append((text[start:match.start()], color))
                        new_parts.append((match.group(), self.syntax_colors[color_key]))
                        start = match.end()
                    new_parts.append((text[start:], color))
                parts = new_parts
        
        return parts

    def wrap_text(self, text, max_width, font):
        words = text.split(' ')
        lines = []
        current_line = []
        current_width = 0
        
        for word in words:
            word_width = font.size(word + ' ')[0]
            if current_width + word_width <= max_width:
                current_line.append(word)
                current_width += word_width
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
                current_width = word_width
        
        if current_line:
            lines.append(' '.join(current_line))
        return lines

    def run_code(self, code):
        import debogger

        return debogger.run_student_code(code)

    def verif(self, code, output, niveau):
        if niveau == 1:
            if len(code) < 16:
                output_lines = output.split('\n')[1:-1]
                result = ["37.0", "38.0", "15.0", "27.0", "57.5", "181.0", "12.0"]
                if result == output_lines:
                    return True
            return False
        
    def niveau_1(self):
        # Constants for layout
        LEFT_PANEL_WIDTH = self.screen_w * 0.4
        RIGHT_PANEL_WIDTH = self.screen_w * 0.6
        CONSOLE_HEIGHT = self.screen_h * 0.3
        EDITOR_HEIGHT = self.screen_h - CONSOLE_HEIGHT
        button_width = 100
        button_height = 30

        for event in self.events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if not self.popup_text_show and not self.shown_popup:
                        self.mode = "menu"
                        self.code_text = [""]
                        self.cursor_pos = [0, 0]
                        self.scroll_offset = 0
                        self.cursor_timer = 0
                        self.cursor_visible = True
                        self.space_number = [0]
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
            "1. Écrivez une fonction qui calcule le triple d'un chiffre, soustrait la moitié du chiffre de départ et ajoute un autre nombre donné.",
            "2. Utilisez une fonction contenant 2 arguments et un retour.",
            "",
            "Conseils:",
            "- Pensez à regarder la catégorie avec les opérateurs.",
            "- N'oubliez pas de bien vérifier votre code.",
            "",
            "Test:",
            "Testez votre code avec les valeurs suivantes : (en une seule exécution)",
            "10 et 12 qui doit donner 37.0",
            "10 et 13 qui doit donner 38.0",
            "4 et 5 qui doit donner 15.0",
            "2 et 22",
            "5 et 45",
            "72 et 1",
            "2 et 7",
            "",
            "Contraintes:",
            "- Vous devez réaliser ce code en moins de 15 lignes de code et vous n'avez le droit qu'à une seule exécution pour compléter les demandes afin de passer au niveau suivant."

        ]

        instructions_height = self.screen_h * 0.5  # Height for instructions area
        buttons_height = self.screen_h * 0.4  # Height reserved for buttons
        
        instructions_surface = pg.Surface((LEFT_PANEL_WIDTH, instructions_height))
        instructions_surface.fill((40, 40, 40))
            
        wrapped_lines = []
        for instruction in instructions:
            wrapped_lines.extend(self.wrap_text(instruction, LEFT_PANEL_WIDTH - 40, self.font))
        
        total_height = len(wrapped_lines) * 30
        content_surface = pg.Surface((LEFT_PANEL_WIDTH, total_height))
        content_surface.fill((40, 40, 40))
        
        for i, line in enumerate(wrapped_lines):
            text = self.font.render(line, True, self.WHITE)
            content_surface.blit(text, (20, i * 30))
        
        for event in self.events:
            if event.type == pg.MOUSEWHEEL:
                if instructions_surface.get_rect().collidepoint(pg.mouse.get_pos()):
                    self.scroll_offset = max(min(0, self.scroll_offset + event.y * 30), 
                                        -max(0, total_height - instructions_height))
    


        # Buttons at bottom of left panel
        buttons = [
           ("Notions de base", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.1), "Notions essentielles pour débuter"),
            ("Variable", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.3), "Garder des informations en mémoire"),
            ("Conditionnelle", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.5), "Exécuter selon certains conditions"),
            ("Boucle for", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.7), "Répéter un certain nombre de fois"),
            ("Boucle while", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.9), "Répéter selon une condition")
        ]

        buttons_surface = pg.Surface((LEFT_PANEL_WIDTH, buttons_height))
        buttons_surface.fill((40, 40, 40))

        for text, pos, alt_text in buttons:
            button_width = LEFT_PANEL_WIDTH * 0.9
            button_height = buttons_height * 0.15

            mouse_pos = pg.mouse.get_pos()
            relative_mouse_pos = (mouse_pos[0], mouse_pos[1] - instructions_height)
            
            hover = (pos[0] <= relative_mouse_pos[0] <= pos[0] + button_width and 
                pos[1] <= relative_mouse_pos[1] <= pos[1] + button_height)

            button_surface = pg.Surface((LEFT_PANEL_WIDTH - pos[0]*2, 40))
            button_surface.fill(self.BLUE if not hover else self.DARK_BLUE)

            text_surface = self.font.render(alt_text, True, self.WHITE) if hover else self.font.render(text, True, self.WHITE)
            text_rect = text_surface.get_rect(center=((LEFT_PANEL_WIDTH - pos[0]*2)/2, 20))
            button_surface.blit(text_surface, text_rect)
            buttons_surface.blit(button_surface, pos)

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
        self.handle_code_editor(editor_surface, self.events)

        
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
        
        # Console button
        console_button_rect = pg.Rect(LEFT_PANEL_WIDTH + button_width + 30, EDITOR_HEIGHT + 10, button_width, button_height)
        console_color = self.DARK_BLUE if self.show_console else self.BLUE
        pg.draw.rect(self.screen, console_color, console_button_rect)
        console_text = self.font.render("Console", True, self.WHITE)
        console_rect = console_text.get_rect(center=console_button_rect.center)
        self.screen.blit(console_text, console_rect)

        # Handle button clicks
        mouse_pos = pg.mouse.get_pos()
        adjusted_pos = (mouse_pos[0] - LEFT_PANEL_WIDTH, mouse_pos[1])  # Adjust for right panel position

        if pg.mouse.get_pressed()[0]:
            if trace_button_rect.collidepoint(adjusted_pos):
                self.show_trace = True
                self.show_console = False
            elif console_button_rect.collidepoint(adjusted_pos):
                self.show_trace = False
                self.show_console = True
            elif 10 <= adjusted_pos[0] <= 50 and EDITOR_HEIGHT - 50 <= adjusted_pos[1] <= EDITOR_HEIGHT - 10:
                code = "\n".join(self.code_text)
                self.output = self.run_code(code)
                self.verif_result = self.verif(self.code_text, self.output, 1)

        if self.show_console:
            if not self.output: 
                console_text = self.font.render("Rien n'a été exécuté ici...", True, self.WHITE)
                console_surface.blit(console_text, (20, 20))
            else:

                console_x = LEFT_PANEL_WIDTH + 10
                console_y = EDITOR_HEIGHT
                console_rect = pg.Rect(console_x, console_y, RIGHT_PANEL_WIDTH - 20, CONSOLE_HEIGHT - 20)

                total_height_console = 0

                temp_y = 10
                output_lines = self.output.split('\n')

                for line in output_lines:
                    words = line.split()
                    current_line = []
                    current_width = 0
                    for word in words:
                        word_surface = self.font.render(word + ' ', True, self.WHITE)
                        word_width = word_surface.get_width()
                        if current_width + word_width <= RIGHT_PANEL_WIDTH - 40:
                            current_line.append(word)
                            current_width += word_width
                        else:
                            temp_y += 25
                            current_line = [word]
                            current_width = word_width
                    temp_y += 25
                total_height_console = temp_y

                for event in self.events:
                    if event.type == pg.MOUSEWHEEL:
                        mouse_pos = pg.mouse.get_pos()
                        if console_surface.get_rect().collidepoint(mouse_pos):
                            self.console_scroll_y += event.y * 20
                            # Limit scrolling
                            self.console_scroll_y = min(0, max((- total_height_console + CONSOLE_HEIGHT - 40), self.console_scroll_y + event.y * 30))

                y_offset = 10 + self.console_scroll_y

                if self.output.startswith("COULEURROUGEErreur"):
                    self.output = self.output.split("COULEURROUGE")[1]
                    words = self.output.split()
                    current_line = []
                    current_width = 0
                    
                    for word in words:
                        word_surface = self.font.render(word + ' ', True, self.WHITE)
                        word_width = word_surface.get_width()
                        
                        if current_width + word_width <= RIGHT_PANEL_WIDTH - 60:
                            current_line.append(word)
                            current_width += word_width
                        else:
                            error_surface = self.font.render(' '.join(current_line), True, self.WHITE, self.RED)
                            console_surface.blit(error_surface, (10, y_offset))
                            y_offset += 25
                            current_line = [word]
                            current_width = word_width
                    
                    if current_line:
                        error_surface = self.font.render(' '.join(current_line), True, self.WHITE, self.RED)
                        console_surface.blit(error_surface, (10, y_offset))
                    self.text_error = True
                else:
                    if self.output.startswith("Bon :"):
                        self.text_error = False
                        self.output = self.output.split("Bon :")[-1]
                    output_lines = self.output.split("\n")
                    for line in output_lines:
                        words = line.split()
                        current_line = []
                        current_width = 0
                        
                        for word in words:
                            word_surface = self.font.render(word + ' ', True, self.WHITE)
                            word_width = word_surface.get_width()
                            
                            if current_width + word_width <= RIGHT_PANEL_WIDTH - 40:
                                current_line.append(word)
                                current_width += word_width
                            else:
                                console_surface.blit(self.font.render(' '.join(current_line), True, 
                                                self.WHITE if not self.text_error else self.RED), 
                                                (10, y_offset))
                                y_offset += 25
                                current_line = [word]
                                current_width = word_width
                        
                        if current_line:
                            console_surface.blit(self.font.render(' '.join(current_line), True, 
                                            self.WHITE if not self.text_error else self.RED), 
                                            (10, y_offset))
                            y_offset += 25

                if total_height_console > CONSOLE_HEIGHT:
                    scrollbar_height = (CONSOLE_HEIGHT / total_height_console) * (CONSOLE_HEIGHT - 20)
                    scrollbar_pos = (-self.console_scroll_y / total_height_console) * (CONSOLE_HEIGHT - 20)
                    pg.draw.rect(console_surface, (100, 100, 100), 
                                (RIGHT_PANEL_WIDTH - 30, scrollbar_pos, 8, scrollbar_height),
                                border_radius=4)



        # Add components to right panel
        right_panel.blit(editor_surface, (10, 10))
        right_panel.blit(play_button, (10, EDITOR_HEIGHT - 50))
        right_panel.blit(slider_surface, (60, EDITOR_HEIGHT - 45))
        right_panel.blit(console_surface, (10, EDITOR_HEIGHT)) if self.show_console else None

        instructions_surface.blit(content_surface, (0, self.scroll_offset))

        if total_height > instructions_height:
            scrollbar_height = (instructions_height / total_height) * instructions_height
            scrollbar_pos = (-self.scroll_offset / total_height) * instructions_height
            
            # Draw scrollbar handle
            pg.draw.rect(instructions_surface, (100, 100, 100), 
                        (LEFT_PANEL_WIDTH - 10, scrollbar_pos, 8, scrollbar_height), border_radius=4)



        left_panel.blit(instructions_surface, (0, 0))

        left_panel.blit(buttons_surface, (0, instructions_height))


        # Add panels to main screen
        self.screen.blit(left_panel, (0, 0))

        if self.verif_result:
            # Position the button above console, on the right side
            next_button_rect = pg.Rect(RIGHT_PANEL_WIDTH - 170, EDITOR_HEIGHT - 50, 150, 40)
            
            # Draw button outline
            pg.draw.rect(right_panel, self.WHITE, next_button_rect, 3, border_radius=10)
            
            # Draw button background
            mouse_pos_adjusted = (pg.mouse.get_pos()[0] - LEFT_PANEL_WIDTH, pg.mouse.get_pos()[1])
            hover = next_button_rect.collidepoint(mouse_pos_adjusted)
            
            pg.draw.rect(right_panel, self.GREEN if not hover else self.DARK_GREEN, 
                        next_button_rect.inflate(-3, -3), border_radius=10)
            
            # Button text
            next_text = self.font.render("Niveau 2", True, self.WHITE)
            next_text_rect = next_text.get_rect(center=next_button_rect.center)
            right_panel.blit(next_text, next_text_rect)
            
            # Handle click with adjusted mouse position
            if hover and pg.mouse.get_pressed()[0]:
                self.niv = 2
                self.code_text = [""]
                self.cursor_pos = [0, 0]
                self.scroll_offset = 0
                self.cursor_timer = 0
                self.cursor_visible = True
                self.space_number = [0]
                self.output = None
                self.verif_result = False


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
        button_width = 100
        button_height = 30

        for event in self.events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if not self.popup_text_show and not self.shown_popup:
                        self.mode = "menu"
                        self.code_text = [""]
                        self.cursor_pos = [0, 0]
                        self.scroll_offset = 0
                        self.cursor_timer = 0
                        self.cursor_visible = True
                        self.space_number = [0]
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
            "1. Écrivez une fonction qui calcule le triple d'un chiffre, soustrait la moitié du chiffre de départ et ajoute un autre nombre donné.",
            "2. Utilisez une fonction contenant 2 arguments et un retour.",
            "",
            "Conseils:",
            "- Pensez à regarder la catégorie avec les opérateurs.",
            "- N'oubliez pas de bien vérifier votre code.",
            "",
            "Test:",
            "Testez votre code avec les valeurs suivantes : (en une seule exécution)",
            "10 et 12 qui doit donner 37.0",
            "10 et 13 qui doit donner 38.0",
            "4 et 5 qui doit donner 15.0",
            "2 et 22",
            "5 et 45",
            "72 et 1",
            "2 et 7",
            "",
            "Contraintes:",
            "- Vous devez réaliser ce code en moins de 15 lignes de code et vous n'avez le droit qu'à une seule exécution pour compléter les demandes afin de passer au niveau suivant."

        ]

        instructions_height = self.screen_h * 0.5  # Height for instructions area
        buttons_height = self.screen_h * 0.4  # Height reserved for buttons
        
        instructions_surface = pg.Surface((LEFT_PANEL_WIDTH, instructions_height))
        instructions_surface.fill((40, 40, 40))
            
        wrapped_lines = []
        for instruction in instructions:
            wrapped_lines.extend(self.wrap_text(instruction, LEFT_PANEL_WIDTH - 40, self.font))
        
        total_height = len(wrapped_lines) * 30
        content_surface = pg.Surface((LEFT_PANEL_WIDTH, total_height))
        content_surface.fill((40, 40, 40))
        
        for i, line in enumerate(wrapped_lines):
            text = self.font.render(line, True, self.WHITE)
            content_surface.blit(text, (20, i * 30))
        
        for event in self.events:
            if event.type == pg.MOUSEWHEEL:
                if instructions_surface.get_rect().collidepoint(pg.mouse.get_pos()):
                    self.scroll_offset = max(min(0, self.scroll_offset + event.y * 30), 
                                        -max(0, total_height - instructions_height))
    


        # Buttons at bottom of left panel
        buttons = [
           ("Notions de base", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.1), "Notions essentielles pour débuter"),
            ("Variable", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.3), "Garder des informations en mémoire"),
            ("Conditionnelle", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.5), "Exécuter selon certains conditions"),
            ("Boucle for", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.7), "Répéter un certain nombre de fois"),
            ("Boucle while", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.9), "Répéter selon une condition")
        ]

        buttons_surface = pg.Surface((LEFT_PANEL_WIDTH, buttons_height))
        buttons_surface.fill((40, 40, 40))

        for text, pos, alt_text in buttons:
            button_width = LEFT_PANEL_WIDTH * 0.9
            button_height = buttons_height * 0.15

            mouse_pos = pg.mouse.get_pos()
            relative_mouse_pos = (mouse_pos[0], mouse_pos[1] - instructions_height)
            
            hover = (pos[0] <= relative_mouse_pos[0] <= pos[0] + button_width and 
                pos[1] <= relative_mouse_pos[1] <= pos[1] + button_height)

            button_surface = pg.Surface((LEFT_PANEL_WIDTH - pos[0]*2, 40))
            button_surface.fill(self.BLUE if not hover else self.DARK_BLUE)

            text_surface = self.font.render(alt_text, True, self.WHITE) if hover else self.font.render(text, True, self.WHITE)
            text_rect = text_surface.get_rect(center=((LEFT_PANEL_WIDTH - pos[0]*2)/2, 20))
            button_surface.blit(text_surface, text_rect)
            buttons_surface.blit(button_surface, pos)

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
        self.handle_code_editor(editor_surface, self.events)

        
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
        
        # Console button
        console_button_rect = pg.Rect(LEFT_PANEL_WIDTH + button_width + 30, EDITOR_HEIGHT + 10, button_width, button_height)
        console_color = self.DARK_BLUE if self.show_console else self.BLUE
        pg.draw.rect(self.screen, console_color, console_button_rect)
        console_text = self.font.render("Console", True, self.WHITE)
        console_rect = console_text.get_rect(center=console_button_rect.center)
        self.screen.blit(console_text, console_rect)

        # Handle button clicks
        mouse_pos = pg.mouse.get_pos()
        adjusted_pos = (mouse_pos[0] - LEFT_PANEL_WIDTH, mouse_pos[1])  # Adjust for right panel position

        if pg.mouse.get_pressed()[0]:
            if trace_button_rect.collidepoint(adjusted_pos):
                self.show_trace = True
                self.show_console = False
            elif console_button_rect.collidepoint(adjusted_pos):
                self.show_trace = False
                self.show_console = True
            elif 10 <= adjusted_pos[0] <= 50 and EDITOR_HEIGHT - 50 <= adjusted_pos[1] <= EDITOR_HEIGHT - 10:
                code = "\n".join(self.code_text)
                self.output = self.run_code(code)
                self.verif_result = self.verif(self.code_text, self.output, 1)

        if self.show_console:
            if not self.output: 
                console_text = self.font.render("Rien n'a été exécuté ici...", True, self.WHITE)
                console_surface.blit(console_text, (20, 20))
            else:

                console_x = LEFT_PANEL_WIDTH + 10
                console_y = EDITOR_HEIGHT
                console_rect = pg.Rect(console_x, console_y, RIGHT_PANEL_WIDTH - 20, CONSOLE_HEIGHT - 20)

                total_height_console = 0

                temp_y = 10
                output_lines = self.output.split('\n')

                for line in output_lines:
                    words = line.split()
                    current_line = []
                    current_width = 0
                    for word in words:
                        word_surface = self.font.render(word + ' ', True, self.WHITE)
                        word_width = word_surface.get_width()
                        if current_width + word_width <= RIGHT_PANEL_WIDTH - 40:
                            current_line.append(word)
                            current_width += word_width
                        else:
                            temp_y += 25
                            current_line = [word]
                            current_width = word_width
                    temp_y += 25
                total_height_console = temp_y

                for event in self.events:
                    if event.type == pg.MOUSEWHEEL:
                        mouse_pos = pg.mouse.get_pos()
                        if console_surface.get_rect().collidepoint(mouse_pos):
                            self.console_scroll_y += event.y * 20
                            # Limit scrolling
                            self.console_scroll_y = min(0, max((- total_height_console + CONSOLE_HEIGHT - 40), self.console_scroll_y + event.y * 30))

                y_offset = 10 + self.console_scroll_y

                if self.output.startswith("COULEURROUGEErreur"):
                    self.output = self.output.split("COULEURROUGE")[1]
                    words = self.output.split()
                    current_line = []
                    current_width = 0
                    
                    for word in words:
                        word_surface = self.font.render(word + ' ', True, self.WHITE)
                        word_width = word_surface.get_width()
                        
                        if current_width + word_width <= RIGHT_PANEL_WIDTH - 60:
                            current_line.append(word)
                            current_width += word_width
                        else:
                            error_surface = self.font.render(' '.join(current_line), True, self.WHITE, self.RED)
                            console_surface.blit(error_surface, (10, y_offset))
                            y_offset += 25
                            current_line = [word]
                            current_width = word_width
                    
                    if current_line:
                        error_surface = self.font.render(' '.join(current_line), True, self.WHITE, self.RED)
                        console_surface.blit(error_surface, (10, y_offset))
                    self.text_error = True
                else:
                    if self.output.startswith("Bon :"):
                        self.text_error = False
                        self.output = self.output.split("Bon :")[-1]
                    output_lines = self.output.split("\n")
                    for line in output_lines:
                        words = line.split()
                        current_line = []
                        current_width = 0
                        
                        for word in words:
                            word_surface = self.font.render(word + ' ', True, self.WHITE)
                            word_width = word_surface.get_width()
                            
                            if current_width + word_width <= RIGHT_PANEL_WIDTH - 40:
                                current_line.append(word)
                                current_width += word_width
                            else:
                                console_surface.blit(self.font.render(' '.join(current_line), True, 
                                                self.WHITE if not self.text_error else self.RED), 
                                                (10, y_offset))
                                y_offset += 25
                                current_line = [word]
                                current_width = word_width
                        
                        if current_line:
                            console_surface.blit(self.font.render(' '.join(current_line), True, 
                                            self.WHITE if not self.text_error else self.RED), 
                                            (10, y_offset))
                            y_offset += 25

                if total_height_console > CONSOLE_HEIGHT:
                    scrollbar_height = (CONSOLE_HEIGHT / total_height_console) * (CONSOLE_HEIGHT - 20)
                    scrollbar_pos = (-self.console_scroll_y / total_height_console) * (CONSOLE_HEIGHT - 20)
                    pg.draw.rect(console_surface, (100, 100, 100), 
                                (RIGHT_PANEL_WIDTH - 30, scrollbar_pos, 8, scrollbar_height),
                                border_radius=4)



        # Add components to right panel
        right_panel.blit(editor_surface, (10, 10))
        right_panel.blit(play_button, (10, EDITOR_HEIGHT - 50))
        right_panel.blit(slider_surface, (60, EDITOR_HEIGHT - 45))
        right_panel.blit(console_surface, (10, EDITOR_HEIGHT)) if self.show_console else None

        instructions_surface.blit(content_surface, (0, self.scroll_offset))

        if total_height > instructions_height:
            scrollbar_height = (instructions_height / total_height) * instructions_height
            scrollbar_pos = (-self.scroll_offset / total_height) * instructions_height
            
            # Draw scrollbar handle
            pg.draw.rect(instructions_surface, (100, 100, 100), 
                        (LEFT_PANEL_WIDTH - 10, scrollbar_pos, 8, scrollbar_height), border_radius=4)



        left_panel.blit(instructions_surface, (0, 0))

        left_panel.blit(buttons_surface, (0, instructions_height))


        # Add panels to main screen
        self.screen.blit(left_panel, (0, 0))

        if self.verif_result:
            # Position the button above console, on the right side
            next_button_rect = pg.Rect(RIGHT_PANEL_WIDTH - 170, EDITOR_HEIGHT - 50, 150, 40)
            
            # Draw button outline
            pg.draw.rect(right_panel, self.WHITE, next_button_rect, 3, border_radius=10)
            
            # Draw button background
            mouse_pos_adjusted = (pg.mouse.get_pos()[0] - LEFT_PANEL_WIDTH, pg.mouse.get_pos()[1])
            hover = next_button_rect.collidepoint(mouse_pos_adjusted)
            
            pg.draw.rect(right_panel, self.GREEN if not hover else self.DARK_GREEN, 
                        next_button_rect.inflate(-3, -3), border_radius=10)
            
            # Button text
            next_text = self.font.render("Niveau 2", True, self.WHITE)
            next_text_rect = next_text.get_rect(center=next_button_rect.center)
            right_panel.blit(next_text, next_text_rect)
            
            # Handle click with adjusted mouse position
            if hover and pg.mouse.get_pressed()[0]:
                self.niv = 2
                self.code_text = [""]
                self.cursor_pos = [0, 0]
                self.scroll_offset = 0
                self.cursor_timer = 0
                self.cursor_visible = True
                self.space_number = [0]
                self.output = None
                self.verif_result = False


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
    
    def niveau_3(self):
        # Constants for layout
        LEFT_PANEL_WIDTH = self.screen_w * 0.4
        RIGHT_PANEL_WIDTH = self.screen_w * 0.6
        CONSOLE_HEIGHT = self.screen_h * 0.3
        EDITOR_HEIGHT = self.screen_h - CONSOLE_HEIGHT
        button_width = 100
        button_height = 30

        for event in self.events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if not self.popup_text_show and not self.shown_popup:
                        self.mode = "menu"
                        self.code_text = [""]
                        self.cursor_pos = [0, 0]
                        self.scroll_offset = 0
                        self.cursor_timer = 0
                        self.cursor_visible = True
                        self.space_number = [0]
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
            "1. Écrivez une fonction qui calcule le triple d'un chiffre, soustrait la moitié du chiffre de départ et ajoute un autre nombre donné.",
            "2. Utilisez une fonction contenant 2 arguments et un retour.",
            "",
            "Conseils:",
            "- Pensez à regarder la catégorie avec les opérateurs.",
            "- N'oubliez pas de bien vérifier votre code.",
            "",
            "Test:",
            "Testez votre code avec les valeurs suivantes : (en une seule exécution)",
            "10 et 12 qui doit donner 37.0",
            "10 et 13 qui doit donner 38.0",
            "4 et 5 qui doit donner 15.0",
            "2 et 22",
            "5 et 45",
            "72 et 1",
            "2 et 7",
            "",
            "Contraintes:",
            "- Vous devez réaliser ce code en moins de 15 lignes de code et vous n'avez le droit qu'à une seule exécution pour compléter les demandes afin de passer au niveau suivant."

        ]

        instructions_height = self.screen_h * 0.5  # Height for instructions area
        buttons_height = self.screen_h * 0.4  # Height reserved for buttons
        
        instructions_surface = pg.Surface((LEFT_PANEL_WIDTH, instructions_height))
        instructions_surface.fill((40, 40, 40))
            
        wrapped_lines = []
        for instruction in instructions:
            wrapped_lines.extend(self.wrap_text(instruction, LEFT_PANEL_WIDTH - 40, self.font))
        
        total_height = len(wrapped_lines) * 30
        content_surface = pg.Surface((LEFT_PANEL_WIDTH, total_height))
        content_surface.fill((40, 40, 40))
        
        for i, line in enumerate(wrapped_lines):
            text = self.font.render(line, True, self.WHITE)
            content_surface.blit(text, (20, i * 30))
        
        for event in self.events:
            if event.type == pg.MOUSEWHEEL:
                if instructions_surface.get_rect().collidepoint(pg.mouse.get_pos()):
                    self.scroll_offset = max(min(0, self.scroll_offset + event.y * 30), 
                                        -max(0, total_height - instructions_height))
    


        # Buttons at bottom of left panel
        buttons = [
           ("Notions de base", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.1), "Notions essentielles pour débuter"),
            ("Variable", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.3), "Garder des informations en mémoire"),
            ("Conditionnelle", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.5), "Exécuter selon certains conditions"),
            ("Boucle for", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.7), "Répéter un certain nombre de fois"),
            ("Boucle while", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.9), "Répéter selon une condition")
        ]

        buttons_surface = pg.Surface((LEFT_PANEL_WIDTH, buttons_height))
        buttons_surface.fill((40, 40, 40))

        for text, pos, alt_text in buttons:
            button_width = LEFT_PANEL_WIDTH * 0.9
            button_height = buttons_height * 0.15

            mouse_pos = pg.mouse.get_pos()
            relative_mouse_pos = (mouse_pos[0], mouse_pos[1] - instructions_height)
            
            hover = (pos[0] <= relative_mouse_pos[0] <= pos[0] + button_width and 
                pos[1] <= relative_mouse_pos[1] <= pos[1] + button_height)

            button_surface = pg.Surface((LEFT_PANEL_WIDTH - pos[0]*2, 40))
            button_surface.fill(self.BLUE if not hover else self.DARK_BLUE)

            text_surface = self.font.render(alt_text, True, self.WHITE) if hover else self.font.render(text, True, self.WHITE)
            text_rect = text_surface.get_rect(center=((LEFT_PANEL_WIDTH - pos[0]*2)/2, 20))
            button_surface.blit(text_surface, text_rect)
            buttons_surface.blit(button_surface, pos)

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
        self.handle_code_editor(editor_surface, self.events)

        
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
        
        # Console button
        console_button_rect = pg.Rect(LEFT_PANEL_WIDTH + button_width + 30, EDITOR_HEIGHT + 10, button_width, button_height)
        console_color = self.DARK_BLUE if self.show_console else self.BLUE
        pg.draw.rect(self.screen, console_color, console_button_rect)
        console_text = self.font.render("Console", True, self.WHITE)
        console_rect = console_text.get_rect(center=console_button_rect.center)
        self.screen.blit(console_text, console_rect)

        # Handle button clicks
        mouse_pos = pg.mouse.get_pos()
        adjusted_pos = (mouse_pos[0] - LEFT_PANEL_WIDTH, mouse_pos[1])  # Adjust for right panel position

        if pg.mouse.get_pressed()[0]:
            if trace_button_rect.collidepoint(adjusted_pos):
                self.show_trace = True
                self.show_console = False
            elif console_button_rect.collidepoint(adjusted_pos):
                self.show_trace = False
                self.show_console = True
            elif 10 <= adjusted_pos[0] <= 50 and EDITOR_HEIGHT - 50 <= adjusted_pos[1] <= EDITOR_HEIGHT - 10:
                code = "\n".join(self.code_text)
                self.output = self.run_code(code)
                self.verif_result = self.verif(self.code_text, self.output, 1)

        if self.show_console:
            if not self.output: 
                console_text = self.font.render("Rien n'a été exécuté ici...", True, self.WHITE)
                console_surface.blit(console_text, (20, 20))
            else:

                console_x = LEFT_PANEL_WIDTH + 10
                console_y = EDITOR_HEIGHT
                console_rect = pg.Rect(console_x, console_y, RIGHT_PANEL_WIDTH - 20, CONSOLE_HEIGHT - 20)

                total_height_console = 0

                temp_y = 10
                output_lines = self.output.split('\n')

                for line in output_lines:
                    words = line.split()
                    current_line = []
                    current_width = 0
                    for word in words:
                        word_surface = self.font.render(word + ' ', True, self.WHITE)
                        word_width = word_surface.get_width()
                        if current_width + word_width <= RIGHT_PANEL_WIDTH - 40:
                            current_line.append(word)
                            current_width += word_width
                        else:
                            temp_y += 25
                            current_line = [word]
                            current_width = word_width
                    temp_y += 25
                total_height_console = temp_y

                for event in self.events:
                    if event.type == pg.MOUSEWHEEL:
                        mouse_pos = pg.mouse.get_pos()
                        if console_surface.get_rect().collidepoint(mouse_pos):
                            self.console_scroll_y += event.y * 20
                            # Limit scrolling
                            self.console_scroll_y = min(0, max((- total_height_console + CONSOLE_HEIGHT - 40), self.console_scroll_y + event.y * 30))

                y_offset = 10 + self.console_scroll_y

                if self.output.startswith("COULEURROUGEErreur"):
                    self.output = self.output.split("COULEURROUGE")[1]
                    words = self.output.split()
                    current_line = []
                    current_width = 0
                    
                    for word in words:
                        word_surface = self.font.render(word + ' ', True, self.WHITE)
                        word_width = word_surface.get_width()
                        
                        if current_width + word_width <= RIGHT_PANEL_WIDTH - 60:
                            current_line.append(word)
                            current_width += word_width
                        else:
                            error_surface = self.font.render(' '.join(current_line), True, self.WHITE, self.RED)
                            console_surface.blit(error_surface, (10, y_offset))
                            y_offset += 25
                            current_line = [word]
                            current_width = word_width
                    
                    if current_line:
                        error_surface = self.font.render(' '.join(current_line), True, self.WHITE, self.RED)
                        console_surface.blit(error_surface, (10, y_offset))
                    self.text_error = True
                else:
                    if self.output.startswith("Bon :"):
                        self.text_error = False
                        self.output = self.output.split("Bon :")[-1]
                    output_lines = self.output.split("\n")
                    for line in output_lines:
                        words = line.split()
                        current_line = []
                        current_width = 0
                        
                        for word in words:
                            word_surface = self.font.render(word + ' ', True, self.WHITE)
                            word_width = word_surface.get_width()
                            
                            if current_width + word_width <= RIGHT_PANEL_WIDTH - 40:
                                current_line.append(word)
                                current_width += word_width
                            else:
                                console_surface.blit(self.font.render(' '.join(current_line), True, 
                                                self.WHITE if not self.text_error else self.RED), 
                                                (10, y_offset))
                                y_offset += 25
                                current_line = [word]
                                current_width = word_width
                        
                        if current_line:
                            console_surface.blit(self.font.render(' '.join(current_line), True, 
                                            self.WHITE if not self.text_error else self.RED), 
                                            (10, y_offset))
                            y_offset += 25

                if total_height_console > CONSOLE_HEIGHT:
                    scrollbar_height = (CONSOLE_HEIGHT / total_height_console) * (CONSOLE_HEIGHT - 20)
                    scrollbar_pos = (-self.console_scroll_y / total_height_console) * (CONSOLE_HEIGHT - 20)
                    pg.draw.rect(console_surface, (100, 100, 100), 
                                (RIGHT_PANEL_WIDTH - 30, scrollbar_pos, 8, scrollbar_height),
                                border_radius=4)



        # Add components to right panel
        right_panel.blit(editor_surface, (10, 10))
        right_panel.blit(play_button, (10, EDITOR_HEIGHT - 50))
        right_panel.blit(slider_surface, (60, EDITOR_HEIGHT - 45))
        right_panel.blit(console_surface, (10, EDITOR_HEIGHT)) if self.show_console else None

        instructions_surface.blit(content_surface, (0, self.scroll_offset))

        if total_height > instructions_height:
            scrollbar_height = (instructions_height / total_height) * instructions_height
            scrollbar_pos = (-self.scroll_offset / total_height) * instructions_height
            
            # Draw scrollbar handle
            pg.draw.rect(instructions_surface, (100, 100, 100), 
                        (LEFT_PANEL_WIDTH - 10, scrollbar_pos, 8, scrollbar_height), border_radius=4)



        left_panel.blit(instructions_surface, (0, 0))

        left_panel.blit(buttons_surface, (0, instructions_height))


        # Add panels to main screen
        self.screen.blit(left_panel, (0, 0))

        if self.verif_result:
            # Position the button above console, on the right side
            next_button_rect = pg.Rect(RIGHT_PANEL_WIDTH - 170, EDITOR_HEIGHT - 50, 150, 40)
            
            # Draw button outline
            pg.draw.rect(right_panel, self.WHITE, next_button_rect, 3, border_radius=10)
            
            # Draw button background
            mouse_pos_adjusted = (pg.mouse.get_pos()[0] - LEFT_PANEL_WIDTH, pg.mouse.get_pos()[1])
            hover = next_button_rect.collidepoint(mouse_pos_adjusted)
            
            pg.draw.rect(right_panel, self.GREEN if not hover else self.DARK_GREEN, 
                        next_button_rect.inflate(-3, -3), border_radius=10)
            
            # Button text
            next_text = self.font.render("Niveau 2", True, self.WHITE)
            next_text_rect = next_text.get_rect(center=next_button_rect.center)
            right_panel.blit(next_text, next_text_rect)
            
            # Handle click with adjusted mouse position
            if hover and pg.mouse.get_pressed()[0]:
                self.niv = 2
                self.code_text = [""]
                self.cursor_pos = [0, 0]
                self.scroll_offset = 0
                self.cursor_timer = 0
                self.cursor_visible = True
                self.space_number = [0]
                self.output = None
                self.verif_result = False


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
    
    def niveau_4(self):
        # Constants for layout
        LEFT_PANEL_WIDTH = self.screen_w * 0.4
        RIGHT_PANEL_WIDTH = self.screen_w * 0.6
        CONSOLE_HEIGHT = self.screen_h * 0.3
        EDITOR_HEIGHT = self.screen_h - CONSOLE_HEIGHT
        button_width = 100
        button_height = 30

        for event in self.events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if not self.popup_text_show and not self.shown_popup:
                        self.mode = "menu"
                        self.code_text = [""]
                        self.cursor_pos = [0, 0]
                        self.scroll_offset = 0
                        self.cursor_timer = 0
                        self.cursor_visible = True
                        self.space_number = [0]
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
            "1. Écrivez une fonction qui calcule le triple d'un chiffre, soustrait la moitié du chiffre de départ et ajoute un autre nombre donné.",
            "2. Utilisez une fonction contenant 2 arguments et un retour.",
            "",
            "Conseils:",
            "- Pensez à regarder la catégorie avec les opérateurs.",
            "- N'oubliez pas de bien vérifier votre code.",
            "",
            "Test:",
            "Testez votre code avec les valeurs suivantes : (en une seule exécution)",
            "10 et 12 qui doit donner 37.0",
            "10 et 13 qui doit donner 38.0",
            "4 et 5 qui doit donner 15.0",
            "2 et 22",
            "5 et 45",
            "72 et 1",
            "2 et 7",
            "",
            "Contraintes:",
            "- Vous devez réaliser ce code en moins de 15 lignes de code et vous n'avez le droit qu'à une seule exécution pour compléter les demandes afin de passer au niveau suivant."

        ]

        instructions_height = self.screen_h * 0.5  # Height for instructions area
        buttons_height = self.screen_h * 0.4  # Height reserved for buttons
        
        instructions_surface = pg.Surface((LEFT_PANEL_WIDTH, instructions_height))
        instructions_surface.fill((40, 40, 40))
            
        wrapped_lines = []
        for instruction in instructions:
            wrapped_lines.extend(self.wrap_text(instruction, LEFT_PANEL_WIDTH - 40, self.font))
        
        total_height = len(wrapped_lines) * 30
        content_surface = pg.Surface((LEFT_PANEL_WIDTH, total_height))
        content_surface.fill((40, 40, 40))
        
        for i, line in enumerate(wrapped_lines):
            text = self.font.render(line, True, self.WHITE)
            content_surface.blit(text, (20, i * 30))
        
        for event in self.events:
            if event.type == pg.MOUSEWHEEL:
                if instructions_surface.get_rect().collidepoint(pg.mouse.get_pos()):
                    self.scroll_offset = max(min(0, self.scroll_offset + event.y * 30), 
                                        -max(0, total_height - instructions_height))
    


        # Buttons at bottom of left panel
        buttons = [
           ("Notions de base", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.1), "Notions essentielles pour débuter"),
            ("Variable", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.3), "Garder des informations en mémoire"),
            ("Conditionnelle", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.5), "Exécuter selon certains conditions"),
            ("Boucle for", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.7), "Répéter un certain nombre de fois"),
            ("Boucle while", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.9), "Répéter selon une condition")
        ]

        buttons_surface = pg.Surface((LEFT_PANEL_WIDTH, buttons_height))
        buttons_surface.fill((40, 40, 40))

        for text, pos, alt_text in buttons:
            button_width = LEFT_PANEL_WIDTH * 0.9
            button_height = buttons_height * 0.15

            mouse_pos = pg.mouse.get_pos()
            relative_mouse_pos = (mouse_pos[0], mouse_pos[1] - instructions_height)
            
            hover = (pos[0] <= relative_mouse_pos[0] <= pos[0] + button_width and 
                pos[1] <= relative_mouse_pos[1] <= pos[1] + button_height)

            button_surface = pg.Surface((LEFT_PANEL_WIDTH - pos[0]*2, 40))
            button_surface.fill(self.BLUE if not hover else self.DARK_BLUE)

            text_surface = self.font.render(alt_text, True, self.WHITE) if hover else self.font.render(text, True, self.WHITE)
            text_rect = text_surface.get_rect(center=((LEFT_PANEL_WIDTH - pos[0]*2)/2, 20))
            button_surface.blit(text_surface, text_rect)
            buttons_surface.blit(button_surface, pos)

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
        self.handle_code_editor(editor_surface, self.events)

        
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
        
        # Console button
        console_button_rect = pg.Rect(LEFT_PANEL_WIDTH + button_width + 30, EDITOR_HEIGHT + 10, button_width, button_height)
        console_color = self.DARK_BLUE if self.show_console else self.BLUE
        pg.draw.rect(self.screen, console_color, console_button_rect)
        console_text = self.font.render("Console", True, self.WHITE)
        console_rect = console_text.get_rect(center=console_button_rect.center)
        self.screen.blit(console_text, console_rect)

        # Handle button clicks
        mouse_pos = pg.mouse.get_pos()
        adjusted_pos = (mouse_pos[0] - LEFT_PANEL_WIDTH, mouse_pos[1])  # Adjust for right panel position

        if pg.mouse.get_pressed()[0]:
            if trace_button_rect.collidepoint(adjusted_pos):
                self.show_trace = True
                self.show_console = False
            elif console_button_rect.collidepoint(adjusted_pos):
                self.show_trace = False
                self.show_console = True
            elif 10 <= adjusted_pos[0] <= 50 and EDITOR_HEIGHT - 50 <= adjusted_pos[1] <= EDITOR_HEIGHT - 10:
                code = "\n".join(self.code_text)
                self.output = self.run_code(code)
                self.verif_result = self.verif(self.code_text, self.output, 1)

        if self.show_console:
            if not self.output: 
                console_text = self.font.render("Rien n'a été exécuté ici...", True, self.WHITE)
                console_surface.blit(console_text, (20, 20))
            else:

                console_x = LEFT_PANEL_WIDTH + 10
                console_y = EDITOR_HEIGHT
                console_rect = pg.Rect(console_x, console_y, RIGHT_PANEL_WIDTH - 20, CONSOLE_HEIGHT - 20)

                total_height_console = 0

                temp_y = 10
                output_lines = self.output.split('\n')

                for line in output_lines:
                    words = line.split()
                    current_line = []
                    current_width = 0
                    for word in words:
                        word_surface = self.font.render(word + ' ', True, self.WHITE)
                        word_width = word_surface.get_width()
                        if current_width + word_width <= RIGHT_PANEL_WIDTH - 40:
                            current_line.append(word)
                            current_width += word_width
                        else:
                            temp_y += 25
                            current_line = [word]
                            current_width = word_width
                    temp_y += 25
                total_height_console = temp_y

                for event in self.events:
                    if event.type == pg.MOUSEWHEEL:
                        mouse_pos = pg.mouse.get_pos()
                        if console_surface.get_rect().collidepoint(mouse_pos):
                            self.console_scroll_y += event.y * 20
                            # Limit scrolling
                            self.console_scroll_y = min(0, max((- total_height_console + CONSOLE_HEIGHT - 40), self.console_scroll_y + event.y * 30))

                y_offset = 10 + self.console_scroll_y

                if self.output.startswith("COULEURROUGEErreur"):
                    self.output = self.output.split("COULEURROUGE")[1]
                    words = self.output.split()
                    current_line = []
                    current_width = 0
                    
                    for word in words:
                        word_surface = self.font.render(word + ' ', True, self.WHITE)
                        word_width = word_surface.get_width()
                        
                        if current_width + word_width <= RIGHT_PANEL_WIDTH - 60:
                            current_line.append(word)
                            current_width += word_width
                        else:
                            error_surface = self.font.render(' '.join(current_line), True, self.WHITE, self.RED)
                            console_surface.blit(error_surface, (10, y_offset))
                            y_offset += 25
                            current_line = [word]
                            current_width = word_width
                    
                    if current_line:
                        error_surface = self.font.render(' '.join(current_line), True, self.WHITE, self.RED)
                        console_surface.blit(error_surface, (10, y_offset))
                    self.text_error = True
                else:
                    if self.output.startswith("Bon :"):
                        self.text_error = False
                        self.output = self.output.split("Bon :")[-1]
                    output_lines = self.output.split("\n")
                    for line in output_lines:
                        words = line.split()
                        current_line = []
                        current_width = 0
                        
                        for word in words:
                            word_surface = self.font.render(word + ' ', True, self.WHITE)
                            word_width = word_surface.get_width()
                            
                            if current_width + word_width <= RIGHT_PANEL_WIDTH - 40:
                                current_line.append(word)
                                current_width += word_width
                            else:
                                console_surface.blit(self.font.render(' '.join(current_line), True, 
                                                self.WHITE if not self.text_error else self.RED), 
                                                (10, y_offset))
                                y_offset += 25
                                current_line = [word]
                                current_width = word_width
                        
                        if current_line:
                            console_surface.blit(self.font.render(' '.join(current_line), True, 
                                            self.WHITE if not self.text_error else self.RED), 
                                            (10, y_offset))
                            y_offset += 25

                if total_height_console > CONSOLE_HEIGHT:
                    scrollbar_height = (CONSOLE_HEIGHT / total_height_console) * (CONSOLE_HEIGHT - 20)
                    scrollbar_pos = (-self.console_scroll_y / total_height_console) * (CONSOLE_HEIGHT - 20)
                    pg.draw.rect(console_surface, (100, 100, 100), 
                                (RIGHT_PANEL_WIDTH - 30, scrollbar_pos, 8, scrollbar_height),
                                border_radius=4)



        # Add components to right panel
        right_panel.blit(editor_surface, (10, 10))
        right_panel.blit(play_button, (10, EDITOR_HEIGHT - 50))
        right_panel.blit(slider_surface, (60, EDITOR_HEIGHT - 45))
        right_panel.blit(console_surface, (10, EDITOR_HEIGHT)) if self.show_console else None

        instructions_surface.blit(content_surface, (0, self.scroll_offset))

        if total_height > instructions_height:
            scrollbar_height = (instructions_height / total_height) * instructions_height
            scrollbar_pos = (-self.scroll_offset / total_height) * instructions_height
            
            # Draw scrollbar handle
            pg.draw.rect(instructions_surface, (100, 100, 100), 
                        (LEFT_PANEL_WIDTH - 10, scrollbar_pos, 8, scrollbar_height), border_radius=4)



        left_panel.blit(instructions_surface, (0, 0))

        left_panel.blit(buttons_surface, (0, instructions_height))


        # Add panels to main screen
        self.screen.blit(left_panel, (0, 0))

        if self.verif_result:
            # Position the button above console, on the right side
            next_button_rect = pg.Rect(RIGHT_PANEL_WIDTH - 170, EDITOR_HEIGHT - 50, 150, 40)
            
            # Draw button outline
            pg.draw.rect(right_panel, self.WHITE, next_button_rect, 3, border_radius=10)
            
            # Draw button background
            mouse_pos_adjusted = (pg.mouse.get_pos()[0] - LEFT_PANEL_WIDTH, pg.mouse.get_pos()[1])
            hover = next_button_rect.collidepoint(mouse_pos_adjusted)
            
            pg.draw.rect(right_panel, self.GREEN if not hover else self.DARK_GREEN, 
                        next_button_rect.inflate(-3, -3), border_radius=10)
            
            # Button text
            next_text = self.font.render("Niveau 2", True, self.WHITE)
            next_text_rect = next_text.get_rect(center=next_button_rect.center)
            right_panel.blit(next_text, next_text_rect)
            
            # Handle click with adjusted mouse position
            if hover and pg.mouse.get_pressed()[0]:
                self.niv = 2
                self.code_text = [""]
                self.cursor_pos = [0, 0]
                self.scroll_offset = 0
                self.cursor_timer = 0
                self.cursor_visible = True
                self.space_number = [0]
                self.output = None
                self.verif_result = False


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

    def niveau_5(self):
        # Constants for layout
        LEFT_PANEL_WIDTH = self.screen_w * 0.4
        RIGHT_PANEL_WIDTH = self.screen_w * 0.6
        CONSOLE_HEIGHT = self.screen_h * 0.3
        EDITOR_HEIGHT = self.screen_h - CONSOLE_HEIGHT
        button_width = 100
        button_height = 30

        for event in self.events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if not self.popup_text_show and not self.shown_popup:
                        self.mode = "menu"
                        self.code_text = [""]
                        self.cursor_pos = [0, 0]
                        self.scroll_offset = 0
                        self.cursor_timer = 0
                        self.cursor_visible = True
                        self.space_number = [0]
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
            "1. Écrivez une fonction qui calcule le triple d'un chiffre, soustrait la moitié du chiffre de départ et ajoute un autre nombre donné.",
            "2. Utilisez une fonction contenant 2 arguments et un retour.",
            "",
            "Conseils:",
            "- Pensez à regarder la catégorie avec les opérateurs.",
            "- N'oubliez pas de bien vérifier votre code.",
            "",
            "Test:",
            "Testez votre code avec les valeurs suivantes : (en une seule exécution)",
            "10 et 12 qui doit donner 37.0",
            "10 et 13 qui doit donner 38.0",
            "4 et 5 qui doit donner 15.0",
            "2 et 22",
            "5 et 45",
            "72 et 1",
            "2 et 7",
            "",
            "Contraintes:",
            "- Vous devez réaliser ce code en moins de 15 lignes de code et vous n'avez le droit qu'à une seule exécution pour compléter les demandes afin de passer au niveau suivant."

        ]

        instructions_height = self.screen_h * 0.5  # Height for instructions area
        buttons_height = self.screen_h * 0.4  # Height reserved for buttons
        
        instructions_surface = pg.Surface((LEFT_PANEL_WIDTH, instructions_height))
        instructions_surface.fill((40, 40, 40))
            
        wrapped_lines = []
        for instruction in instructions:
            wrapped_lines.extend(self.wrap_text(instruction, LEFT_PANEL_WIDTH - 40, self.font))
        
        total_height = len(wrapped_lines) * 30
        content_surface = pg.Surface((LEFT_PANEL_WIDTH, total_height))
        content_surface.fill((40, 40, 40))
        
        for i, line in enumerate(wrapped_lines):
            text = self.font.render(line, True, self.WHITE)
            content_surface.blit(text, (20, i * 30))
        
        for event in self.events:
            if event.type == pg.MOUSEWHEEL:
                if instructions_surface.get_rect().collidepoint(pg.mouse.get_pos()):
                    self.scroll_offset = max(min(0, self.scroll_offset + event.y * 30), 
                                        -max(0, total_height - instructions_height))
    


        # Buttons at bottom of left panel
        buttons = [
           ("Notions de base", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.1), "Notions essentielles pour débuter"),
            ("Variable", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.3), "Garder des informations en mémoire"),
            ("Conditionnelle", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.5), "Exécuter selon certains conditions"),
            ("Boucle for", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.7), "Répéter un certain nombre de fois"),
            ("Boucle while", (LEFT_PANEL_WIDTH * 0.05, buttons_height * 0.9), "Répéter selon une condition")
        ]

        buttons_surface = pg.Surface((LEFT_PANEL_WIDTH, buttons_height))
        buttons_surface.fill((40, 40, 40))

        for text, pos, alt_text in buttons:
            button_width = LEFT_PANEL_WIDTH * 0.9
            button_height = buttons_height * 0.15

            mouse_pos = pg.mouse.get_pos()
            relative_mouse_pos = (mouse_pos[0], mouse_pos[1] - instructions_height)
            
            hover = (pos[0] <= relative_mouse_pos[0] <= pos[0] + button_width and 
                pos[1] <= relative_mouse_pos[1] <= pos[1] + button_height)

            button_surface = pg.Surface((LEFT_PANEL_WIDTH - pos[0]*2, 40))
            button_surface.fill(self.BLUE if not hover else self.DARK_BLUE)

            text_surface = self.font.render(alt_text, True, self.WHITE) if hover else self.font.render(text, True, self.WHITE)
            text_rect = text_surface.get_rect(center=((LEFT_PANEL_WIDTH - pos[0]*2)/2, 20))
            button_surface.blit(text_surface, text_rect)
            buttons_surface.blit(button_surface, pos)

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
        self.handle_code_editor(editor_surface, self.events)

        
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
        
        # Console button
        console_button_rect = pg.Rect(LEFT_PANEL_WIDTH + button_width + 30, EDITOR_HEIGHT + 10, button_width, button_height)
        console_color = self.DARK_BLUE if self.show_console else self.BLUE
        pg.draw.rect(self.screen, console_color, console_button_rect)
        console_text = self.font.render("Console", True, self.WHITE)
        console_rect = console_text.get_rect(center=console_button_rect.center)
        self.screen.blit(console_text, console_rect)

        # Handle button clicks
        mouse_pos = pg.mouse.get_pos()
        adjusted_pos = (mouse_pos[0] - LEFT_PANEL_WIDTH, mouse_pos[1])  # Adjust for right panel position

        if pg.mouse.get_pressed()[0]:
            if trace_button_rect.collidepoint(adjusted_pos):
                self.show_trace = True
                self.show_console = False
            elif console_button_rect.collidepoint(adjusted_pos):
                self.show_trace = False
                self.show_console = True
            elif 10 <= adjusted_pos[0] <= 50 and EDITOR_HEIGHT - 50 <= adjusted_pos[1] <= EDITOR_HEIGHT - 10:
                code = "\n".join(self.code_text)
                self.output = self.run_code(code)
                self.verif_result = self.verif(self.code_text, self.output, 1)

        if self.show_console:
            if not self.output: 
                console_text = self.font.render("Rien n'a été exécuté ici...", True, self.WHITE)
                console_surface.blit(console_text, (20, 20))
            else:

                console_x = LEFT_PANEL_WIDTH + 10
                console_y = EDITOR_HEIGHT
                console_rect = pg.Rect(console_x, console_y, RIGHT_PANEL_WIDTH - 20, CONSOLE_HEIGHT - 20)

                total_height_console = 0

                temp_y = 10
                output_lines = self.output.split('\n')

                for line in output_lines:
                    words = line.split()
                    current_line = []
                    current_width = 0
                    for word in words:
                        word_surface = self.font.render(word + ' ', True, self.WHITE)
                        word_width = word_surface.get_width()
                        if current_width + word_width <= RIGHT_PANEL_WIDTH - 40:
                            current_line.append(word)
                            current_width += word_width
                        else:
                            temp_y += 25
                            current_line = [word]
                            current_width = word_width
                    temp_y += 25
                total_height_console = temp_y

                for event in self.events:
                    if event.type == pg.MOUSEWHEEL:
                        mouse_pos = pg.mouse.get_pos()
                        if console_surface.get_rect().collidepoint(mouse_pos):
                            self.console_scroll_y += event.y * 20
                            # Limit scrolling
                            self.console_scroll_y = min(0, max((- total_height_console + CONSOLE_HEIGHT - 40), self.console_scroll_y + event.y * 30))

                y_offset = 10 + self.console_scroll_y

                if self.output.startswith("COULEURROUGEErreur"):
                    self.output = self.output.split("COULEURROUGE")[1]
                    words = self.output.split()
                    current_line = []
                    current_width = 0
                    
                    for word in words:
                        word_surface = self.font.render(word + ' ', True, self.WHITE)
                        word_width = word_surface.get_width()
                        
                        if current_width + word_width <= RIGHT_PANEL_WIDTH - 60:
                            current_line.append(word)
                            current_width += word_width
                        else:
                            error_surface = self.font.render(' '.join(current_line), True, self.WHITE, self.RED)
                            console_surface.blit(error_surface, (10, y_offset))
                            y_offset += 25
                            current_line = [word]
                            current_width = word_width
                    
                    if current_line:
                        error_surface = self.font.render(' '.join(current_line), True, self.WHITE, self.RED)
                        console_surface.blit(error_surface, (10, y_offset))
                    self.text_error = True
                else:
                    if self.output.startswith("Bon :"):
                        self.text_error = False
                        self.output = self.output.split("Bon :")[-1]
                    output_lines = self.output.split("\n")
                    for line in output_lines:
                        words = line.split()
                        current_line = []
                        current_width = 0
                        
                        for word in words:
                            word_surface = self.font.render(word + ' ', True, self.WHITE)
                            word_width = word_surface.get_width()
                            
                            if current_width + word_width <= RIGHT_PANEL_WIDTH - 40:
                                current_line.append(word)
                                current_width += word_width
                            else:
                                console_surface.blit(self.font.render(' '.join(current_line), True, 
                                                self.WHITE if not self.text_error else self.RED), 
                                                (10, y_offset))
                                y_offset += 25
                                current_line = [word]
                                current_width = word_width
                        
                        if current_line:
                            console_surface.blit(self.font.render(' '.join(current_line), True, 
                                            self.WHITE if not self.text_error else self.RED), 
                                            (10, y_offset))
                            y_offset += 25

                if total_height_console > CONSOLE_HEIGHT:
                    scrollbar_height = (CONSOLE_HEIGHT / total_height_console) * (CONSOLE_HEIGHT - 20)
                    scrollbar_pos = (-self.console_scroll_y / total_height_console) * (CONSOLE_HEIGHT - 20)
                    pg.draw.rect(console_surface, (100, 100, 100), 
                                (RIGHT_PANEL_WIDTH - 30, scrollbar_pos, 8, scrollbar_height),
                                border_radius=4)



        # Add components to right panel
        right_panel.blit(editor_surface, (10, 10))
        right_panel.blit(play_button, (10, EDITOR_HEIGHT - 50))
        right_panel.blit(slider_surface, (60, EDITOR_HEIGHT - 45))
        right_panel.blit(console_surface, (10, EDITOR_HEIGHT)) if self.show_console else None

        instructions_surface.blit(content_surface, (0, self.scroll_offset))

        if total_height > instructions_height:
            scrollbar_height = (instructions_height / total_height) * instructions_height
            scrollbar_pos = (-self.scroll_offset / total_height) * instructions_height
            
            # Draw scrollbar handle
            pg.draw.rect(instructions_surface, (100, 100, 100), 
                        (LEFT_PANEL_WIDTH - 10, scrollbar_pos, 8, scrollbar_height), border_radius=4)



        left_panel.blit(instructions_surface, (0, 0))

        left_panel.blit(buttons_surface, (0, instructions_height))


        # Add panels to main screen
        self.screen.blit(left_panel, (0, 0))

        if self.verif_result:
            # Position the button above console, on the right side
            next_button_rect = pg.Rect(RIGHT_PANEL_WIDTH - 170, EDITOR_HEIGHT - 50, 150, 40)
            
            # Draw button outline
            pg.draw.rect(right_panel, self.WHITE, next_button_rect, 3, border_radius=10)
            
            # Draw button background
            mouse_pos_adjusted = (pg.mouse.get_pos()[0] - LEFT_PANEL_WIDTH, pg.mouse.get_pos()[1])
            hover = next_button_rect.collidepoint(mouse_pos_adjusted)
            
            pg.draw.rect(right_panel, self.GREEN if not hover else self.DARK_GREEN, 
                        next_button_rect.inflate(-3, -3), border_radius=10)
            
            # Button text
            next_text = self.font.render("Niveau 2", True, self.WHITE)
            next_text_rect = next_text.get_rect(center=next_button_rect.center)
            right_panel.blit(next_text, next_text_rect)
            
            # Handle click with adjusted mouse position
            if hover and pg.mouse.get_pressed()[0]:
                self.niv = 2
                self.code_text = [""]
                self.cursor_pos = [0, 0]
                self.scroll_offset = 0
                self.cursor_timer = 0
                self.cursor_visible = True
                self.space_number = [0]
                self.output = None
                self.verif_result = False


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

    def niveau_fini(self):
        if not self.fin:
            choix = random.randint(1, 2) 
            pg.mixer_music.load(f"music/Fin/win{choix}.mp3")
            pg.mixer_music.set_volume(1) if choix == 1 else pg.mixer_music.set_volume(0.1)
            pg.mixer_music.play(-1)
        self.fin = True


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
                crumble_img = pg.image.load('./img/fusion.png').convert_alpha()
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
