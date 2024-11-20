distances = {
    "Voyager1": 163,
    "Voyager2": 136,
    "Pioneer10": 80,
    "New Horizons": 58,
    "Pioneer11": 44,
}

def main():
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")


def convert(au):
    return au * 1495978706

main()