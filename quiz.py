kyssarit = {"kuinka monta päivää on viikossa? ": "7",
"tähän toinen kyssäri": "ja vastaus", 
"Kuinka paljon painaa kilo höyheniä? ":"1 kg"}
oikeat = 0
kaikki = 0
while True:
    vastaus = input(list(kyssarit.keys())[kaikki])
    if vastaus == "":
        break
    elif vastaus == kyssarit.get(vastaus):
        oikeat += 1
        kaikki += 1
    else:
        kaikki += 1

print(f"sinulla oli {oikeat}/{kaikki} oikeaa vastausta")
