from matplotlib import image, pyplot
from requests import get
from os import remove
from time import sleep

def downloadImg(URL="https://picsum.photos/200", filename="image.jpg"):
    print("Downloading image from " + URL)
    data = get(URL).content
    print("Downloading complete, now writing file to disk at " + filename)
    with open(filename, "wb") as file:
        file.write(data)
    print("Write complete")
    return filename

def displayImg(filename):
    img = image.imread(filename)
    imgplot = pyplot.imshow(img)
    print("Now displaying image plot")
    pyplot.show()

def displayRandomImg():
    filename = downloadImg()
    displayImg(filename)
    remove(filename)
    
try:
    print("Press ctrl+c in the terminal any time to stop spawning new image plots.")
    while(True):
        displayRandomImg()
finally:
    remove(filename)
    exit()
