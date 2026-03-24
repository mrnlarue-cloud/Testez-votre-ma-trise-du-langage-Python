words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

voyelles = "aeiouy"

resultats = []

for mot in words:
    count = 0
    for lettre in mot:
        if lettre in voyelles:
            count += 1
    resultats.append((mot, count))

print(resultats)
