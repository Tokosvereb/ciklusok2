import math


def szamok(szam1=float, szam2=float):
    if szam1 == szam2:
        print("a két szám megegyezik")
        return
    
    i:int= math.ceil(szam1)
    if szam1>szam2:
        csere:float = szam1
        szam1=szam2
        szam2=csere
    while i < szam2:
        if (i==szam2-1):
            print(i)
        else:    
            print(i,end=',')
        i+=1