def kysymys(numero):

    kysymykset = {"1" : {"Minkä värisenä Tšerenkovin säteily näkyy?" : ["A: Sinisenä", "B: Punaisena", "A"]},
                  "2" : {"Kuinka monen vuoden välein Mars on lähimpänä maata?" : ["A: 7 vuoden", "B: 15 vuoden", "B"]},
                  "3" : {"Uskotko voivasi voittaa?" : ["A: Kyllä", "B: Ei", "A"]}}
    kysymys = kysymykset.get(numero)
    vastaus = ""
    counter = 0
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

kysymys("2")