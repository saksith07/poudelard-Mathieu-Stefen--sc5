def initialiser_personnage(nom, prenom, attributs):
    liste_inventaire = []
    liste_sortilege = []
    argent = 100
    joueur = {
        "Nom": nom,
        "Prenom": prenom,
        "Argent": argent,
        "Inventaire": liste_inventaire,
        "Sortilèges": liste_sortilege,
        "Attributs": attributs
    }

    return joueur

def afficher_personnage(joueur):
    print("Profil du personnage :")

    for cle in joueur:
        valeur = joueur[cle]

        if isinstance(valeur, dict):
            print(f"{cle} :")
            for sous_cle in valeur:
                print(f"- {sous_cle} : {valeur[sous_cle]}")

        elif isinstance(valeur, list):
            if valeur:
                print(f"{cle} : {', '.join(valeur)}")
            else:
                print(f"{cle} :")

        else:
            print(f"{cle} : {valeur}")