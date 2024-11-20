from PIL import Image
from PIL import ImageFilter

def main():
    with Image.open("Car.jpg") as img:
        img = img.rotate(190)
        img = img.filter(ImageFilter.BLUR)
        img = img.filter(ImageFilter.Find_Edges)
        img.save("Truck.jpg")
            print(img.size)
            print(img.format)


main()