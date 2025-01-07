def mediaan(lijst):
    lengte = len(lijst)
    if lengte % 2 == 0:
        eerste = lijst[lengte // 2 - 1]
        tweede = lijst[lengte // 2]
        return (eerste + tweede) / 2
    else:
        return lijst[lengte // 2]
