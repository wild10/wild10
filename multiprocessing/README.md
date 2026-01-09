# Python Parallel Computing: Ejecución Paralela de Modelo Detector de Personas 🚀

Este repositorio contiene implementaciones avanzadas y optimizadas para el procesamiento en paralelo en Python, diseñadas para acelerar tareas de **MLOps y Visión por Computadora (Computer Vision)**.

## 📌 Descripción

El objetivo de este proyecto es demostrar cómo superar el **GIL (Global Interpreter Lock)** de Python utilizando el módulo `multiprocessing` para acelerar la **inferencia de modelos**.

Específicamente, se muestra la ejecución de un modelo ligero de detección de personas sobre múltiples *frames* o imágenes de forma concurrente, distribuyendo la carga en todos los núcleos del procesador para maximizar el *throughput* (rendimiento de inferencia).

## 🛠 Skills Implementadas
*   **Paralelismo a nivel de procesos:** Uso eficiente de `multiprocessing.Pool` y `starmap` para distribuir la carga de inferencia.
*   **Gestión de recursos:** Carga del modelo (ej. OpenCV DNN o TensorFlow Lite) en cada proceso hijo de manera eficiente.
*   **Benchmark de inferencia:** Comparación de tiempos de ejecución (Secuencial vs. Paralelo) en la detección.
*   **Robustez:** Manejo seguro de la carga y descarga de modelos en entornos de ejecución paralela.

## 📂 Estructura del Módulo
*   `human_detector.py`: Script principal que contiene la lógica de carga y ejecución del modelo.
*   `pool_executor.py`: Uso de `Pool` para la inferencia concurrente de imágenes.
*   `benchmarks/`: Scripts para medir la aceleración (speedup) obtenida en la detección de personas.

## 🚀 Ejemplo de Uso (Inferencia Paralela)

```python
import multiprocessing as mp
import cv2
import time

def detect_humans(image_path, model_config, model_weights):
    # Cargar modelo (ej: YOLO, SSD) dentro del proceso hijo
    net = cv2.dnn.readNetFromDarknet(model_config, model_weights)
    image = cv2.imread(image_path)
    # ... (lógica de preprocesamiento y detección) ...
    return f"Detección completada para {image_path}"

if __name__ == "__main__":
    image_list = ['img1.jpg', 'img2.jpg', 'img3.jpg', 'img4.jpg']
    config = 'yolov3.cfg'
    weights = 'yolov3.weights'

    # Prepara los argumentos para starmap
    args = [(img, config, weights) for img in image_list]
    
    start_time = time.time()
    with mp.Pool(processes=4) as pool:
        results = pool.starmap(detect_humans, args)
    end_time = time.time()

    print(f"Inferencia completada en {end_time - start_time:.2f} segundos.")

