<<<<<<< HEAD

def ohje():
    print("Ohjelmassa voit valita joko 0 tai 1, 0 lopettaa pelin ja 1 jatkaa peliä.")

def pelaa():
    pass
=======
#tulostaa ohjeet kysymyspelin pelaamiseen
def ohje():
    return print("Ohje tulee tähän")

#tulostaa kysymykset
#ja laskee oikeat vastaukset
#ja tulostaa pisteet
def pelaa():
    return print("Peli pyörii")
>>>>>>> origin/jaakko

#while-loop joka kutsuu kysymyksentulostusta, käsittelee pelaajan syötteen
#1 pelaa 0 lopeta
def suorita():
<<<<<<< HEAD
    pass

suorita()
=======
    print(ohje)
    kysymys = int(input("Oletko valmis pelaamaan? 1 = Pelaa, 0 = Lopeta "))
    if kysymys == 1:
        return pelaa()
    elif kysymys == 0:
        pass

suorita()

print("Kiitos pelaamisesta!")
>>>>>>> origin/jaakko
