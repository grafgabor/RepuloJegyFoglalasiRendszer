from typing import List, Optional

from jarat import Jarat


class LegiTarsasag:
    """Egy légitársaság, amely több járatot kezel."""

    def __init__(self, nev: str) -> None:
        if not nev.strip():
            raise ValueError("A légitársaság neve nem lehet üres.")
        self.nev = nev
        self.jaratok: List[Jarat] = []

    def jarat_hozzaadasa(self, jarat: Jarat) -> None:
        if self.jarat_keresese(jarat.jaratszam) is not None:
            raise ValueError("Ilyen járatszám már létezik.")
        self.jaratok.append(jarat)

    def jarat_keresese(self, jaratszam: str) -> Optional[Jarat]:
        for jarat in self.jaratok:
            if jarat.jaratszam.lower() == jaratszam.lower():
                return jarat
        return None

    def jaratok_listazasa(self) -> None:
        print(f"\n{self.nev} elérhető járatai:")
        print("-" * 60)
        for jarat in self.jaratok:
            print(jarat)
        print("-" * 60)
