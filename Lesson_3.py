# json = java script object notation
# pisou se jenom ""; true/false
#mode => jestli do neho chceme zapisovat(w) nebo cist (r); defaultne se cte

import json
with open("pizza.json", mode="r", encoding="utf-8") as soubor:
    pizzy = json.load(soubor)
print(pizzy["ingredience"][-1]) 

data = {
    "1.misto": "Olga",
    "2.misto": "Zanet",
    "3.misto": "Andy"
}

#muzes pridat ensure_ascii=False, aby se nam ukazala diakritika
with open("vyherci.json", mode="w",encoding="utf-8") as soubor:
    json.dump(data, soubor)
