from quote import quote
from pprint import pprint


result = quote("Simone De Beauvoir", limit=30)
list_book = []
list_book_unique = []
dictionnaire_titre = {}
list_quote = []
list_words = []
list_words_unique = []
dictionnaire_words = {}
mots = []


def impression_citation():
    index_quote = 1
    #Permet d'obtenir 30 citation (limite=30 et on va chercher la clé quote dans result)
    for results in result:
        print(f"citation n° {index_quote} - {results['quote']}")
        index_quote +=1

def titre_livre():
    index_titre =1 
    #Permet d'obtenir 30 titres (limite=30 et on va chercher la clé book dans result)
    for results in result:
        list_book.append(results["book"])

    #création d'une liste de titre de livre unitaire
    list_book_unique = list(list_book)
    for book in list_book_unique :
        while(list_book_unique.count(book) > 1) :
            list_book_unique.remove(book)

    #création d'un dicitonnaire avec les titres de livre et leur nombre
    for book in list_book_unique:
        if book == "":
            continue
        else :
            dictionnaire_titre.update({book:list_book.count(book)}) 

    dictionnaire_titre_tri = sorted(dictionnaire_titre.items(), key=lambda t: t[1],reverse=True)
    
    print(f"-"*60)
    print("Classement des titres de livres par occurance")
    print(f"-"*60)
    for k,val in dictionnaire_titre_tri:
        print(f"{index_titre} - {val} fois : {k}")
        index_titre +=1
    
    print(f"-"*60)
    print(f"Attention dans la liste {list_book.count('')} livres n'avaient pas de titres")
    print(f"-"*60)

def mot_citation():
    index_mot = 1
    flat_list_words = []
    #Permet d'obtenir 30 citations (limite=30 et on va chercher la clé quote dans result)
    for results in result:
        list_quote.append(results["quote"])

    #création d'une liste de mots
    for i in range (0,len(list_quote)):
        list_words.append(list_quote[i].split())

    #écrase la list_words
    for item in list_words :
        flat_list_words += item

    #création d'une liste de mots apparraissant moins de 5 fois
    flat_list_words_unique = list(flat_list_words)
    for items in flat_list_words :
        if flat_list_words_unique.count(items) < 5 :
            flat_list_words_unique.remove(items)

    #création d'un dicitonnaire avec les mots et leur occurance
    for words in flat_list_words_unique:
            dictionnaire_words.update({words:flat_list_words_unique.count(words)})

    dictionnaire_words_tri = sorted(dictionnaire_words.items(), key=lambda t: t[1],reverse=True)

    print(f"-"*60)
    print("Classement des mots par occurance dans les citations")
    print(f"-"*60)

    for k,val in dictionnaire_words_tri:
        print(f"{index_mot} - {val} fois : {k}")
        index_mot +=1
    
    print(f"-"*70)
    print(f"{len(flat_list_words)-len(flat_list_words_unique)} mots n'ont pas été comptabilisés car inférieurs à 5 caractères")
    print(f"-"*70)

impression_citation()
titre_livre()
mot_citation()