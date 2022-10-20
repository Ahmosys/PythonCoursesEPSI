"""Exercice 1
"""

def initialize_variable() -> None:
    """Test declaration et initialisation des différent types de variables.
    """
    prenom = "Pierre"
    age = 20
    majeur = True
    compte_en_banque = 20135.284
    amies = ["Marie", "Julien", "Adrien"]
    parents = ("Marc", "Caroline")
    print(f"""
Prénom: {prenom}
Age: {age}
Majeur?: {majeur}
Solde compte: {compte_en_banque}
""")
    for ami in amies:
        print(ami)
    for parent in parents:
        print(parent)
    