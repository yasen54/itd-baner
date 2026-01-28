import random


def style_pixel(img, offset_x, offset_y, step, size):
    h, w = img.shape[:2]
    pixels = []

    for y in range(0, h, step):
        for x in range(0, w, step):
            b, g, r = img[y, x]
            color = f"rgb({int(r)},{int(g)},{int(b)})"
            pixels.append((x + offset_x, y + offset_y, size, size, color))

    return pixels


def style_oil_pixel(img, offset_x, offset_y, step, size, pos_noise, color_noise):
    h, w = img.shape[:2]
    pixels = []

    for y in range(0, h, step):
        for x in range(0, w, step):
            b, g, r = img[y, x]

            r = min(255, max(0, r + random.randint(-color_noise, color_noise)))
            g = min(255, max(0, g + random.randint(-color_noise, color_noise)))
            b = min(255, max(0, b + random.randint(-color_noise, color_noise)))

            dx = random.randint(-pos_noise, pos_noise)
            dy = random.randint(-pos_noise, pos_noise)

            bw = random.randint(size, size + 1)
            bh = random.randint(size, size + 1)

            px = x + offset_x + dx
            py = y + offset_y + dy

            color = f"rgb({r},{g},{b})"
            pixels.append((px, py, bw, bh, color))

    return pixels
