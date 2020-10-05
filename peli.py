print("Tervetuluo pellaamaan kysymyspeliä!")
jatkuuko = True
while jatkuuko==True:
    print("Halluukkonä jatkaa ite pelliin? (K/E)")
    counter = 0
    userinput = input()
    if userinput == "K" or userinput == "k" :
        #ARIN-Koodi tähän!!!
        jatkuuko=False
    elif userinput == "E" or userinput == "e" :
        jatkuuko=False
