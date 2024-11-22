## Gegeven

We willen de pH-waarde of zuurtegraad berekenen van een oplossing. Dit doen we volgens de gekende formule:

$$
pH = − log{_10}{H^+}
$$

Hierin is `H+` de concentratie aan waterstof-ionen. Om het logaritme te berekenen, hebben we de logaritmische functie nodig, die gedefinieerd is in de module math.

```python
import math

waarde = 0.01

log_tien = math.log(waarde, 10)
```

## Gevraagd

Maak een functie `ph_waarde(concentratie)`, waarbij:
 - `concentratie` een parameter is die de concentratie waterstof-ionen voorstelt
 - de ph waarde teruggegeven wordt
 - **afgerond** op 2 getallen na de komma met `round()`

Voorbeeld waarbij de functie wordt gebruikt:

```python
concentratie_cola = 0.00155

print(ph_waarde(concentratie_cola))
# 2.81
```