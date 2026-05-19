

import random
from unidecode import unidecode

#Définir le chemin du fichier contenant la liste de mots
chemin_du_fichier = "mots_pendu.txt"

#Défini le nombre maximal de tentatives permises
nombre_maximum_de_tentatives = 6


#Fonction qui lit le fichier de mots et les stockent dans une liste
def lire_fichier_mots (a):
    #Ouvrir le fichier
    contenu_fichier=open(a,"r",encoding="utf-8")

    #Lire, séparer et remplacer les caractères spéciaux du fichier et retourner la liste
    return unidecode(contenu_fichier.read()).split()

#Fonction pour choisir un mot au hasard
def choisir_mot_hasard (b):
    return random.choice(b)

#Fonction pour demander une lettre à l'utilisateur et valider que l'entrée est acceptable
def demander_une_lettre (liste_demande):
    #Demander la lettre à l'utilisateur
    lettre = input("Choisir la lettre que vous souhaiter valider : ")


    #Valider que l'entrée est valide
    #Valider si la lettre a déjà été saisie
    if len(lettre) == 1 and lettre.isalpha() == True and lettre.lower() in liste_demande:
        print("Vous avez déjà valider cette lettre, vous pouvez en prendre une différente")
        demander_une_lettre(liste_demande)

    #Valider que l'entrée est valide et la convertir en minuscule
    elif len(lettre) == 1 and lettre.isalpha() == True:
        return lettre.lower()

    #Soulever une erreur si l'entrée n'est pas valide
    else:
        print("Veuillez vous assurez d'entrer seulement une lettre")
        demander_une_lettre()

#Fonction pour vérifier si une lettre est dans le mot à deviner
def valider_la_presence_de_la_lettre_dans_le_mot (lettre, mot,progression,tentative):
    presence_lettre=False

    #Boucler dans le mot pour trouver la position de la lettre si elle est présente
    for i in range(len(mot)):

        #Mettre à jout la progression avec l'emplacement de la lettre
        if mot[i]==lettre:
            progression[i]=lettre
            presence_lettre=True

    #Incrément du compteur de tentavives car la lettre n'est pas dans le mot
    if presence_lettre==False:
        tentative +=1
    return progression,tentative

#Fonction qui permet de donner un indice à l'utilisateur
def donner_un_indice(liste_deja_demandee, mot):

    #Boucle infinie pour valider que l'indice n'est pas dans le mot et n'a pas déjà été demandé
    while True:
        indice=random.choice("abcdefghijklmnopqrstuvwxyz")
        if indice not in liste_deja_demandee and indice not in mot:
            break
    print(f"Voici un indice : Le mot à deviner ne contient pas la lettre {indice}")


#Fonction principale du jeu, elle permet de jouer au pendu
def jouer_au_pendu():
    #Importer la liste de mots à partir du fichier
    mots = lire_fichier_mots(chemin_du_fichier)
    #print(f"Voici la liste {mots}")

    #Choisir au hasard le mot à deviner
    mot_a_deviner = choisir_mot_hasard(mots)

    #print(f"Voici le mot à deviner {mot_a_deviner}")

    #Initialiser la list de suivi de la progression et le décompte tentatives écoulées
    progression_pendu = ["_"]*len(mot_a_deviner)
    tentatives_ecoulees = 0
    liste_demande = []

    #Boucle pour procéder aux tentatives
    while tentatives_ecoulees < nombre_maximum_de_tentatives :

        print(f"Voici le statut du mot à deviner : {" ".join(progression_pendu)}")

        #Demander la lettre à l'utilisateur
        lettre_demande=demander_une_lettre(liste_demande)

        #Ajouter la lettre demandée dans la liste des lettres demandées
        liste_demande.append(lettre_demande)

        #Valider si la lettre est dans le mot ou pas
        progression_pendu,tentatives_ecoulees=valider_la_presence_de_la_lettre_dans_le_mot(lettre_demande,mot_a_deviner,progression_pendu,tentatives_ecoulees)
        print(f"Il vous reste {nombre_maximum_de_tentatives-tentatives_ecoulees} tentatives pour deviner le mot")

        #Déterminer si l'utilisateur à gagné
        if "_" not in progression_pendu:
            print(f"Félicitations, vous avez bien deviné tout le mot : {mot_a_deviner}")
            break

        #Déterminer si on est rendu à la dernière tentative pour donner un indice
        if nombre_maximum_de_tentatives - tentatives_ecoulees == 1:
            donner_un_indice(liste_demande,mot_a_deviner)

    #Message pour dire que l'utilisateur n'a pas réussi
    if tentatives_ecoulees == nombre_maximum_de_tentatives:
        print(f"Vous n'avez pas réussi à deviner le mot en moins de {nombre_maximum_de_tentatives} tentatives")

    #Demander au joueur s'il veut rejouer ou non
    choix = input("Entrez 1 pour rejouer ou 2 pour quitter")
    if choix == "1":
        jouer_au_pendu()

#Mot de bienvenue
print (f"Bienvenue dans ce jeu du pendu. Les consignes sont très simples. Vous disposez de {nombre_maximum_de_tentatives} tentatives pour deviner le mot. \nBonne chance!")

#Fonction principale
jouer_au_pendu()