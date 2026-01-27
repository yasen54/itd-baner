import cv2
import json
import numpy as np

# НАСТРОЙКИ

CANVAS_W = 800
CANVAS_H = 267

PIXEL_STEP = 1   # шаг по пикселям
DOT_SIZE = 1    # размер точки на canvas

# ПРЕОБРАЗОВАНИЕ КАРТИНКИ В ПИКСЕЛИ

def image_to_pixels(path):
    img = cv2.imread(path)
    h, w = img.shape[:2]

    scale = min(CANVAS_W / w, CANVAS_H / h)
    new_w, new_h = int(w * scale), int(h * scale)
    offset_x = (CANVAS_W - new_w) // 2
    offset_y = (CANVAS_H - new_h) // 2

    resized = cv2.resize(img, (new_w, new_h))

    pixels = []

    for y in range(0, new_h, PIXEL_STEP):
        for x in range(0, new_w, PIXEL_STEP):
            b, g, r = resized[y, x][:3]  # cv2 хранит в BGR
            color = f'rgb({int(r)}, {int(g)}, {int(b)})'

            px = x + offset_x
            py = y + offset_y
            pixels.append({
                "x": int(px),
                "y": int(py),
                "color": color
            })

    print(f"Pixels to draw: {len(pixels)}")
    return pixels

# ГЕНЕРАЦИЯ JS
def generate_js(pixels):
    out = [
        "(async function(){",
        "  try {",
        "    const canvas = document.querySelector('.drawing-canvas');",
        "    if (!canvas) { console.error('Canvas not found'); return; }",
        "    const ctx = canvas.getContext('2d');"
    ]

    for px in pixels:
        out.append(f'    ctx.fillStyle = "{px["color"]}";')
        out.append(f'    ctx.fillRect({px["x"]}, {px["y"]}, {DOT_SIZE}, {DOT_SIZE});')

    out.append("  } catch(e) { console.error('SCRIPT ERROR:', e); }")
    out.append("})();")

    return "\n".join(out)

# ЗАПУСК
if __name__ == "__main__":
    pixels = image_to_pixels("input.png")
    js = generate_js(pixels)

    with open("output.js", "w", encoding="utf-8") as f:
        f.write(js)

    print("✔ JS saved to output.js")
