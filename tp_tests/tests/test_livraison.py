from app.livraison import frais_livraison

def test_livraison_panier_ordinaire():
    # Arrange
    montant = 0
    # Act
    resultat = frais_livraison(montant)
    # Assert
    assert resultat == 25
