import pytest
from parentheses import matching_parentheses



@pytest.mark.parametrize('string', [
    '',
    '()',
    '(())',
    '()()()',
    '(())()',
])

def test_matching_parentheses_valid(string):
    assert matching_parentheses(string)

@pytest.mark.parametrize("string", [
    "(",         # Alleen een open haakje
    ")",         # Alleen een sluitend haakje
    "(()",       # Eén open haakje teveel
    "())",       # Eén sluitend haakje teveel
    "())(",      # Verkeerde volgorde
    ")(",        # Gesloten voordat geopend
])
def test_matching_parentheses_invalid(string):
    assert not matching_parentheses(string)