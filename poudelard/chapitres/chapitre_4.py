import random
from utils.input_utils import load_fichier
from univers.maison import actualiser_points_maison, afficher_maison_gagnante
from univers.personnage import afficher_personnage

def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None):

    equipe = {
        "nom": maison,
        "score": 0,
        "a_marque": 0,
        "a_stoppe": 0,
        "attrape_vifdor": False,
        "joueurs": []
    }

    liste_originale = equipe_data["joueurs"]

    if est_joueur == True and joueur is not None:
        nom_joueur = "{} {} (Attrapeur)".format(joueur["Prenom"], joueur["Nom"])
        equipe["joueurs"].append(nom_joueur)

        for membre in liste_originale:
            if "Attrapeur" not in membre and "Attrapeuse" not in membre:
                equipe["joueurs"].append(membre)

    else:
        for membre in liste_originale:
            equipe["joueurs"].append(membre)

    return equipe


def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):

    proba_but = random.randint(1, 10)

    if proba_but >= 6:
        buteur = ""

        if joueur_est_joueur == True:
            buteur = equipe_attaque["joueurs"][0]
        else:
            buteur = random.choice(equipe_attaque["joueurs"])

        equipe_attaque["score"] = equipe_attaque["score"] + 10
        equipe_attaque["a_marque"] = equipe_attaque["a_marque"] + 1

        print("{} marque un but pour {} ! (+10 points)".format(buteur, equipe_attaque["nom"]))

    else:
        equipe_defense["a_stoppe"] = equipe_defense["a_stoppe"] + 1
        print("{} bloque l'attaque !".format(equipe_defense["nom"]))


def apparition_vifdor():

    chance = random.randint(1, 6)

    if chance == 6:
        return True
    else:
        return False


def attraper_vifdor(e1, e2):

    choix = random.randint(1, 2)
    equipe_victorieuse = {}

    if choix == 1:
        equipe_victorieuse = e1
    else:
        equipe_victorieuse = e2

    equipe_victorieuse["score"] = equipe_victorieuse["score"] + 150
    equipe_victorieuse["attrape_vifdor"] = True

    return equipe_victorieuse


def afficher_score(e1, e2):

    print("\nScore actuel :")
    print("→ {} : {} points".format(e1["nom"], e1["score"]))
    print("→ {} : {} points".format(e2["nom"], e2["score"]))


def afficher_equipe(maison, equipe):

    print("\nÉquipe de {} :".format(maison))

    for joueur in equipe["joueurs"]:
        print("- {}".format(joueur))


def match_quidditch(joueur, maisons):

    donnees_equipes = load_fichier("data/equipes_quidditch.json")

    maison_joueur = joueur["Maison"]
    liste_adversaires = []

    for nom_maison in donnees_equipes.keys():
        if nom_maison != maison_joueur:
            liste_adversaires.append(nom_maison)

    maison_adverse = random.choice(liste_adversaires)

    print("\nMatch de Quidditch : {} vs {} !".format(maison_joueur, maison_adverse))

    equipe_joueur = creer_equipe(maison_joueur, donnees_equipes[maison_joueur], est_joueur=True, joueur=joueur)
    equipe_adverse = creer_equipe(maison_adverse, donnees_equipes[maison_adverse], est_joueur=False)

    afficher_equipe(maison_joueur, equipe_joueur)
    afficher_equipe(maison_adverse, equipe_adverse)

    print("\nTu joues pour {} en tant qu'Attrapeur".format(maison_joueur))

    tour = 1
    match_termine = False

    while tour <= 20 and match_termine == False:
        print("\n━━━ Tour {} ━━━".format(tour))

        tentative_marque(equipe_joueur, equipe_adverse, joueur_est_joueur=True)
        tentative_marque(equipe_adverse, equipe_joueur, joueur_est_joueur=False)

        afficher_score(equipe_joueur, equipe_adverse)

        if apparition_vifdor() == True:
            equipe_qui_attrape = attraper_vifdor(equipe_joueur, equipe_adverse)
            print("\nLe Vif d'Or a été attrapé par {} ! (+150 points)".format(equipe_qui_attrape["nom"]))
            match_termine = True

        if match_termine == False:
            input("\nAppuyez sur Entrée pour continuer")
            tour = tour + 1

    print("\nFin du match !")
    afficher_score(equipe_joueur, equipe_adverse)

    print("\nRésultat final :")

    if equipe_joueur["attrape_vifdor"] == True:
        print("Le Vif d'Or a été attrapé par {} !".format(equipe_joueur["nom"]))
    elif equipe_adverse["attrape_vifdor"] == True:
        print("Le Vif d'Or a été attrapé par {} !".format(equipe_adverse["nom"]))

    nom_gagnant = ""

    if equipe_joueur["score"] > equipe_adverse["score"]:
        nom_gagnant = equipe_joueur["nom"]
        print("{} remporte le match...".format(nom_gagnant))

    elif equipe_adverse["score"] > equipe_joueur["score"]:
        nom_gagnant = equipe_adverse["nom"]
        print("{} remporte le match...".format(nom_gagnant))

    else:
        print("Match nul ! Incroyable !")

    if nom_gagnant != "":
        print("+500 points pour {} !".format(nom_gagnant))
        actualiser_points_maison(maisons, nom_gagnant, 500)


def lancer_chapitre4_quidditch(joueur, maisons):

    print("\n" + "=" * 50)
    print("⚡ CHAPITRE 4 : LA GRANDE FINALE DE QUIDDITCH ⚡")
    print("=" * 50)

    match_quidditch(joueur, maisons)

    print("\nFin du Chapitre 4 — Quelle performance incroyable sur le terrain !")

    print("\n--- RÉSULTAT DE LA COUPE DES QUATRE MAISONS ---")
    afficher_maison_gagnante(maisons)

    print("\n--- INFORMATIONS FINALES SUR VOTRE PERSONNAGE ---")
    afficher_personnage(joueur)