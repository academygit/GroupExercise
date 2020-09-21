kyssarit = {"kuinka monta päivää on viikosta": "7",
"tähän toinen kyssäri": "ja vastaus"}

while True:
    oikeat = 0
    kaikki = 0
    for kyssari, oikea in kyssarit:
        vastaus = input(kyssari)
        if vastaus == "":
            break
        elif vastaus == oikea:
            oikeat += 1
            kaikki += 1
        else:
            kaikki += 1


print(f"sinulla oli {oikeat}/{kaikki} oikeaa vastausta")