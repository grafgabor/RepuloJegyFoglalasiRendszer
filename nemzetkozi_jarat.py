from jarat import Jarat


class NemzetkoziJarat(Jarat):
    """Nemzetközi, általában hosszabb és drágább járat."""

    def jarat_tipus(self) -> str:
        return "Nemzetközi járat"
