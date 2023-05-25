from kiir import Kiir


nev=input("Add meg a neved kérlek.")
a=input("Az a oldalt kérem.")
b=input("Az b oldalt kérem.")

if a.isnumeric()==True and b.isnumeric()==True:
    aold=int(a)
    bold=int(b)
    fajlbair=Kiir(nev,aold,bold)
    fajlbair.nyomtatos_funkcio()
else:
    print("Számban add meg kérlek.")