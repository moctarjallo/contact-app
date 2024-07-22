def afficher_grille():
    n = 4
    ligne_horizontale = '+' + ('-' * 4 + ' +') * n
    
    ligne_verticale = '|' + ('' * 9 + '|') * n
    for i in range(n):
        print(ligne_horizontale) 
        for j in range(4):  
            print(ligne_verticale)
    print(ligne_horizontale)  

afficher_grille()
