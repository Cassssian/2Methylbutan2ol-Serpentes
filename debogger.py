import io
import sys
import traceback

def run_student_code(code):
    
    stdout = io.StringIO()
    sys.stdout = stdout
    
    try:
        exec(code)
        output = stdout.getvalue()
        
        if output:
            return f"Bon :\n{output}"
        else:
            return "Bon :Le code s'est exécuté mais n'a rien affiché. N'oublie pas d'utiliser print() !"

    except NameError as e:
        var = str(e).split("'")[1]
        tb = traceback.extract_tb(sys.exc_info()[2])
        line_no = tb[-1].lineno
        return f"COULEURROUGEErreur ligne {line_no}: Tu utilises '{var}' mais tu ne l'as pas défini avant. Vérifie que tu as bien créé cette variable."
        
    except SyntaxError as e:
        line_no = e.lineno
        return f"COULEURROUGEErreur ligne {line_no}: Il y a une erreur dans l'écriture de ton code. Vérifie la syntaxe (parenthèses, deux points, etc)."
        
    except IndentationError as e:
        line_no = e.lineno
        return f"COULEURROUGEErreur ligne {line_no}: L'indentation n'est pas correcte. Vérifie les espaces au début des lignes."
        
    except TypeError as e:
        tb = traceback.extract_tb(sys.exc_info()[2])
        line_no = tb[-1].lineno
        return f"COULEURROUGEErreur ligne {line_no}: Tu mélanges des types différents (texte, nombres...). Vérifie que tu utilises les bonnes opérations ou que les deux éléments soient du même type."
        
    except ZeroDivisionError as e:
        tb = traceback.extract_tb(sys.exc_info()[2])
        line_no = tb[-1].lineno
        return f"COULEURROUGEErreur ligne {line_no}: Tu essaies de diviser par zéro, ce qui n'est pas possible en mathématiques."
        
    except ValueError as e:
        tb = traceback.extract_tb(sys.exc_info()[2])
        line_no = tb[-1].lineno
        error_msg = str(e)
        if "invalid literal for int()" in error_msg:
            return f"COULEURROUGEErreur ligne {line_no}: Tu essaies de convertir '{error_msg.split(chr(39))[1]}' en nombre entier, mais ce n'est pas possible car ce n'est pas un nombre."
        elif "could not convert string to float" in error_msg:
            return f"COULEURROUGEErreur ligne {line_no}: Tu essaies de convertir '{error_msg.split(chr(39))[1]}' en nombre décimal, mais ce n'est pas possible car ce n'est pas un nombre."
        elif "invalid literal for float()" in error_msg:
            return f"COULEURROUGEErreur ligne {line_no}: Tu essaies de convertir '{error_msg.split(chr(39))[1]}' en nombre décimal, mais ce n'est pas possible car ce n'est pas un nombre."
        else:
            return f"COULEURROUGEErreur ligne {line_no}: La valeur que tu utilises n'est pas du bon type. Message d'erreur: {error_msg}"
        
    except Exception as e:
        tb = traceback.extract_tb(sys.exc_info()[2])
        line_no = tb[-1].lineno
        return f"COULEURROUGEUne erreur s'est produite ligne {line_no}: {str(e)}"


    
    finally:
        
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    
    test_codes = [
        
        """
def calcul(x, y):
    return x * 3 - x/2 + y
print(calcul(10, 12))
print(calcul(10, 13))
print(calcul(4, 5))
        """,
        
        # Cas d'erreur
        "print(x)",  # NameError
        "print('hello'",  # SyntaxError
        "if True:\nprint('no indent')",  # IndentationError
        "print(5 + 'texte')",  # TypeError
        "print(5/0)",  # ZeroDivisionError
        "float('abc')"  # ValueError
    ]
    
    for code in test_codes:
        print("\nTest du code:")
        print(code)
        print("-" * 40)
        print(run_student_code(code))
        print("=" * 40)