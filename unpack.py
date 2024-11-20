def total(galleons, sickels, knuts):
    return(galleons * 17 + sickels) * 29 + knuts

coins = {"galleons": 100, "sickels": 50, "knuts": 25}

print(total(**coins), "Knuts")


def f(*args, **kwargs):
    print("Named:", kwargs)

f(galleons = 100, sickles = 50, knuts = 25)