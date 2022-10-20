"""Exercice 8 (Tri alphabétique de la chaîne + Calcul de volumes)
"""

import mathyui

from colorama import Fore


def worker():
    """Fonction principale.
    """
    while True:
        clear()
        print(f"{Fore.CYAN}Que voulez-vous calculer (1. Sphère, 2. Parallélépipède) ? \n{Fore.RESET}")
        choice_user = input("[>>] ")
        clear()
        if not choice_user.isdigit():
            print(f"{Fore.RED}[-] Vous devez saisir un nombre.{Fore.RESET}")
        elif choice_user not in ["1", "2"]:
            print(f"{Fore.RED}[-] Vous devez saisir un nombre entre 1 et 2.{Fore.RESET}")
        elif choice_user == "1":
            rayon = int(input("Saisissez le rayon de votre sphère: "))
            resultat_calcul = (4/3) * math.pi * pow(rayon, 3)
            print(f"Le résultat du calcul du volume de la sphère est: {resultat_calcul}")
        elif choice_user == "2":
            largeur = int(input("Saisissez la largeur de votre parallélépipède: "))
            longueur = int(input("Saisissez la longueur de votre parallélépipède: "))
            hauteur = int(input("Saisissez la hauteur de votre parallélépipède: "))
            resultat_calcul = largeur * longueur * hauteur
            print(f"Le résultat du calcul du volume du parallélépipède est: {resultat_calcul}")
        time.sleep(3)
        clear()
            

def clear():
    """Permet de vider le terminal.
    """
    os.system("cls" if os.name == "nt" else "clear")

def sort_list() -> None:
    """Tri la chaîne par ordre alphabétique.
    """
    fruits = "Pomme, Abricot, Cerise, Fraise, Orange"
    fruits_list = fruits.split(", ")
    fruits_list.sort()
    final_str = ", ".join(fruits_list)
    print(final_str)
    
if __name__ == "__main__":
    worker()
