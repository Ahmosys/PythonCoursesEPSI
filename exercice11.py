"""Exercice 11 (Compter le nombre d’occurrences d'une lettre dans une chaîne)
"""

def count_nb_occurrence_in_str(text: str, letter_to_count: str) -> int:
    """Retourne le nombre de fois qu'une lettre se trouve dans une chaîne de caractère.

    Args:
        text (str): Texte voulant être compter.
        letter_to_count (str): La lettre.

    Returns:
        int: Nombre de fois que la lettre est dans la chaîne.
    """
    return text.lower().count(letter_to_count.lower())


def most_numerous_letter_in_str(text: str) -> str:
    """Retourne le caractère étant le plus présent dans la chaîne.

    Args:
        text (str): Texte voulant être compter.

    Returns:
        str: La lettre là plus présente.
    """
    dict_letters = {}
    for letter in text:
        if letter in dict_letters:
            dict_letters[letter] += 1
        else:
            dict_letters[letter] = 1
    return max(dict_letters, key=dict_letters.get)
          

def add_letter_between_each_char(text: str, char: str) -> str:
    """Remplace une lettre dans la chaîne de caractère par une autre valeur (chiffrage)

    Args:
        text (str): Texte voulant être "chiffrer".
        char (str): Caractère cibler par le "chiffrement".

    Returns:
        str: Le texte chiffrer.
    """
    return text.replace(char, f"{char}!@Q")
        
    
if __name__ == "__main__":
    # print(add_letter_between_each_char("testes", "e"))