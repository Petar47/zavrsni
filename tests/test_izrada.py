from ..semanticka_tablica import *
from ..dnfiknf import *
from ..logickaekvivalencija import *
import pytest

@pytest.mark.parametrize("sud, atomi, ocekivani_dnff, ocekivani_knff", [
    ([{'A': False, 'B': False, 'A∨B': False}, {'A': False, 'B': True, 'A∨B': True}, {'A': True, 'B': False, 'A∨B': True}, {'A': True, 'B': True, 'A∨B': True}], 2, "(¬A∧B)(A∧¬B)(A∧B)", "(¬A∨¬B)"),
])
def test_dnfiknff(sud, atomi, ocekivani_dnff, ocekivani_knff):
    dnff, knff = dnfiknff(sud, atomi)
    assert knff == ocekivani_knff
    
@pytest.mark.parametrize("sud, kombinacija, ocekivani_rezultat", [
    (['A', '|', 'B'], {'A': False, 'B': False},{'A': False, 'B': False, 'A∨B': False}),  
    (['A', '|', 'B'], {'A': True, 'B': True},{'A': True, 'B': True,'A∨B': True}),  
])
def test_semanticka(sud,kombinacija,ocekivani_rezultat):
    rez = semanticka(sud,kombinacija)
    assert rez == ocekivani_rezultat

    
@pytest.mark.parametrize("sud, atomi, sudd, atomii, ocekivani_rezultat", [
    ("A | B", 2, "B | A", 2, True),  
    ("A & B", 2, "A | B", 2, False),  
])
def test_logicka_ekvivalencija(sud, atomi, sudd, atomii, ocekivani_rezultat):
    rezultat = logickaekvivalencija(sud, atomi, sudd, atomii)
    assert rezultat == ocekivani_rezultat
