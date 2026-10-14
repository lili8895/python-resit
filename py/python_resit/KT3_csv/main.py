def get_books(filename):
    with open(filename, encoding="utf-8") as file:
        lines = file.read().splitlines()

    rows = list(map(lambda line: line.split("|"), lines[1:]))

    return list(map(
        lambda row: [row[0], row[1], row[2], int(row[3]), float(row[4])],
        rows
    ))


def filtered_books(books, text):
    text = text.lower()

    selected = list(filter(
        lambda book: text in book[1].lower(),
        books
    ))

    return list(map(
        lambda book: [book[0], f"{book[1]}, {book[2]}", book[3], book[4]],
        selected
    ))


def books_to_amounts(books):
    return list(map(
        lambda book: (book[0], book[2] * book[3]),
        books
    ))


if __name__ == "__main__":
    books = get_books("books.csv")
    print("Задание 1:")
    print(books)

    python_books = filtered_books(books, "python")
    print("\nЗадание 2:")
    print(python_books)

    amounts = books_to_amounts(books)
    print("\nЗадание 3:")
    print(amounts)
