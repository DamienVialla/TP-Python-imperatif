import csv

somme_age = 0
nb_val =0
nb_survivant_classe1 = 0
nb_tot_classe1 =0
nb_survivant_classe2 = 0
nb_tot_classe2 =0
nb_survivant_classe3 = 0
nb_tot_classe3 =0
liste_bateaux_valides = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","A","B","C","D"]
liste_sauvetage =[]
nb_non_traité = 0
nb_pers = 0
nb_pers_sans_age = 0
dictionnaire_sauvetage ={}

with open('titanic_survival.csv', "r", encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',',)
    #on saute la ligne entête
    next(reader)
    
    for row in reader:
        #calcul moyenne age
        if row[4] == "": 
            row[4]= 0 #pers avec age vide, on met 0. Le "continue" ne marche pas car impact le reste, pourquoi ?
            nb_pers_sans_age +=1 #on garde en variable le nombre de pers sans age pour les stats
        else :
            somme_age += float(row[4]) #on convertit en nombre, ici en float pour les nombres à virgule
            nb_val +=1 #besoin du nombre de pers avec un age rentré pour faire ensuite la moyenne
        
        #on comptabilise le nombre de personnes en classe 1/2/3 et nombre de personnes sauvées, à voir si on peut créer une fonction
        if row[0] == "1": #appartient classe 1 (colonne 0)
            nb_tot_classe1 += 1 #on compte
            if row[1] == "1": #si classe 1, on regarde si sauvé (colonne 1)
                nb_survivant_classe1 += 1 #on compte
        if row[0] == "2":
            nb_tot_classe2 += 1
            if row[1] == "1":
                nb_survivant_classe2 += 1
        if row[0] == "3":
            nb_tot_classe3 += 1
            if row[1] == "1":
                nb_survivant_classe3 += 1

        #on va chercher le nombre de fois où un bateau a sauvé une personne
        if row[11] in liste_bateaux_valides : #on regarde si la valeur dans le csv est une valeur abérante (si elle fait partie ou non de la liste des bateaux)
            for num_bateau in liste_bateaux_valides:
                if row[11] == num_bateau :
                    liste_sauvetage.append(num_bateau)
                    break
        else :
            nb_non_traité += 1 #pour stat       
            
        #création d'un dictonnaire avec le num bateau et le nombre de pers sauvées
        for bateau in liste_sauvetage:
            dictionnaire_sauvetage.update({bateau:liste_sauvetage.count(bateau)})

    #on trie le dictionnaire des bateaux sauveteurs
    dictionnaire_sauvetage_tri = sorted(dictionnaire_sauvetage.items(), key=lambda t: t[1],reverse=True)
    
    #impression des résultats    
    print(f"la moyenne d'âge des personnes était de {round(somme_age/nb_val,2)} ans ({nb_pers_sans_age-1} pers sans âge indiqué)")  
    print(f"le pourcentage de survie en 1e classe est de : {round(nb_survivant_classe1/nb_tot_classe1,3)*100} %")
    print(f"le pourcentage de survie en 2e classe est de : {round(nb_survivant_classe2/nb_tot_classe2,3)*100} %")
    print(f"le pourcentage de survie en 3e classe est de : {round(nb_survivant_classe3/nb_tot_classe3,3)*100} %")
    print(f"le bateau ayant sauvé le plus de personnes ({dictionnaire_sauvetage_tri[0][1]} pers) est le numéro {dictionnaire_sauvetage_tri[0][0]}. ATTENTION, il y a eu {nb_non_traité} valeurs abérrantes non prises en compte (num bateau non correct, deux bateaux déclarés, manque info, ...)")
    

def pourcentage_survie(classe):
        nb_tot = 0
        nb_survivant = 0
        if row[0] == str(classe):
            nb_tot += 1
            if row[1] == "1":
                nb_survivant += 1
        print(nb_tot)
        print(nb_survivant)
        print(f"le pourcentage de survie en 1e classe est de : {round(nb_survivant/nb_tot,3)*100} %")

