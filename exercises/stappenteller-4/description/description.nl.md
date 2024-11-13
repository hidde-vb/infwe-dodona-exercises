## Gegeven

We gaan nog een stapje (snapje?) verder gaan, en onze logica verder onderverdelen. We starten met dezelfde functie uit `Stappenteller 3`. 

We zouden graag willen dat onze `stappenteller()` functie zelf geen berekeningen maakt. Dat wilt zeggen dat we de berekening van het aantal stappen eruit gaan halen.

Dit kunnen we doen door de eenvoudige berekening in een **andere functie** te plaatsen. We gaan deze de naam `nog_te_zetten()` geven. 

Deze zouden we kunnen gebruiken als volgt:

```python
stappen = int(input())

overige = nog_te_zetten(stappen)

print(overige) # 10000 - stappen
```

de functie hierboven zouden we ook direct kunnen aanroepen als volgt:
```console?lang=python&prompt=>>>
>>> nog_te_zetten(6000)
4000
```

## Gevraagd

Implementeer `nog_te_zetten()`, en pas de `stappenteller()` functie aan zodat hij ook gebruikt maakt van je nieuwe functie.