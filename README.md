# Techforb-challenge-backend

Repositorio para el Challenge de la posicion Dev. Backend para Techforb.

Simula el manejo de un sistema Bancario, con creacion de Usuarios en Base de datos, las tarjetas que generen y las transacciones que se realicen.

## Funcionalidades

### Usuarios

* Creacion de Usuarios
* Inicio de Sesion
* Cerrar Sesion
* Eliminar Usuario
* Obtener Todos los Usuarios

### Tarjetas

* Pedir Tarjeta
* Ver Datos de una tarjeta 
* Eliminar Tarjeta

### Transacciones

* Depositar Dinero
* Extraer Dinero
* Transferir Dinero
* Ver historial de Transacciones


## Prerequisitos

* Tener [Git](https://git-scm.com/) instalado 
* Tener instalado [Python](https://www.python.org/downloads/)
* (Windows)Tener la Virtualizacion de Windows Activada, link para ver como hacerlo [acá](https://support.microsoft.com/es-es/windows/habilitar-la-virtualizaci%C3%B3n-en-equipos-windows-11-c5578302-6e43-4b4b-a449-8ced115f58e1)
* Tener instalado Docker
    * (Windows) Si no lo tienes, descarga e instala Docker Desktop desde [este link](https://www.docker.com/products/docker-desktop/)

## Clonar Repositorio

```
git clone https://github.com/RooCordoba/Techforb-challenge-backend.git
```
```
cd Techforb-challenge-backend
```

## Para correr el programa

Abrir la aplicacion de Docker Desktop

### Si quiero que la base de datos se me guarde localmente:

En la terminal y dentro de la carpeta raiz del proyecto colocar el siguiente comando:

```
docker-compose up
```

### Si quiero probar los endpoins en una base de datos en memoria:

En la terminal y dentro de la carpeta raiz del proyecto colocar el siguiente comando:

```
docker build -t techforb-challenge-backend-app .
```
```
docker run -p 5000:5000 techforb-challenge-backend-app
```


En ambas opciones instalara todos los requerimientos de requirements.txt y todo lo necesario para que el proyecto funcione y creará la imagen para luego poder correrla.

Se iniciara el programa en [localhost:5000](http://localhost:5000/). Para interactuar con los endpoints, ir a esa direccion.

**Para detener el programa, apretar 'Ctrl + C'**  


## Tecnologías utilizadas

* Python
* Flask
* Docker
* SQLAlchemy
* flask_restx (para una interfaz visual mas amigable en los endpoints)

### Imagenes de muestra del proyecto:

![Image Text](https://github.com/RooCordoba/Techforb-challenge-backend/blob/develop/src/images_git/image1.png)
![Image Text](https://github.com/RooCordoba/Techforb-challenge-backend/blob/develop/src/images_git/image2.png)
![Image Text](https://github.com/RooCordoba/Techforb-challenge-backend/blob/develop/src/images_git/image3.png)