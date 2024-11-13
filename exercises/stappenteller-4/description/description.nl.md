## Gegeven

We gaan nog een stapje (snapje?) verder gaan, en onze logica verder onderverdelen

## Gevraagd

We beginnen met dezelfde functie uit `Stappenteller 3`. We zouden graag willen dat onze `stappenteller()` functie geen berekeningen maakt. 

Dit kunnen we doen door de eenvoudige berekening in een **ander functie** `nog_te_zetten()` te plaatsen. Deze zouden we kunnen gebruiken als volgt:

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

Implementeer `nog_te_zetten()`, en pas de `stappenteller()` functie aan zodat hij ook gebruikt maakt van je nieuwe functie.