def gemiddelde(list):
    i = 0
    sum = 0
    while i < len(list):
        sum += list[i]
        i += 1
    return round(sum / len(list), 1)
