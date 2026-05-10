from datetime import date

from jarat import Jarat


class JegyFoglalas:
    """Egy konkrét járatra és dátumra szóló foglalás."""

    kovetkezo_azonosito = 1

    def __init__(self, utas_nev: str, jarat: Jarat, utazas_datuma: date) -> None:
        if not utas_nev.strip():
            raise ValueError("Az utas neve nem lehet üres.")
        if utazas_datuma < date.today():
            raise ValueError("Múltbeli dátumra nem lehet jegyet foglalni.")

        self.foglalas_id = JegyFoglalas.kovetkezo_azonosito
        JegyFoglalas.kovetkezo_azonosito += 1
        self.utas_nev = utas_nev
        self.jarat = jarat
        self.utazas_datuma = utazas_datuma

    @property
    def ar(self) -> int:
        return self.jarat.jegyar

    def __str__(self) -> str:
        return (
            f"Foglalás ID: {self.foglalas_id} | "
            f"Utas: {self.utas_nev} | "
            f"Járat: {self.jarat.jaratszam} ({self.jarat.celallomas}) | "
            f"Dátum: {self.utazas_datuma} | "
            f"Ár: {self.ar} Ft"
        )
