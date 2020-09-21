kyssarit = {"kuinka monta päivää on viikosta": "7",
"tähän toinen kyssäri": "ja vastaus"}

while True:
    oikeat = 0
    kaikki = 0
    keyt = kyssarit.keys()
    valuet = kyssarit.values()
    for key, value in keyt, valuet:
        vastaus = input(key)
        if vastaus == "":
            break
        elif vastaus == value:
            oikeat += 1
            kaikki += 1
        else:
            kaikki += 1


print(f"sinulla oli {oikeat}/{kaikki} oikeaa vastausta")