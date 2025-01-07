# splits input in lijst van strings, gescheiden door spaties
# "33 37 36 32" -> ["33", "37", "36", "32"]
lijst = input().split(" ")

def far_to_cel(f):
    return round((f - 32) * 5 / 9, 1)

oplossing = []
for element in lijst:
    cel = far_to_cel(int(element))
    oplossing.append(cel)

print(oplossing)

