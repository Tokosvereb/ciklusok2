"""Kérj be egy számot a felhasználótól
Írj eljárást számok néven, melynek paramétere a felhasználó által megadott két szám
és
az eljárás kiírja a számokat ezen két paraméter között
"""
import eljarasok

szam1:int=int(input ("szam1:"))
szam2:int=int(input ("szam2:"))
"""A felhasználó csak olyan b-t tudjon megadni ami nagyobb mint az a"""
while (szam1 > szam2):
    print("a szam2-nek nagyobbnak kell lennie szam1-nel")
    b:int= int(input(f"Adj{szam1}-nál nagyobbat!"))
eljarasok.szamok(szam1,szam2)