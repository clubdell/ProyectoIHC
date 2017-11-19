# Proyecto IHC

**Importante:** Asegurate que estes trabajando en un entorno linux con python y docker instalado.

**Configuracion**

1. Abre una terminal
2. Instala virtualenv `sudo -H pip install virtualenv`
3. Crea el entorno de virtualenv para tus proyectos de python usando python3 `virtualenv --python=python3 <name>`
4. En tu terminal naviga hacia el directorio que contenga el virtualenv `cd <name>`
5. Activa el entorno de virtualenv `source bin/activate`
6. Clona este repositorio
7. Ingresa al directorio del proyecto ciclocelular `cd ciclocelular` e instala las dependencias `pip install -r requeriments.txt`
8. Crea tu archivo de variables de entorno `cp .env.example .env` y editalo con tus configuraciones
9. Construye las imagenes de docker para los servicios `docker-compose build`
10. Levanta los servicios `docker-compose up -d`
11. Ejecuta `docker-compose run web /usr/local/bin/python manage.py migrate` para verficar que haya conexion con MySQL
12. Por ultimo ejecuta `docker-compose run web /usr/local/bin/python manage.py collectstatic --noinput` para recolectar los archivos _estaticos (JS, CSS, images)_ que usa el login y aplicaciones de Django
