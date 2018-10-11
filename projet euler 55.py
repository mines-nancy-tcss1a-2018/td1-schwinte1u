def transformation_nombre_en_liste(n):
    nombre=n
    liste_chiffres=[]
    while nombre>0:
        liste_chiffres.append(nombre%10)
        nombre=nombre//10
    #A ce stade la liste liste_chiffres contient la liste de chaque chiffre du nombre de départ n. En revanche, l'ordre est inversé. Ex, pour 123456, liste_chiffres=[6,5,4,3,2,1]
    return(liste_chiffres[::-1]) #l'instruction G[::-1] pour une liste G renvoie la liste miroir de G


def reverse(n):
    revers=0
    L=transformation_nombre_en_liste(n)
    for i in range(len(L)):
        revers += L[i]*(10**i)
    return(revers)
    
def test_palindrome(n):
    L=transformation_nombre_en_liste(n)
    return(L[::-1]==L)
    
def addition_avec_reverse(n):
    return(n+reverse(n))
    
def solve(n):
    nombre_non_lychrel=0
    for i in range(1,n+1):
        calcul=i
        for j in range(50):
            calcul=addition_avec_reverse(calcul)
            if test_palindrome(calcul):
                nombre_non_lychrel +=1
                break
    reponse=n-nombre_non_lychrel            
    return(reponse)

# Remarque: On vérifie facilement à la main que tout nombre en dessus de 49 ne peut être un nombre de lychrel. (Une itération d'addition avec son miroir suffit)

assert solve(49)==0

print(solve(10000))

            