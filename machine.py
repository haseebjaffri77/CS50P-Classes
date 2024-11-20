emoticon = "v.v"

def main():
    global emoticon
    say("Is anyone there? ")
    emoticon = ":D"
    say("Oh, Hi there! ")

def say(phrase):
    print(phrase + " " + emoticon)

main()