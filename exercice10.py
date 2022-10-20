"""Exercice 10 (Générateur de lancé de dès)
"""

import random
import math

def throw_dice() -> int:
    """Lance un dès à 6 faces et retourne une valeur d'une face aléatoirement.

    Returns:
        int: Retourne la valeur sur lequel le dès est tomber.
    """
    return random.randint(1, 6)

def simulate_throw_dice(nb_throw: int) -> int:
    """Simule un nombre lancé et en fait la moyenne.
    Args:
        nb_throw (int): Nombre de lancés.

    Returns:
        int: Face la plus tombé en moyenne.
    """
    sum = 0
    for _ in range(nb_throw):
        sum += random.randint(0, 6)
    return round(sum / nb_throw)
    
if __name__ == "__main__":
    # print(throw_dice())
    # print(simulate_throw_dice(1000))