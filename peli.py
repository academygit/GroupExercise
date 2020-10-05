correct_answers = 0
jatkuuko = True
print("Tervetuluo pellaamaan kysymyspeliä!")

while jatkuuko==True:
    print("Halluukkonä jatkaa ite pelliin? (K/E)")
    counter = 0
    userinput = input()
    if userinput == "K" or userinput == "k" :
        #ARIN-Koodi tähän!!!
        if correct_answers = 3:
            print("Onneksi olkoon! Olet legenda.")
        if correct_answers = 2:
            print("Sait kaksi oikeaa vastausta. Se on ihan hyvin.")
        if correct_answers = 1:
            print("Sait vain yhden vastauksen oikein. Aika noloa.")
        if correct_answers = 0:
            print("Kaikki meni väärin. Surullista.")
        jatkuuko=False
    elif userinput == "E" or userinput == "e" :
        jatkuuko=False
