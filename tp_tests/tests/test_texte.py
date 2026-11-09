import pytest
from app.texte import nettoyer_texte


@pytest.mark.parametrize("entree, attendu", [
    ("  BONJOUR   monde  ", "bonjour monde"),
    (" déjà propre ", "déjà propre"),
    ("     ", ""),
    ("PYTHON", "python"),
])
def test_nettoyer_texte(entree, attendu):
    assert nettoyer_texte(entree) == attendu


def test_nettoyer_texte_entier():
    with pytest.raises(TypeError):
        nettoyer_texte(123)


def test_nettoyer_texte_none():
    with pytest.raises(TypeError):
        nettoyer_texte(None)


def test_nettoyer_deux_fois_donne_le_meme_resultat():
    texte = "  BONJOUR   monde  "

    premier_nettoyage = nettoyer_texte(texte)
    deuxieme_nettoyage = nettoyer_texte(premier_nettoyage)

    assert deuxieme_nettoyage == premier_nettoyage