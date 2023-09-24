from vectors import Vec3

WIDTH = 160
HEIGHT = 40
ASPECT_RATIO = WIDTH / HEIGHT
PIXEL_ASPECT = 11 / 24
GRADIENT = " .:|/(@"

# FOV = 60 deg.
DIST_TO_SCREEN = ASPECT_RATIO * PIXEL_ASPECT * (3**0.5)

CAMERA_POS = Vec3(0, 0, -4)

VIEW_MIN = 0.0001
VIEW_MAX = 10000

LIGHT_DIR = Vec3(-0.5, 0.5, -0.5).norm()

SPHERES = [
    {
        "pos": Vec3(0),
        "radius": 0.5,
    },

    {
        "pos": Vec3(-1.5, -0.7, 1),
        "radius": 0.3,
    },

    {
        "pos": Vec3(1.6, 0.4, 0.6),
        "radius": 0.37,
    },
]


def sphere_intersection(ro, rd, pos, radius):
    o = ro - pos

    a = rd.dot(rd)
    b = o.dot(rd)
    c = o.dot(o) - radius;

    D = b**2 - a * c
    if D < 0:
        return [-1, -1]

    sqrt_D = D**0.5
    return (-b + sqrt_D) / a, (-b - sqrt_D) / a


def calc_normal(pos, dot):
    return (dot - pos).norm()


def get_closest_collide(ro, rd):
    closest_object = None
    closest = float("inf")

    for i in SPHERES:
        t1, t2 = sphere_intersection(ro, rd, i["pos"], i["radius"])
        
        if VIEW_MIN < t1 < VIEW_MAX and t1 < closest:
            closest = t1
            closest_object = i

        if VIEW_MIN < t2 < VIEW_MAX and t2 < closest:
            closest = t2
            closest_object = i
        
    return closest_object, closest


def cast_ray(ro, rd):
    closest_object, closest = get_closest_collide(ro, rd)

    if closest_object == None:
        return 0

    collide_dot = ro + rd * closest
    normal = calc_normal(closest_object["pos"], collide_dot)
    
    diffuse = max(0, normal.dot(LIGHT_DIR)) * 0.8 + 0.2

    return diffuse

def get_pixel_color(pixel_x, pixel_y):
    x = (pixel_x / WIDTH * 2 - 1) * ASPECT_RATIO * PIXEL_ASPECT
    y = (1 - pixel_y / HEIGHT) * 2 - 1

    ro = CAMERA_POS.copy()
    rd = Vec3(x, y, DIST_TO_SCREEN)

    color = cast_ray(ro, rd)
    
    return color


def calc_image():
    res = []
    COLORS_COUNT = len(GRADIENT)

    for y in range(HEIGHT):
        row = ""

        for x in range(WIDTH):
            brightness = get_pixel_color(x, y)
            color = GRADIENT[min(COLORS_COUNT - 1, int(brightness * COLORS_COUNT))]
            row += color

        res.append(row)

    return "\n".join(res)

    
def main():
    image = calc_image()
    print(image)    


if __name__ == "__main__":
    main()