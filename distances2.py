distances = {
    "Voyager1": "163",
    "Voyager2": "136",
    "Pioneer10": "80 AU",
    "New Horizons": "58",
    "Pioneer11": "44 AU",
}


def main():
    spacecraft = input("Enter a spacecraft: ")
    try:
        au = float(distances[spacecraft])
    except KeyError:
        print(f"{spacecraft} is not in dictionary")
        return
    except ValueError:
        print(f"Cant convert {distances[spacecraft]} to a float")
        return

    m = convert(au)
    print(f"{m} m away")

def convert(au):
    return au * 149597870691

main()