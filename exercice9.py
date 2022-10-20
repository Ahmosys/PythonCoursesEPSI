"""Exercice 9 (Déclaration et initialisation de liste)
"""

list_number_of_10_to_100 = list(range(10, 101))
list_number_of_even_until_100 = [i for i in range(201) if i % 2 == 0]

print(f"""
{list_number_of_10_to_100}

{list_number_of_even_until_100}      
""")
