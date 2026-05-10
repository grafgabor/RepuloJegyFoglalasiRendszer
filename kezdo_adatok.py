from datetime import date, timedelta

from belfoldi_jarat import BelfoldiJarat
from foglalasi_rendszer import FoglalasiRendszer
from legi_tarsasag import LegiTarsasag
from nemzetkozi_jarat import NemzetkoziJarat


def kezdo_adatok_betoltese() -> FoglalasiRendszer:
    legi_tarsasag = LegiTarsasag("Python Airlines")

    legi_tarsasag.jarat_hozzaadasa(BelfoldiJarat("PA101", "Budapest", 18000))
    legi_tarsasag.jarat_hozzaadasa(BelfoldiJarat("PA102", "Debrecen", 15000))
    legi_tarsasag.jarat_hozzaadasa(NemzetkoziJarat("PA201", "London", 65000))

    rendszer = FoglalasiRendszer(legi_tarsasag)

    # 6 előre betöltött foglalás, mindig mai vagy jövőbeli dátummal.
    mai_nap = date.today()
    rendszer.jegy_foglalasa("Kiss Anna", "PA101", mai_nap + timedelta(days=5))
    rendszer.jegy_foglalasa("Nagy Péter", "PA102", mai_nap + timedelta(days=7))
    rendszer.jegy_foglalasa("Szabó Réka", "PA201", mai_nap + timedelta(days=10))
    rendszer.jegy_foglalasa("Tóth Gábor", "PA101", mai_nap + timedelta(days=14))
    rendszer.jegy_foglalasa("Varga Lilla", "PA102", mai_nap + timedelta(days=20))
    rendszer.jegy_foglalasa("Balogh Máté", "PA201", mai_nap + timedelta(days=30))

    return rendszer
