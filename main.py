import os
import time
import cv2 as cv
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from functions import combine


class WatermarkApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.message_label = None
        self.progress = None
        self.watermark_text = None
        self.process_button = None
        self.watermark_label = None
        self.folder_text = None
        self.watermark_button = None
        self.folder_label = None
        self.folder_button = None
        self.title_label = None
        self.title("Aplicación de Marca de Agua")
        self.geometry("500x450")

        # Intentamos usar el tema 'clam'
        try:
            style = ttk.Style()
            style.theme_use('clam')
        except tk.TclError:
            print("Tema 'clam' no disponible. Usando el tema por defecto de ttk.")

        self.folder_name = ""
        self.watermark_path = ""
        self.file_list = []
        self.watermark = None

        self.create_widgets()

    def create_widgets(self):
        """Crea los widgets de la interfaz gráfica."""
        self.title_label = tk.Label(self, text="Aplicación de Marca de Agua", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.folder_button = tk.Button(self, text="Selecciona Carpeta de Imágenes", command=self.select_folder,
                                       font=("Helvetica", 12))
        self.folder_button.pack(pady=10)

        self.folder_label = tk.Label(self, text="Carpeta seleccionada:", font=("Helvetica", 12))
        self.folder_label.pack(pady=5)
        self.folder_text = tk.Entry(self, font=("Helvetica", 12), state="readonly")
        self.folder_text.pack(pady=5, fill=tk.X, padx=20)

        self.watermark_button = tk.Button(self, text="Selecciona Imagen de Marca de Agua",
                                          command=self.select_watermark, font=("Helvetica", 12))
        self.watermark_button.pack(pady=10)

        self.watermark_label = tk.Label(self, text="Imagen de marca de agua seleccionada:", font=("Helvetica", 12))
        self.watermark_label.pack(pady=5)
        self.watermark_text = tk.Entry(self, font=("Helvetica", 12), state="readonly")
        self.watermark_text.pack(pady=5, fill=tk.X, padx=20)

        self.process_button = tk.Button(self, text="Procesar Imágenes", command=self.process_images,
                                        font=("Helvetica", 12))
        self.process_button.pack(pady=20)
        self.process_button.config(state="disabled")

        self.progress = ttk.Progressbar(self, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)

        self.message_label = tk.Label(self, text="", font=("Helvetica", 12))
        self.message_label.pack(pady=10)

    def select_folder(self):
        """Permite seleccionar una carpeta de imágenes y actualiza la interfaz con la carpeta seleccionada."""
        self.folder_name = filedialog.askdirectory()
        if self.folder_name:
            self.folder_text.config(state="normal")
            self.folder_text.delete(0, tk.END)
            self.folder_text.insert(0, os.path.basename(self.folder_name))
            self.folder_text.config(state="readonly")
            self.file_list = os.listdir(self.folder_name)
            self.check_ready_to_process()

    def select_watermark(self):
        """Permite seleccionar una imagen de marca de agua y la carga en la aplicación."""
        self.watermark_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if self.watermark_path:
            self.watermark_text.config(state="normal")
            self.watermark_text.delete(0, tk.END)
            self.watermark_text.insert(0, os.path.basename(self.watermark_path))
            self.watermark_text.config(state="readonly")
            self.watermark = cv.imread(self.watermark_path, cv.IMREAD_UNCHANGED)
            if self.watermark is None:
                messagebox.showerror("Error", f"No se pudo cargar la imagen de marca de agua '{self.watermark_path}'")
                self.watermark_path = ""
            self.check_ready_to_process()

    def check_ready_to_process(self):
        """Habilita el botón de procesar imágenes si se han seleccionado la carpeta y la imagen de marca de agua."""
        if self.folder_name and self.watermark_path:
            self.process_button.config(state="normal", bg="green", fg="white")
        else:
            self.process_button.config(state="disabled", bg="SystemButtonFace", fg="black")

    def process_images(self):
        """Procesa las imágenes seleccionadas aplicando la marca de agua."""
        if not self.folder_name or not self.watermark_path:
            messagebox.showwarning("Advertencia",
                                   "Debes seleccionar una carpeta de imágenes y una imagen de marca de agua.")
            return

        start_time = time.time()

        total_files = len([file for file in self.file_list if file.lower().endswith(('jpg', 'jpeg', 'png'))])
        processed_files = 0

        destination_folder = os.path.join(self.folder_name, "edited_images")
        os.makedirs(destination_folder, exist_ok=True)

        for file in self.file_list:
            if file.lower().endswith(('jpg', 'jpeg', 'png')):
                image_path = os.path.join(self.folder_name, file)
                destination_path = os.path.join(destination_folder, file)

                shutil.copyfile(image_path, destination_path)

                background = cv.imread(destination_path)
                if background is None:
                    self.message_label.config(text=f"No se pudo cargar la imagen '{file}'", fg="red")
                    continue

                combined = combine(self.watermark, background, .4)
                cv.imwrite(destination_path, combined)
                processed_files += 1
                self.progress["value"] = (processed_files / total_files) * 100
                self.update_idletasks()

        end_time = time.time()
        total_time = end_time - start_time

        messagebox.showinfo("Proceso Completado",
                            f"Fotos editadas con éxito.\nTiempo total de procesamiento: {total_time:.2f} segundos")
        self.progress["value"] = 0


if __name__ == "__main__":
    app = WatermarkApp()
    app.mainloop()

# Posibles mejoras:
# 1. Agregar soporte para más formatos de imagen.
# 2. Mejorar el manejo de errores, por ejemplo, cuando no se puede cargar una imagen.
# 3. Permitir al usuario seleccionar la posición y la transparencia de la marca de agua.
# 4. Optimizar el procesamiento de imágenes para manejar carpetas con gran cantidad de imágenes.
