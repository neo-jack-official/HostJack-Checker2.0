![alt text](https://raw.githubusercontent.com/neo-jack-official/FastJack/master/img/vista01.png)
# HostJack-Checker 2.0 (hostjack.py3)
# Es una Herramienta de comprobacion de estado para Servidores-Web por Neo-Jack ENE/2020

## ¿Qué es HostJack-Checker?
Es una simple herramienta de comprobacion de estado de sitios web.
Evita tener que estar verificando el estado de un sitio miediante un navegador, y cuenta con conexion Tor si es requerido.
Se elimina el metodo: urllib2.urlopen(url,timeout=timeout).getcode() == 200
y fue remplazo por: socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Optimizando su funcionalidad y suprimiendo errores causados por baneos.
HostJack-Checher es rapido simple y seguro.

## Que version python utiliza?
Python 3.6

## Como se que version python tengo?
* `python -V | python3 -V`

## ¿Como funciona HostJack-Checker 2.0?
1. Realiza peticiones al sitio cada 5 Segundos intercalando entre puerto 80 y 443, optimizando la comprobacion.
2. Como respuesta se le notificara si esta conectado a red TOR, el puerto que a utilizar y estado del Servidor: Operativo, No Disponible o TimeOUT.
3. El tiempo de espera es de 5 segundos entre cada puerto, y 10 segundos a la respuesta TimeOUT.
4. Cuenta con acceso a Tor Network mediante el argumento (-T). A proxy por defecto 127.0.0.1:9050
5. Funciona en un LOOP predeterminado de 99.999 peticiones por puerto a verificar.
6. para abortar el programa usar teclas : (Ctrl + Z)

## Como lo utiliso?

Si `hostjack.py3` esta en Escritorio:
1) Abra terminal, Escriba `cd Escritorio`
2) Ejecute bajo Python 3.6:
* `python3 hostjack.py3 www.ejemplo.com` 
* `python3 hostjack.py3 -h` para acceder al menu de ayuda.

## Opciones de Configuracion

* `-h, --help, --ayuda = Menu de Ayuda`
* `-T = Habilitar el enrutamiento TOR, por defecto: Desactivado`
* `-F = Des-habilitar el enrutamiento TOR`

## Ejemplos de comandos.

  Sin TOR:
* `python hostjack.py3 www.ejemplo.com`
* `python hostjack.py3 www.ejemplo.com -F`
  Con TOR:
* `python hostjack.py3 www.ejemplo.com -T`

## Como Instalar PYTHON 3.6 ?
## Linux con SUDO

Abrir terminal:
* `sudo apt-get update`
* `sudo apt-get install build-essential checkinstall`
* `sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev`
* `sudo apt-get install python3.6`

## Tengo problemas para instalar PYTHON 3.6
* `sudo apt-get install software-properties-common`
* `sudo add-apt-repository ppa:deadsnakes/ppa`
* `sudo apt-get update`
* `sudo apt-get install build-essential checkinstall`
* `sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev`
* `sudo apt-get install python3.6`

## Revisamos que python esta instalado correctamente
* `python3 -V`

## Como se si tengo Tor Network instalado?
Abrir Terminal:
* `tor --version`

## Como Instalo Tor Network
* `sudo apt-get update`
* `sudo apt-get install tor`
* `sudo apt-get install torsocks`
* `sudo apt-get install tor-geoipdb`
* `sudo /etc/init.d/tor restart`

