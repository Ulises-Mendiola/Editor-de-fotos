# Conversor_RGBA.py
import cv2 as cv
import numpy as np


def convert_to_rgba(image_path):
    """
    Convierte una imagen RGB a RGBA añadiendo un canal alfa.

    Args:
        image_path: Ruta de la imagen a convertir.

    Returns:
        Ruta de la nueva imagen convertida a RGBA.
    """
    image = cv.imread(image_path, cv.IMREAD_UNCHANGED)

    if image is None:
        raise ValueError("La imagen no se pudo cargar. Verifique la ruta proporcionada.")

    if image.shape[2] == 4:
        return image_path

    b_channel, g_channel, red_channel = cv.split(image)
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255

    img_bgra = cv.merge((b_channel, g_channel, red_channel, alpha_channel))

    new_image_path = image_path.replace('.png', '_rgba.png')
    cv.imwrite(new_image_path, img_bgra)

    return new_image_path

# Posibles mejoras:
# 1. Agregar soporte para otros formatos de imagen.
# 2. Permitir la opción de especificar el valor del canal alfa.
# 3. Optimizar la función para grandes cantidades de imágenes.
# 4. Implementar la opción de convertir imágenes en lotes.
