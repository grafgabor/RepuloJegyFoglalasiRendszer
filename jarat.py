from abc import ABC, abstractmethod


class Jarat(ABC):
    """Absztrakt alaposztály a járatok közös adataihoz."""

    def __init__(self, jaratszam: str, celallomas: str, jegyar: int) -> None:
        if not jaratszam.strip():
            raise ValueError("A járatszám nem lehet üres.")
        if not celallomas.strip():
            raise ValueError("A célállomás nem lehet üres.")
        if jegyar <= 0:
            raise ValueError("A jegyárnak pozitív számnak kell lennie.")

        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def jarat_tipus(self) -> str:
        pass

    def __str__(self) -> str:
        return f"{self.jaratszam} | {self.jarat_tipus()} | {self.celallomas} | {self.jegyar} Ft"
