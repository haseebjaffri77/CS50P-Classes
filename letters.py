def main():
    names = ["Mario","Luigi","Daisy","Yoshi","Bowser"]
    for name in names:
                   print(write_letter(name , "Princess Peach"))

def write_letter(reciever , sender):
    return f"""

    Dear {reciever},
    You are cordially invited at a ball
    at Peach's castle this evening at 07:00PM.

    Sincerly,
    {sender}
    """

main()