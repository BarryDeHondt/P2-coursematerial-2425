import pytest
from book import Book




@pytest.mark.parametrize('title, isbn', [
    ("Watchmen", "978-1779501127"),
    ("Clean Code", "978-0132350884"),
    ("The Pragmatic Programmer", "9780135957059"),
    ("Refactoring", "978-0201485677"),
    ("Python Tricks", "978-1775093307"),
])
def test_valid_creation(title, isbn):
    book = Book(title, isbn)
    
    assert book.title == title
    assert book.isbn == isbn



@pytest.mark.parametrize("invalid_title", [
    "",          # leeg
    " ",         # enkel spatie
    "\n\t",      # whitespace
])
def test_creation_with_invalid_title(invalid_title):
    with pytest.raises(RuntimeError):
        Book(invalid_title, "978-0132350884")



@pytest.mark.parametrize("invalid_isbn", [
    "978-0132350885",        # verkeerde checksum
    "978013235088",          # 12 cijfers
    "97801323508845",        # 14 cijfers
    "97801323A0884",         # bevat een letter
    "978 0132 3508 84",      # correcte hoeveelheid cijfers maar verkeerde checksum
    "",                      # lege string
    "   ",                   # spaties
])
def test_creation_with_invalid_isbn(invalid_isbn):
    with pytest.raises(RuntimeError):
        Book("Valid Title", invalid_isbn)