def transformation_nombre_en_liste(n):
    nombre=m
    list_chiffres=[]
    while nombre>0:
        list_chiffres.append(nombre%10)
        nombre=nombre//10
    return(list_chiffres[::-1])#L'instruction L[::-1] pour une liste L renvoie la liste miroir de L

def test_palindromes(L):
    L=transformation_nombre_en_liste(n)
    return(L[::-1]==L)

def addition_avec_reverse(k):
    

def solve(n):
    nombre_Lychrel=0
    for i in range(1,10000):
        