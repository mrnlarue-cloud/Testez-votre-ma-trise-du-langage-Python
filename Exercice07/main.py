def square(number):
    # Vérifie si la valeur donnée est bien un nombre
    if not isinstance(number, (int, float)):
        # Affiche un message d'erreur si ce n'est pas un nombre
        print("Le paramètre doit être un nombre !")
        return None

    # Retourne le carré du nombre
    return number ** 2
