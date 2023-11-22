# trrzy rózne sposoby importu
import pakiet  # dostępne tylko metody z __init__.py w pakiecie
from pakiet import fun
import pakiet.fun as pk

fun.powitanie()
pk.powitanie()
pakiet.info()
# Dzień dobry
# Dzień dobry
# Jestem pakietem
