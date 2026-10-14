import random
from pathlib import Path

WORDS_FILE = Path(__file__).with_name("words.txt")
HANGMAN_DIR = Path(__file__).with_name("hangman")

def load_words():
    return [word.strip().lower() for word in WORDS_FILE.read_text(encoding="utf-8").splitlines() if word.strip()]

def load_stage(stage):
    return (HANGMAN_DIR / f"{stage}.txt").read_text(encoding="utf-8")

def choose_word(words):
    return random.choice(words)

def hidden_word(word, guessed):
    return "".join(letter if letter in guessed else "_" for letter in word)

def valid_guess(guess, guessed):
    return len(guess) == 1 and guess.isalpha() and guess not in guessed

def play_game():
    words = load_words()
    word = choose_word(words)
    guessed = set()
    wrong = 0
    max_wrong = 6

    print("Игра «Виселица на поле чудес»")
    print("Угадайте слово по буквам.")
    print(hidden_word(word, guessed))

    while wrong < max_wrong:
        guess = input("Введите букву: ").strip().lower()

        if not valid_guess(guess, guessed):
            print("Введите одну ещё не названную букву.")
            continue

        guessed.add(guess)

        if guess in word:
            print("Есть такая буква!")
        else:
            wrong += 1
            print("Такой буквы нет.")
            print(load_stage(wrong))

        current = hidden_word(word, guessed)
        print(current)

        if "_" not in current:
            print("Поздравляем! Вы угадали слово:", word)
            return

    print("Вы проиграли. Загаданное слово:", word)
