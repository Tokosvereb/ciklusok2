import math


def szamok(szam1=int, szam2=int):
    szam1:int= math.floor(szam1)
    while szam1 <= szam2:
        print(szam1 ,end=',')
        szam1+=1