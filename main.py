from kezdo_adatok import kezdo_adatok_betoltese
from seged_fuggvenyek import datum_bekerese, egesz_szam_bekerese


def menu_megjelenitese() -> None:
    print("\n===== Repülőjegy Foglalási Rendszer =====")
    print("1. Járatok listázása")
    print("2. Jegy foglalása")
    print("3. Foglalás lemondása")
    print("4. Foglalások listázása")
    print("0. Kilépés")


def main() -> None:
    rendszer = kezdo_adatok_betoltese()

    while True:
        menu_megjelenitese()
        valasztas = input("Választás: ").strip()

        if valasztas == "1":
            rendszer.legi_tarsasag.jaratok_listazasa()

        elif valasztas == "2":
            try:
                rendszer.legi_tarsasag.jaratok_listazasa()
                utas_nev = input("Utas neve: ").strip()
                jaratszam = input("Járatszám: ").strip()
                utazas_datuma = datum_bekerese()
                ar = rendszer.jegy_foglalasa(utas_nev, jaratszam, utazas_datuma)
                print(f"Sikeres foglalás! A jegy ára: {ar} Ft")
            except ValueError as hiba:
                print(f"Hiba: {hiba}")

        elif valasztas == "3":
            rendszer.foglalasok_listazasa()
            foglalas_id = egesz_szam_bekerese("Lemondandó foglalás ID-ja: ")
            if rendszer.foglalas_lemondasa(foglalas_id):
                print("A foglalás sikeresen lemondva.")
            else:
                print("Hiba: nincs ilyen azonosítójú foglalás.")

        elif valasztas == "4":
            rendszer.foglalasok_listazasa()

        elif valasztas == "0":
            print("Kilépés. Viszontlátásra!")
            break

        else:
            print("Hiba: érvénytelen menüpont.")


if __name__ == "__main__":
    main()
