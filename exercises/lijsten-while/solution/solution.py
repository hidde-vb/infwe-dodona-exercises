# Deze lijn code splitst deinput in lijst van strings, gescheiden door spaties
# "hallo wereld" -> ["hallo", "wereld"]
lijst = input().split(" ")

i = 0
while i < len(lijst):
  print(str(i) + ": " + lijst[i])
  i += 1