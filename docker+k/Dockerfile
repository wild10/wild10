# Imagen base con Python 3.9
FROM python:3.9-slim

# Evita prompts interactivos
ENV DEBIAN_FRONTEND=noninteractive

# Dependencias del sistema necesarias para OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
WORKDIR  /app 

# Copiamos requirements primero ( mejor cache)
COPY requirements.txt .

# Actualizamos pip e instalamos dependencias
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del proyecto
COPY app.py . 
COPY yolo12n.pt . 

# Exponemos el API. port. 
EXPOSE 8000


# Comando run FastAPI server

CMD ["uvicorn","app:app", "--host", "0.0.0.0", "--port", "8000"]