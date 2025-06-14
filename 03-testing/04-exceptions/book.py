



class Book():
    def __init__(self, title, isbn):
        
        if not title.strip():
            raise RuntimeError("Title mag niet leeg zijn.")
        if not self._is_valid_isbn13(isbn):
            raise RuntimeError("Ongeldige ISBN.")
        
        self.__title = title
        self.__isbn = isbn
        
        
    @property
    def title(self):
        return self.__title
    
    @property
    def isbn(self):
        return self.__isbn
    
    def _is_valid_isbn13(self, isbn):

        cleaned = isbn.replace('-', '').replace(' ', '')
        if len(cleaned) != 13 or not cleaned.isdigit():
            return False

        total = 0
        for i in range(13):
            digit = int(cleaned[i])
            if i % 2 == 0:
                total += digit
            else:
                total += 3 * digit

        return total % 10 == 0


book = Book("Watchmen", "978-1779501127")  # Geldig
print(book.title)  # Watchmen
print(book.isbn)   # 978-1779501127

# invalid = Book("Watchmen", "978-1779501128")  # RuntimeError