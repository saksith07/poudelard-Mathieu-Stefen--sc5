from utils import demander_choix


def actualiser_points_maison(maisons, nom_maison, points):
    if nom_maison in maisons:
        maisons[nom_maison] = maisons[nom_maison] + points
        print("{} gagne {} points. Total : {} points.".format(nom_maison, points, maisons[nom_maison]))
    else:
        print("Maison introuvable.")


def afficher_maison_gagnante(maisons):
    score_max = -1000

    for points in maisons.values():
        if points > score_max:
            score_max = points


    gagnantes = []
    for nom, points in maisons.items():
        if points == score_max:
            gagnantes.append(nom)

    if len(gagnantes) == 1:
        print("La maison gagnantes est {} avec {} points.".format(gagnantes[0], score_max))

    else:
        print("Maisons à égalité :")
        for nom in gagnantes:
            print("- {} ( {} points )".format(nom, score_max))


# ================================
# Répartition d'un joueur dans les maisons quiz
# ================================




def repartition_maison(joueur, questions):
    scores = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }


    attributs = joueur["Attributs"]
    scores["Gryffondor"] += attributs["courage"] * 2
    scores["Serpentard"] += attributs["ambition"] * 2
    scores["Poufsouffle"] += attributs["loyauté"] * 2
    scores["Serdaigle"] += attributs["intelligence"] * 2


    for question_texte, liste_choix, liste_maisons in questions:


        reponse_choisie = demander_choix(question_texte, liste_choix)


        index_trouve = 0


        for i in range(len(liste_choix)):
            if liste_choix[i] == reponse_choisie:
                index_trouve = i



        maison_concernee = liste_maisons[index_trouve]
        scores[maison_concernee] += 3


    print("Résumé des scores :")
    maison_gagnante = ""

    score_max = -1


    for maison, points in scores.items():
        print("{} : {} points".format(maison, points))


        if points > score_max:
            score_max = points
            maison_gagnante = maison

    return maison_gagnante