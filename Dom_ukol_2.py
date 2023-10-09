""" Vyvíjíš software pro obchod s elektronickými součástkami. Firma eviduje informace o počtu součástek na skladě ve slovníku. Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě. """

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

""" Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník chce koupit. """

""" Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.
Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů. Následně součástku odeber ze slovníku, protože je vyprodaná.
Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, a sniž počet součástek na skladě o množství požadované zákazníkem. """

kod_soucastky = str(input("Zadej kod soucastky:"))

if kod_soucastky in sklad:
    pozadovane_mnozstvi = int(input('Zadej pozadovane mnozstvi: '))
    mnozstvi_na_sklade = sklad[kod_soucastky]
    if mnozstvi_na_sklade < pozadovane_mnozstvi:
        print("Lze prodat pouze omezeny pocet kusu")
        del sklad[kod_soucastky]
    if mnozstvi_na_sklade > pozadovane_mnozstvi:
        print("Poptavku lze uspokojit v plne vysi")
        sklad[kod_soucastky] = (mnozstvi_na_sklade)-(pozadovane_mnozstvi)
else:
    print("Poptavku bohuzel nelze uspokojit")

print(sklad)
