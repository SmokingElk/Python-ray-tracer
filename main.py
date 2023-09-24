from vectors import Vec3

WIDTH = 120
HEIGHT = 30
ASPECT_RATIO = WIDTH / HEIGHT
PIXEL_ASPECT = 11 / 24
GRADIENT = " .:a|/(@"


def getPixelColor(pixelX, pixelY):
    x = (pixelX / WIDTH * 2 - 1) * ASPECT_RATIO * PIXEL_ASPECT
    y = pixelY / HEIGHT * 2 - 1

    if x**2 + y**2 < 0.5:
        return 1
    
    return 0


def calcImage():
    res = []
    COLORS_COUNT = len(GRADIENT)

    for y in range(HEIGHT):
        row = ""

        for x in range(WIDTH):
            brightness = getPixelColor(x, y)
            color = GRADIENT[min(COLORS_COUNT - 1, int(brightness * COLORS_COUNT))]
            row += color

        res.append(row)

    return "\n".join(res)

    
def main():
    image = calcImage()
    print(image)    


if __name__ == "__main__":
    main()