class Book:
    def __init__(self, title, author, year):
        # Infos du livre
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        # Livres dispo
        self.books = []
        # Livres empruntés
        self.borrowed_books = []

    def add_book(self, book):
        # Ajoute un livre à la bibliothèque
        self.books.append(book)

    def remove_book(self, book_title):
        # Supprime un livre par son titre
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                break

    def borrow_book(self, book_title):
        # Déplace un livre de books vers borrowed_books
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrowed_books.append(book)
                break

    def return_book(self, book_title):
        # Remet un livre emprunté dans les livres dispo
        for book in self.borrowed_books:
            if book.title == book_title:
                self.borrowed_books.remove(book)
                self.books.append(book)
                break

    def available_books(self):
        # Retourne les titres des livres disponibles
        return [book.title for book in self.books]

    def borrowed_books_list(self):
        # Retourne les titres des livres empruntés
        return [book.title for book in self.borrowed_books]
