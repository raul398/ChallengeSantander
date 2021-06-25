# Challenge Birras


Sistema desarrollado con Django.

Puede descargar este desarrollo en su escritorio local. Para su ejecucion es necesario descargar e instalar Python 3.8 (puede crear un virtual environment y descargar Python version 3.8).

Virtualenv es una herramienta utilizada para crear un entorno Python aislado. Este entorno tiene sus propios directorios de instalación que no comparten bibliotecas con otros entornos virtualenv o las bibliotecas instaladas globalmente en el servidor.

Al ser un framework web de Python, Django requiere del mismo. Consulte ¿Qué versión de Python puedo usar con Django? para más detalles. Python contiene una base de datos ligera llamada SQLite, por lo que no tendrá que crear una base de datos por el momento.

Obtenga la última versión de Python en https://www.python.org/download/ o con el administrador de paquetes de su sistema operativo.

Una vez instalado Python en su ordenador, debera descargar django en su ordenador utilizando la herramienta pip de Python.

Mas informacion sobre Django en https://docs.djangoproject.com/es/3.2/intro/install/

una vez intalado Python y Django, ingrese por terminal al directorio del repositorio descargado, ñuego al directorio birras y ejecute el comando python manage.py runserver Se actiavara e servidor local de Django que ejecutara el desarrollo en la IP 127.0.0.1:8000


Este sistema permite crear reuniones y calcular la cantidad de bebidas necesarias dependiendo la temperatura y cantidad de invitados.

Crear reunion: Para crear una reunion debera dirigirse a la url 127.0.0.1/admin

Mail: admin@mail.com
Password: admin1234

luego de ingreasar al panel de administrador usted podra crear una reunion en meeting --> +add

debe ingresar los campos solicitados : Nombre de la reunion, cantidad de invitados, fecha y hora.
el sistemas calcula la temperatura mediante https://api.openweathermap.org/
NOTA: se toma la temoeratura de la fecha actual en vez de la de la reunion, ya que para acceder a ese servicio habia que pagar.
luego de tener temperatura y cantidad de invitados, calcula la cantidad de cajas que va a necesitar y luego de crear lo va a mostrar en el panel del adminitrador y en el home. (url: https://127.0.0.1:8000/)

el sistema cuenta con distintas rutas para las API's. Para ver un listado de las mismas es necesario primero hacer logout en el panel del administrador.
la ruta para ver el listados es https://127.0.0.1:8000/apis/

para el consumo de apis externas es necesario instalar requests desde la consola --> pip install requests
para la conversion de json es necesario instalar json desde la consola --> pip install json

para poder visualizar las apis internas se utilizo DRF(Django Rest Framework) por tal motivo en caso de on poder ver la insterfaz de DRF,
 es necesario instalar DRF desde la consola --> pip install djangorestframework

Para mas informacion visite https://www.django-rest-framework.org/


# Challenge Birras



You can download this development on your local desktop. For its execution it is necessary to download and install Python 3.8 (you can create a virtual environment and download Python version 3.8).

Virtualenv is a tool used to create an isolated Python environment. This environment has its own installation directories that do not share libraries with other virtualenv environments or the libraries installed globally on the server.

Being a Python web framework, Django requires it. See What version of Python can I use with Django? for more details. Python contains a lightweight database called SQLite, so you won't have to create a database just yet.

Get the latest version of Python at https://www.python.org/download/ or with your operating system's package manager.

Once Python is installed on your computer, you will need to download django onto your computer using the Python pip tool.

More information about Django at https://docs.djangoproject.com/es/3.2/intro/install/

Once Python and Django have been installed, enter the downloaded repository directory by terminal and execute the command python manage.py runserver The local Django server will be activated and will run development on the IP 127.0.0.1:8000


This system allows you to create meetings and calculate the amount of drinks needed depending on the temperature and number of guests.

Create meeting: To create a meeting you should go to the url 127.0.0.1/admin

Mail: admin@mail.com
Password: admin1234

after entering the administrator panel you can create a meeting in meeting -> + add

You must enter the requested fields: Name of the meeting, number of guests, date and time.
the system calculates the temperature using https://api.openweathermap.org/
NOTE: the temperature of the current date is taken instead of that of the meeting, since to access this service you had to pay.
after having temperature and number of guests, calculate the number of boxes that you will need and after creating it, it will show it in the administrator panel and in the home. (url: https://127.0.0.1:8000/)

the system has different routes for the APIs. To see a list of them, it is first necessary to log out in the admin panel.
the path to see the listings is https://127.0.0.1:8000/apis/

for the consumption of external apis it is necessary to install requests from the console -> pip install requests
for the json conversion it is necessary to install json from the console -> pip install json

In order to visualize the internal apis, DRF (Django Rest Framework) was used for this reason in case of being able to see the DRF interface,
 you need to install DRF from the console -> pip install djangorestframework

For more information visit https://www.django-rest-framework.org/