# Correccion de exposicion.py

import cv2 as cv
import numpy as np


def ajustar_exposicion(imagen, factor):
    """
    Ajusta la exposición de una imagen.

    Args:
        imagen: Imagen a ajustar.
        factor: Factor de ajuste de la exposición.

    Returns:
        Imagen con la exposición ajustada.
    """
    if imagen is None:
        raise ValueError("La imagen no se pudo cargar. Verifique la ruta proporcionada.")

    hsv = cv.cvtColor(imagen, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(hsv)

    v = cv.add(v, int(factor * 255))
    v = np.clip(v, 0, 255)

    hsv_ajustada = cv.merge((h, s, v))
    imagen_ajustada = cv.cvtColor(hsv_ajustada, cv.COLOR_HSV2BGR)

    return imagen_ajustada

# Posibles mejoras:
# 1. Agregar soporte para ajustar otros parámetros como el contraste y la saturación.
# 2. Implementar la opción de ajustes automáticos basados en histogramas.
# 3. Permitir la opción de ajuste en diferentes regiones de la imagen.
# 4. Mejorar la eficiencia del algoritmo para imágenes de alta resolución.
