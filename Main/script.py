import tkinter as tk
from tkinter import filedialog
import shutil
from PIL import Image
import os


def compress_images(file_paths, output_folder, quality=85, reduce_colors=None, reduce_resolution=None):
    """
    Сжимает выбранные изображения с использованием библиотеки Pillow и shutil.

    Parameters:
        file_paths (list): Список путей к выбранным изображениям.
        output_folder (str): Путь к директории для сохранения сжатых изображений.
        quality (int): Качество сжатия для JPEG (от 0 до 100).
        reduce_colors (int): Количество цветов в палитре. Уменьшение этого значения уменьшит размер файла PNG.
        reduce_resolution (tuple): Новое разрешение изображения в виде кортежа (ширина, высота).

    Returns:
        None
    """
    try:
        os.makedirs(output_folder, exist_ok=True)

        for file_path in file_paths:
            filename = os.path.basename(file_path)
            output_path = os.path.join(output_folder, filename)

            # Открываем изображение
            with Image.open(file_path) as img:
                # Уменьшаем количество цветов
                if reduce_colors:
                    img = img.convert('P', palette=Image.ADAPTIVE, colors=reduce_colors)

                # Уменьшаем разрешение с использованием другого метода интерполяции (Image.LANCZOS)
                if reduce_resolution:
                    img = img.resize(reduce_resolution, Image.LANCZOS)

                # Сохраняем с использованием сжатия zlib (для PNG)
                img.save(output_path, format="PNG", optimize=True, quality=quality)

            print(f"Изображение {filename} успешно сжато и сохранено.")
    except Exception as e:
        print(f"Ошибка при сжатии изображений: {e}")


def browse_images():
    file_paths = filedialog.askopenfilenames(
        title="Выберите изображения для сжатия",
        filetypes=[("Изображения", "*.jpg;*.jpeg;*.png")],
    )
    return file_paths


def choose_output_folder():
    output_folder = filedialog.askdirectory(title="Выберите директорию для сохранения сжатых изображений")
    return output_folder


def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Выбор нескольких изображений
    file_paths = browse_images()

    if not file_paths:
        print("Отменено пользователем.")
        return

    # Выбор директории для сохранения сжатых изображений
    output_folder = choose_output_folder()

    if not output_folder:
        print("Отменено пользователем.")
        return

    # Вы можете настроить параметр quality по своему усмотрению.
    compress_images(file_paths, output_folder, quality=95, reduce_colors=256, reduce_resolution=(1200, 1200))


if __name__ == "__main__":
    main()
