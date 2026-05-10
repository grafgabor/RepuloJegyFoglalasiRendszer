from datetime import date, datetime


def datum_bekerese() -> date:
    while True:
        datum_szoveg = input("Utazás dátuma (ÉÉÉÉ-HH-NN): ").strip()
        try:
            utazas_datuma = datetime.strptime(datum_szoveg, "%Y-%m-%d").date()
            if utazas_datuma < date.today():
                print("Hiba: múltbeli dátumra nem lehet foglalni.")
                continue
            return utazas_datuma
        except ValueError:
            print("Hiba: a dátum formátuma legyen például 2026-06-15.")


def egesz_szam_bekerese(uzenet: str) -> int:
    while True:
        ertek = input(uzenet).strip()
        try:
            return int(ertek)
        except ValueError:
            print("Hiba: egész számot adj meg.")
