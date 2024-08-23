# MobyMon Championship

Este repositorio contiene el código y configuración necesarios para combatir en un campeonato de MobyMon utilizando Docker y Docker Compose. El campeonato se basa en una simulación de batallas entre MobyMons, donde cada uno tiene estrategias para atacar o no atacar en cada ronda.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- `Dockerfile`: Contiene las instrucciones para construir la imagen de Docker.
- `docker-compose.yml`: Define los servicios y la configuración de Docker Compose.
- `mobius.py`: Script principal para ejecutar el campeonato.
- `requirements.txt`: Archivo de dependencias

## Construcción y Ejecución

Sigue estos pasos para construir la imagen de Docker y ejecutar el campeonato:

### 1. Clonar el Repositorio

Primero, clona este repositorio a tu máquina local:

```bash
git clone https://github.com/apptec-cl/mobymon-python
cd mobymon-python
```

### 2. Construir la Imagen de Docker

Para construir la imagen de Docker, ejecuta el siguiente comando en el directorio raíz del proyecto:

```bash
docker-compose build
```

Esto construirá la imagen necesaria para ejecutar el campeonato.

### 3. Ejecutar el Campeonato

Una vez que la imagen esté construida, puedes ejecutar el campeonato con:

```bash
docker-compose up
```

Este comando iniciará los contenedores y ejecutará la batalle de MobyMon. El resultado se mostrará en la consola.

### 4. Detener los Contenedores

Después de que el match haya terminado, puedes detener y eliminar los contenedores utilizando:

```bash
docker-compose down
```

Este comando limpiará el entorno y detendrá todos los servicios asociados.
