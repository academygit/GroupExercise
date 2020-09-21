kyssarit = {"kuinka monta päivää on viikosta": "7",
"tähän toinen kyssäri": "ja vastaus"}

while True:
    oikeat = 0
    kaikki = 0
    vastaus = input("tähän joku kysymys")
    if vastaus == "":
        break
    elif vastaus == "tähän sitte oikea vastaus":
        oikeat += 1
        kaikki += 1
    else:
        kaikki += 1

print(f"sinulla oli {oikeat}/{kaikki} oikeaa vastausta")
