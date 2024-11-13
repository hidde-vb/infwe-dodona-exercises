TOTAL_STEPS = 10000

def stappenteller(steps):
    steps_to_make = TOTAL_STEPS - steps
    if steps_to_make == 1:
        print('Je moet nog maar één stap zetten!')
    elif steps_to_make <= 0:
        print('Je hebt je stappendoel bereikt!')
    else:
        print('Je dient nog', steps_to_make, 'stappen te zetten.')