# Kodi para Dummies

Todo lo necesario para poner en funcionamiento el sistema multimedia Kodi en una Raspberry Pi 3 o 3+ sin necesidad de grandes configuraciones ni conocimientos.

Y para mayor seguridad, por defecto está configurado para que no se pueda acceder desde fuera de la propia red en la que está instalado.

Se han instalado los componentes mínimos para poder disfrutar de una mejor experiencia.

## Funcionalidades principales

### Sistema multimedia

* Reproduce contenido tanto películas como música
* Descarga automática de información extra tanto para películas y series como para música: portadas, sinopsis, trailers, artistas, género, etc

**NOTA**: El contenido visual en 4k no está soportado.

*Si se intenta reproducir contenido en 4k el sistema se reiniciará continuamente.*

### Control remoto

Permite controlar el sistema a través de un cliente conectado en la misma red, como un dispositivo móvil o un PC.

Testeado en [Kore](https://play.google.com/store/apps/details?id=org.xbmc.kore&hl=es&gl=US) para Android.

**Configuración de Kore**:
* Puerto: 37999
* Usuario: kodi
* Contraseña: kodi

### Descarga de contenido a través de P2P

Permite la descarga de nuevo contenido a través de un cliente conectado a la misma red, como un dispositivo móvil o un PC. Este cliente será el que lance las descargas a través de ficheros .torrent que se ejecutarán internamente en el programa Transmission.

Testeado en [Transmission Remote](https://play.google.com/store/apps/details?id=net.yupol.transmissionremote.app&hl=es&gl=US) para Android.

**Configuración de Transmission Remote**
* Puerto: 9091
* Sin credenciales (ni usuario ni contraseña)

El programa requiere de diversas carpetas en el disco duro externo. La estructura es la siguiente:
- Disco duro externo *portable*
  - *torrent*
    - *descargas*: descargas finalizadas. Todo el contenido puede ser borrado, modificado y/ o movido a su respectiva carpeta
    - *watch*: no borrar ni modificar
    - *incompletos*: no borrar ni modificar

**Nota**: No fomentamos la piratería, por favor haz un uso legal de la herramienta.

### Gestión avanzada

Permite controlar de forma avanzada el sistema a través de un cliente SSH conectado en la misma red, como un dispositivo móvil o un PC.

Testeado en [RaspController](https://play.google.com/store/apps/details?id=it.Ettore.raspcontroller&hl=es&gl=US) para Android.

**Configuración de RaspController**
* Usuario: root
* Contraseña: libreelec

### PIN

Permite un PIN maestro que evita el cambio de configuración.

**Código Maestro**
* PIN: 0000

## Otras funcionalidades

Soporte de control remoto con:

* Mando XBox
* Mando PlayStation
* Ratón y teclado
* Mando a distancia TV (necesario TV con HDMI-CEC)

NOTA: *Hay una pre-configuración por defecto pero se puede modificar con el add-on Keymap Editor*

## Información del sistema

Nombre y versión: [Kodi 18.9 Leia](https://kodi.tv/)

Version del sistema operativo base: [LibreELEC-RPi2.arm-9.2.6.img](https://libreelec.tv/downloads_new/raspberry-pi-3-3/) para Raspberry Pi 3 / 3+

## Configuración pre-programada

Firewall activado, que impide la entrada desde afuera de la red. No se puede acceder desde Internet

PIN Maestro activado

Disco duro externo auto-montado en */var/media/portable*

  * Sistema de ficheros recomendado: exFAT o FAT32
  * REQUERIDO. Etiqueta de volumen: portable
  
Colecciones de películas, series y música enlazadas en carpetas del disco duro externo *portable*

Sistema de carpetas para Transmission enlazadas en carpetas del disco duro externo *portable*

