# ================================
# Introduction au monde
# ================================

def introduction():
    print("Bienvenue dans le monde magique de Poudlard !")
    print("Une aventure extraordinaire commence…")
    input("Appuie sur Entrée pour continuer...")

# ================================
# Création du personnage
# ================================

def creer_personnage():
    # nom prénom
    nom = input("Entrez le nom de votre personnage : ")
    prenom = input("Entrez le prénom de votre personnage : ")

    print("Choisissez vos attributs (entre 1 et 10) :")

    courage = int(input("Niveau de courage (1-10) : "))
    intelligence = int(input("Niveau d’intelligence (1-10) : "))
    loyaute = int(input("Niveau de loyauté (1-10) : "))
    ambition = int(input("Niveau d’ambition (1-10) : "))

    # dictionnaire des attributs
    attributs = {
        "courage": courage,
        "intelligence": intelligence,
        "loyauté": loyaute,
        "ambition": ambition
    }

    # création du perso
    joueur = initialiser_personnage(nom, prenom, attributs)

    # affichage du perso
    afficher_personnage(joueur)

    return joueur