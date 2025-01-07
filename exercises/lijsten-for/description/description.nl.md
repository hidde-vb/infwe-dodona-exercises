## Gegeven

Omdat de `while` lus redelijk omslachtig is, is er een eenvoudigere manier om dit te schrijven: de `for` lus.

```python
lijst = [1, 2, 3]
for element in lijst:
    print(element)
```

Dit leest een heel stuk vlotter, en we hoeven zelf geen telvariabele bij te houden. De for lus garandeert dat er over elk element in een lijst geïtereerd wordt.

Enkele nieuwe zaken die je in deze oefening nodig gaat hebben:

- je kan een lege lijst aanmaken met `lege_lijst = []`
- je kan aan een lijst elementen toevoegen met `lijst.append(1)`

## Gevraagd

![Temperaturen](image.png){:width="50%"}

De temperaturen staan in **fahrenheit**! Dit willen we graag omvormen naar een lijst in celcius.

- De input wordt opgesplits in een lijst van strings. Dit is al voor je geschreven.
- Vorm alle elementen om naar celcius, en rond af op **1 getal na de komma**.
- De formule om dit om te vormen kan je op het internet vinden.
- Maak gebruik van een `for` lus.
- Vergeet niet de input om te vormen naar getallen! Doe dit in de lus zelf.
- Print de omgevormde lijst. Dit kan je eenvoudig doen met `print(lijst)`.

 ## Voorbeeld

Stel we geven als input 3 voorspellingen door: `33 34 33`. Dan krijgen we als resultaat:
```python
[0.6, 1.1, 0.6]
```