import random

bye_count = 0

print("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!")

while True:
    phrase = input("> ")

    if phrase == "ПОКА!":
        bye_count += 1
        if bye_count == 3:
            print("ДО СВИДАНИЯ, МИЛЫЙ!")
            break
        print(f"НЕТ, НИ РАЗУ С {random.randint(1930, 1950)} ГОДА!")
    elif phrase.isupper():
        bye_count = 0
        print(f"НЕТ, НИ РАЗУ С {random.randint(1930, 1950)} ГОДА!")
    else:
        bye_count = 0
        print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")
