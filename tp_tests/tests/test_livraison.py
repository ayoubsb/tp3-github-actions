import pytest
from app.livraison import frais_livraison

def test_livraison_panier_ordinaire():
    montant = 120
    resultat = frais_livraison(montant)
    assert resultat == 25  # Adapter au tarif défini dans ton TP2

def test_livraison_montant_invalide():
    with pytest.raises(ValueError):
        frais_livraison(0)