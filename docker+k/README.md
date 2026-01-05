
# ¿ Que es un Container?
* Un contenedor es una instancia de ejecucion de una imagen.

dicho de otra forma:

> Un container es un proceso aislado del sistema host que corre usando una imagen como base


_Container = imagen + proceso(s)corriendo + estado2_


# Caracteristicas de una container
- Un entorno aislado.
- Creado a partir de una imagen.
- Donde hay procesos corriendo.
- Tiene : filesystem, Process Id, red, variables de entorno, estasos(running, exited).ß

# instrucciones de contenedor

comandos para crear imagen y ejecución de contenedor

# create imagen
```bash
# create image
docker built -t read-opencv:1.0 .
# otra forma 
docker build --no-cache -t read-opencv:1.2 .

```
- t: -> nombre y version (tag).
- . -> contexto de construccion(directorio actual).

```bash
# run interactive mode 
docker run -it read-opencv:1.0 bash
```
- it -> terminal interactivo .
- --rm -> el container se borra al salir(tmp).
- read-opencv:1.0 -> la imagen.
- bash -> entras al contenedor.

```bash
# create again new tag image version 2
docker build --no-cache -t read-opencv:1.2 .

# remove image 
docker rmi read-opencv:1.2 
```
 - no-cache -> fuerza a res instalar todo el pip en el container.

 
 ## run the docker 

Despues de ejecutar exitosamente y ver la imagen creada con **docker images**
 ```bash
 # check docker running 
  docker ps

  # run the api docker in the port :8000
  docker run -d --name yolo-api -p 8000:8000 read-opencv:1.0

  # to check the exposes api:
  curl http://localhost:8000/docs
 ```

 - d --> modo desacoplado: no se carga en el terminal (segundo plano)

 ## run Cliente.

 ```bash
 source new_env/bin/activate
 cd Documents/wild10/docker+k
 python main.py

 ```


 ## usar orquestador de container: docker-compose

 en vez de usar docker run -d ... usar : docker compuse up.

 se crea al file docker-compose.yml <<--orquestador
 
 ```bash
 # Detener y eliminar container actual
 docker stop yolo-api
 docker rm yolo-api
 # 
  docker compose up -d
 ```