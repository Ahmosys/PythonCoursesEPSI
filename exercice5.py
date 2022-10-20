"""Exercice 5
"""

def print_addition() -> None:
    """Affiche les variables sans les additionner.
    """
    a, b, c = 2, 6, 3
    print(a, b, c, sep=" + ")
    print(f"{a} + {b} + {c}")
    
if __name__ == "__main__":
    print_addition()
