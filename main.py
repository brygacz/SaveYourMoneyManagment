oszczednosci = []

while True:
    oszczednosc = input("Podaj swoje oszczędności: ")
    try:
        oszczednosc = float(oszczednosc)
        if oszczednosc < 0:
            print("Błąd: podana wartość musi być nieujemna.")
        else:
            oszczednosci.append(oszczednosc)
            break
    except ValueError:
        print("Błąd: podana wartość musi być liczbą.")

suma_oszczednosci = sum(oszczednosci)
print(f"Masz na koncie {suma_oszczednosci} zł.")

while True:
    wplata_netto = input("Podaj swoją wypłatę netto w tym miesiącu: ")
    try:
        wplata_netto = float(wplata_netto)
        if wplata_netto < 0:
            print("Błąd: podana wartość musi być nieujemna.")
        else:
            break
    except ValueError:
        print("Błąd: podana wartość musi być liczbą.")

while True:
    rachunki = input("Podaj sumę swoich rachunków w tym miesiącu: ")
    try:
        rachunki = float(rachunki)
        if rachunki < 0:
            print("Błąd: podana wartość musi być nieujemna.")
        else:
            break
    except ValueError:
        print("Błąd: podana wartość musi być liczbą.")

po_odjeciu = wplata_netto - rachunki
print(f"Po odjęciu rachunków pozostanie ci {po_odjeciu} zł.")

while True:
    wplata_oszczednosci = input("Ile zł chcesz wpłacić na konto oszczędnościowe?: ")
    try:
        wplata_oszczednosci = float(wplata_oszczednosci)
        if wplata_oszczednosci < 0:
            print("Błąd: podana wartość musi być nieujemna.")
        else:
            break
    except ValueError:
        print("Błąd: podana wartość musi być liczbą.")

suma_oszczednosci += wplata_oszczednosci
pozostale_oszczednosci = po_odjeciu - wplata_oszczednosci
print(f"Stan Twojego konta oszczędnościowego to {suma_oszczednosci} zł.")
print(f"Na życie w tym miesiącu zostanie ci {pozostale_oszczednosci} zł.")
