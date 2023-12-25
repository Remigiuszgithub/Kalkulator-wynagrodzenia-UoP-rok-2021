print("Kalkulator wynagrodzeń 2021\nUmowa o pracę\nProgram oblicza składki oraz wynagrodzenie netto pracownika.")
brutto = float(input("Podaj kwotę wynagrodzenia brutto: "))
brutto = round(brutto, 2)
wiek = int(input("Podaj swój wiek: "))
ue = 0
uz = 0
uc = 0
ur = 0
us = 0
PIT = 0
if wiek < 26:
    ue = brutto * 0.0976
    uc = brutto * 0.0245
    ur = brutto * 0.015
    us = ue+uc+ur
    uz = (brutto-us)*0.09
else:
    ue = brutto * 0.0976
    uc = brutto * 0.0245
    ur = brutto * 0.015
    us = ue+uc+ur
    uz = (brutto-us)*0.09
    PIT = brutto * 0.0489
ue = round(ue, 2)
uc = round(uc, 2)
ur = round(ur, 2)
us = round(us, 2)
uz = round(uz, 2)
PIT = round(PIT, 0)
netto = round(brutto - (ue+uz+uc+ur+PIT), 2)
print("Wynagrodzenie brutto wynosi:", brutto, "zł","\nUbezpiecznie społeczne:", "\nUbezpieczenie emerytalne: ", ue,"zł","\nUbezpieczenie rentowe: ", ur,"zł", "\nUbezpieczenie chorobowe: ", uc, "zł", "\nUbezpieczenie społeczne razem: ", us, "zł", "\nUbezpieczenie zdrowotne: ", uz, "zł", "\nZaliczka na PIT (dotyczy tylko osób, które ukończyły 26 rok życia): ", PIT, "zł", "\nWynagrodzenie netto wynosi:", netto, "zł")
