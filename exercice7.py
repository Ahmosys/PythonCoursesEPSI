"""Exercice 7
"""

def is_type(value, type) -> None:
    """Vérifie si l'argument passer en paramètre de fonction est une instance d'un certain type.

    Args:
        value (any): la valeur voulant être vérifier.
    """
    if isinstance(value, type):
        print(f"Votre variable est une bien du type ({type}).")
    else:
        print(f"Votre variable n'est pas du type {type}.")


def ask_type_test() -> None:
    """Demande à l'utilisateur quel type il veut comparer avec sa variable.
    """
    print("1. String, 2. Integer, 3. Float, 4. List, 5. Tuple\n")
    user_choice = input("[+] Qu'elle type voulez vous tester sur votre variable ? : ")
    if not user_choice.isdigit() or user_choice not in ["1", "2", "3", "4", "5"]:
        print("[-] Veuillez spécifier un nombre entre 1 et 5.")
    else:
        value = "Ma valeur voulant être tester."
        dict_choices =  {
            "1": str,
            "2": int,
            "3": float,
            "4": list,
            "5": tuple
        }
        is_type(value, dict_choices.get(user_choice))
        

if __name__ == "__main__":
    ask_type_test()