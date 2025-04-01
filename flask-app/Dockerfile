# FROM: La imagen base que se usará para crear la imagen de Docker.
# En este caso, se utiliza una imagen de Python 3.9 en su versión slim.
FROM python:3.9-slim
LABEL author="Hiram Castillo - hiramcastillo36@gmail.com"

# WORKDIR: Establece el directorio de trabajo dentro del contenedor.
# En este caso, se establece en /code.
# Esto significa que cualquier comando posterior se ejecutará en este directorio.
WORKDIR /code

# COPY: Copia el archivo requirements.txt desde el directorio actual en la máquina host
# al directorio de trabajo dentro del contenedor.
# Esto es útil para instalar las dependencias de la aplicación.
COPY requirements.txt .

# RUN: Ejecuta un comando dentro del contenedor.
# En este caso, se instala pipenv y luego se instalan las dependencias
# especificadas en el archivo requirements.txt.
# La opción --no-cache-dir se utiliza para evitar que pip almacene en caché los paquetes descargados,
# lo que reduce el tamaño de la imagen final.
RUN pip install --no-cache-dir -r requirements.txt

# ENV: Establece variables de entorno dentro del contenedor.
# Estas variables se utilizan para configurar la aplicación Flask.
# FLASK_APP: Especifica el nombre del archivo principal de la aplicación Flask.
# FLASK_ENV: Establece el entorno de la aplicación (desarrollo o producción).
# FLASK_DEBUG: Habilita el modo de depuración de Flask.
# FLASK_RUN_PORT: Especifica el puerto en el que se ejecutará la aplicación Flask.
# FLASK_RUN_HOST: Especifica la dirección IP en la que se ejecutará la aplicación Flask.
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV FLASK_RUN_PORT=8000
ENV FLASK_RUN_HOST=0.0.0.0

# EXPOSE: Informa a Docker que el contenedor escuchará en el puerto especificado en tiempo de ejecución.
EXPOSE 8000

# CMD: Especifica el comando que se ejecutará cuando se inicie el contenedor.
# En este caso, se inicia la aplicación Flask utilizando el comando "flask run".
# Esto iniciará el servidor de desarrollo de Flask y la aplicación estará disponible en el puerto 8000.
CMD ["flask", "run"]
