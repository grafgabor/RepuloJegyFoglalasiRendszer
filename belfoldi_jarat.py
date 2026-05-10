from jarat import Jarat


class BelfoldiJarat(Jarat):
    """Belföldi, általában rövidebb és olcsóbb járat."""

    def jarat_tipus(self) -> str:
        return "Belföldi járat"
