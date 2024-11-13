def nog_te_zetten(stappen):
    nog_te_zetten = 10000 - stappen
    return nog_te_zetten

def stappenteller(stappen):
    steps_to_make = nog_te_zetten(stappen)
    if steps_to_make == 1:
        print('Je moet nog maar één stap zetten!')
    elif steps_to_make <= 0:
        print('Je hebt je stappendoel bereikt!')
    else:
        print('Je dient nog', steps_to_make, 'stappen te zetten.')