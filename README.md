# 📸 Aplicación de Marca de Agua y Mejora de imagen.

Este software es una aplicación de escritorio que permite agregar marcas de agua a imágenes de forma masiva y mejorar brillo y contraste. A continuación, se describen las características y funcionalidades principales:

## 🖥️ Interfaz Gráfica

La aplicación cuenta con una interfaz gráfica desarrollada con **Tkinter**, que incluye los siguientes elementos:

- **Título:** "Aplicación de Marca de Agua" 🏷️
- **Botón para seleccionar la carpeta de imágenes:** Permite al usuario seleccionar una carpeta que contenga las imágenes a las que se les aplicará la marca de agua 📂
- **Etiqueta y campo de texto para mostrar la carpeta seleccionada:** Muestra la ruta de la carpeta seleccionada por el usuario 📁
- **Botón para seleccionar la imagen de la marca de agua:** Permite al usuario seleccionar la imagen que se utilizará como marca de agua 🖼️
- **Etiqueta y campo de texto para mostrar la imagen de la marca de agua seleccionada:** Muestra la ruta de la imagen de marca de agua seleccionada 🌊
- **Botón para procesar las imágenes:** Inicia el proceso de aplicación de la marca de agua a las imágenes seleccionadas 📷
- **Barra de progreso:** Muestra el progreso del procesamiento de las imágenes ⏳
- **Etiqueta de mensajes:** Muestra mensajes de estado e información al usuario 📢

## 📂 Funcionalidades

### Selección de Carpeta de Imágenes
Permite al usuario seleccionar una carpeta que contenga las imágenes a procesar. La aplicación verifica que la carpeta contenga archivos de imagen válidos y actualiza la interfaz en consecuencia.

### Selección de Imagen de Marca de Agua
Permite al usuario seleccionar una imagen que se utilizará como marca de agua. La aplicación carga la imagen y verifica que sea válida.

### Proceso de Aplicación de Marca de Agua
Inicia el proceso de aplicación de la marca de agua a todas las imágenes seleccionadas en la carpeta. Este proceso incluye los siguientes pasos:
- Crear una carpeta llamada `edited_images` dentro de la carpeta seleccionada para almacenar las imágenes procesadas.
- Copiar cada imagen original a la carpeta `edited_images`.
- Aplicar la marca de agua a cada imagen utilizando la función `combine` del módulo `functions.py`.

## 🛠️ Funciones Adicionales

### Función `combine`
Combina una imagen de marca de agua con una imagen de fondo. Ajusta el tamaño de la marca de agua según un factor de escala y la aplica a la imagen de fondo. Utiliza un canal alfa para manejar la transparencia de la marca de agua.

### Función `convert_to_rgba`
Convierte una imagen RGB a RGBA añadiendo un canal alfa. Es útil para asegurar que las imágenes de marca de agua tengan un canal de transparencia.

### Función `ajustar_exposicion`
Ajusta la exposición de una imagen. Convierte la imagen a espacio de color HSV, modifica el canal de valor (v) y vuelve a convertirla a espacio de color BGR.


¡Con esta aplicación podrás agregar marcas de agua a tus imágenes de manera rápida y eficiente, tambien mejora la calidad de la imagen! 🌟
