import cv2

CANVAS_W = 800
CANVAS_H = 267


def load_and_scale_image(path):
    img = cv2.imread(path)
    if img is None:
        raise ValueError("Не удалось загрузить изображение")

    h, w = img.shape[:2]
    scale = min(CANVAS_W / w, CANVAS_H / h)

    new_w = int(w * scale)
    new_h = int(h * scale)

    offset_x = (CANVAS_W - new_w) // 2
    offset_y = (CANVAS_H - new_h) // 2

    resized = cv2.resize(img, (new_w, new_h))
    return resized, offset_x, offset_y
