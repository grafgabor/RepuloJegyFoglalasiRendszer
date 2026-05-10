from datetime import date
from typing import List

from jegy_foglalas import JegyFoglalas
from legi_tarsasag import LegiTarsasag


class FoglalasiRendszer:
    """A jegyfoglalási műveleteket összefogó rendszer."""

    def __init__(self, legi_tarsasag: LegiTarsasag) -> None:
        self.legi_tarsasag = legi_tarsasag
        self.foglalasok: List[JegyFoglalas] = []

    def jegy_foglalasa(self, utas_nev: str, jaratszam: str, utazas_datuma: date) -> int:
        jarat = self.legi_tarsasag.jarat_keresese(jaratszam)
        if jarat is None:
            raise ValueError("Nincs ilyen járatszámú járat.")

        foglalas = JegyFoglalas(utas_nev, jarat, utazas_datuma)
        self.foglalasok.append(foglalas)
        return foglalas.ar

    def foglalas_lemondasa(self, foglalas_id: int) -> bool:
        for foglalas in self.foglalasok:
            if foglalas.foglalas_id == foglalas_id:
                self.foglalasok.remove(foglalas)
                return True
        return False

    def foglalasok_listazasa(self) -> None:
        print("\nAktuális foglalások:")
        print("-" * 100)
        if not self.foglalasok:
            print("Jelenleg nincs aktív foglalás.")
        else:
            for foglalas in self.foglalasok:
                print(foglalas)
        print("-" * 100)
