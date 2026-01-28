import tkinter as tk
from tkinter import filedialog, ttk, messagebox

from processor import load_and_scale_image
from styles import style_pixel, style_oil_pixel
from js_generator import generate_js


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Canvas Generator")
        self.root.geometry("300x420")

        self.image_path = None

        ttk.Button(root, text="Выбрать изображение", command=self.choose_image).pack(pady=5)

        ttk.Label(root, text="Стиль").pack()
        self.style = ttk.Combobox(root, values=["Pixel", "Oil Pixel"], state="readonly")
        self.style.current(0)
        self.style.pack()

        ttk.Label(root, text="Детализация").pack()
        self.detail = ttk.Scale(root, from_=1, to=10, orient="horizontal")
        self.detail.set(2)
        self.detail.pack()

        ttk.Label(root, text="Размер мазка").pack()
        self.size = ttk.Scale(root, from_=1, to=6, orient="horizontal")
        self.size.set(2)
        self.size.pack()

        ttk.Label(root, text="Шум позиции").pack()
        self.pos_noise = ttk.Scale(root, from_=0, to=5, orient="horizontal")
        self.pos_noise.set(1)
        self.pos_noise.pack()

        ttk.Label(root, text="Шум цвета").pack()
        self.color_noise = ttk.Scale(root, from_=0, to=30, orient="horizontal")
        self.color_noise.set(5)
        self.color_noise.pack()

        ttk.Button(root, text="Сгенерировать JS", command=self.generate).pack(pady=10)

    def choose_image(self):
        self.image_path = filedialog.askopenfilename(
            filetypes=[("Images", "*.png *.jpg *.jpeg")]
        )

    def generate(self):
        if not self.image_path:
            messagebox.showerror("Ошибка", "Выберите изображение")
            return

        img, ox, oy = load_and_scale_image(self.image_path)

        step = int(self.detail.get())
        size = int(self.size.get())

        if self.style.get() == "Pixel":
            pixels = style_pixel(img, ox, oy, step, size)
        else:
            pixels = style_oil_pixel(
                img, ox, oy,
                step,
                size,
                int(self.pos_noise.get()),
                int(self.color_noise.get())
            )

        js = generate_js(pixels)

        with open("output.js", "w", encoding="utf-8") as f:
            f.write(js)

        messagebox.showinfo("Готово", "output.js создан")


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
