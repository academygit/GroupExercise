
def kysymys():

    kysymykset = {"1" : {"Minkä värisenä Tšerenkovin säteily näkyy?" : ["A: Sinisenä", "B: Punaisena", "A"]},
                  "2" : {"Kuinka monen vuoden välein Mars on lähimpänä maata?" : ["A: 7 vuoden", "B: 15 vuoden", "B"]},
                  "3" : {"Uskotko voivasi voittaa?" : ["A: Kyllä", "B: Ei", "A"]}}
    counter = 0
    for numero in range (1,4):
        kysymys = kysymykset.get(numero)
        vastaus = ""
        
        for key in kysymys:
            print(key)
            print(kysymys.get(key)[0])
            print(kysymys.get(key)[1])
            vastaus = (kysymys.get(key)[2])
    
        vastattu = input("Anna vastauksesi: ")
        if vastattu == vastaus:
            print("Oikein")
            counter += 1
        else:
            print("Väärin")



print("Tervetuluo pellaamaan kysymyspeliä!")
jatkuuko = True
while jatkuuko==True:
    print("Halluukkonä jatkaa ite pelliin? (K/E)")
    counter = 0
    userinput = input()
    if userinput == "K" or userinput == "k" :
        kysymys()
        jatkuuko=False
    elif userinput == "E" or userinput == "e" :
        jatkuuko=False

