import cv2 as cv
import numpy as np
from tqdm import tqdm


def combine(watermark, background, scale_factor):
    """
    Combina una marca de agua con una imagen de fondo.

    Args:
        watermark: Imagen de la marca de agua (RGBA).
        background: Imagen de fondo (BGR).
        scale_factor: Factor de escala para ajustar el tamaño de la marca de agua.

    Returns:
        Imagen combinada con la marca de agua aplicada.
    """
    if len(background.shape) < 3 or len(watermark.shape) < 3:
        raise ValueError("Las imágenes deben ser de al menos 3 canales (BGR/RGBA)")

    h1, w1 = background.shape[:2]
    h2, w2 = watermark.shape[:2]

    scale_factor_2 = h2 / w2
    new_width = int(w1 * scale_factor)
    new_height = int(new_width * scale_factor_2)

    watermark_resized = cv.resize(watermark, (new_width, new_height))

    watermark_alpha = watermark_resized[:, :, 3] / 255
    watermark_colors = watermark_resized[:, :, :3]

    alpha_mask = np.dstack((watermark_alpha, watermark_alpha, watermark_alpha))

    h3, w3 = watermark_resized.shape[:2]
    background_subsection = background[0:h3, 0:w3]

    # Inicializar la barra de progreso
    with tqdm(total=h3, desc="Combinando imágenes", ncols=100,
              bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]", colour='green') as pbar:
        for i in range(h3):
            result = background_subsection[i] * (1 - alpha_mask[i]) + watermark_colors[i] * alpha_mask[i]
            background[i:i + 1, 0:w3] = result
            pbar.update(1)

    return background

# Posibles mejoras:
# 1. Permitir la opción de colocar la marca de agua en diferentes posiciones de la imagen.
# 2. Implementar diferentes modos de fusión de la marca de agua (por ejemplo, multiplicar, añadir).
# 3. Agregar la posibilidad de ajustar la opacidad de la marca de agua.
# 4. Mejorar la eficiencia del algoritmo para manejar imágenes de mayor resolución.
