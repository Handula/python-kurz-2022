import json
with open("body.json", mode="r", encoding="utf-8") as soubor:
    body = json.load(soubor)
print(body)

for jmeno, pocet_bodu in body.items():
    if pocet_bodu >=60:
        body[jmeno]="pass"
    else:
        body[jmeno]="fail"
print(body)


  