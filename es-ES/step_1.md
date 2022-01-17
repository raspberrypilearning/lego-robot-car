## Introducción

Usa LEGO® y Raspberry Pi Build HAT para construir un carro robot, luego prográmalo para que puedas controlarlo con una conexión Bluetooth desde tu teléfono Android. Luego agrega algunos LED para deslumbrar a sus amigos.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">El nombre [Bluetooth](https://en.wikipedia.org/wiki/Bluetooth)</span> fue propuesto en 1997 por Jim Kardach de Intel. En el momento de esta propuesta, estaba leyendo la novela histórica de Frans G. Bengtsson * The Long Ships * sobre los vikingos y el rey danés del siglo X, Harald Bluetooth. Bluetooth era el apodo del rey Harald, quien unió a las tribus danesas en un solo reino, al igual que Bluetooth une los protocolos de comunicación.
</p>

Vas a:
+ Controlar los motores LEGO® Technic ™ usando un Raspberry Pi Build HAT
+ Usar Bluetooth para enviar señales a la Raspberry Pi
+ Aprender a controlar los LEDs usando gpiozero en la Raspberry Pi

--- no-print ---

![Una foto del robot con ruedas LEGO® terminado con la Raspberry Pi y Build HAT montados en el centro. Una placa de pruebas con cables conectados a LEDs en la parte superior de la pila.](images/lego-bot.gif)

--- /no-print ---

Construirás un carro con ruedas. Su movimiento estará determinado por dos ruedas impulsadas por separado colocadas a cada lado del automóvil, lo que le permitirá moverse hacia adelante, hacia atrás y girar. Opcionalmente, puedes agregar LEDs al automóvil para que actúen como luces de freno, indicadores o faros delanteros.

--- print-only ---

![Proyecto completo.](images/buggy.JPG)

--- /print-only ---

### Necesitarás

+ Una computadora Raspberry Pi que ejecuta la última versión de escritorio del sistema operativo Raspberry Pi
+ Un Build HAT Raspberry Pi
+ 2 × motores LEGO® Technic ™
+ Variedad de LEGO®, incluidas las ruedas (utilizamos una selección del kit [LEGO® Education SPIKE ™ Prime](https://education.lego.com/en-gb/product/spike-prime))
+ Un teléfono móvil o tableta Android
+ 5 pilas AA y un contenedor de pilas con un conector de barril

### Software

+ La biblioteca build HAT de Python para controlar el build HAT
+ Biblioteca Blue Dot de Python y la aplicación Blue Dot para Android
+ la biblioteca gpiozero de Python


--- collapse ---
---
title: Información adicional para educadores
---

Puedes descargar el proyecto completo [aquí](https://rpf.io/p/en/bt-robot-car-go){: target = "_ blank.

Si necesitas imprimir este proyecto, usa la [versión para imprimir](https://projects.raspberrypi.org/en/projects/bt-robot-car/print){:target="_blank"}.

--- /collapse ---

Antes de comenzar, deberás configurar tu computadora Raspberry Pi e instalar el Build HAT:

--- task ---

Monta tu Raspberry Pi en la placa de construcción LEGO usando pernos y tuercas M2, asegurándote de que la Raspberry Pi esté en el lado sin borde':

 ![Raspberry Pi atornillada a una placa de construcción LEGO magenta.](images/build_11.jpg)

--- /task ---

Montar la Raspberry Pi de esta manera permite un fácil acceso a los puertos, así como a la ranura de la tarjeta SD. La placa de construcción te permitirá conectar la Raspberry Pi a la estructura principal de tu tablero más fácilmente.

--- task ---

Alinea el Build HAT con la Raspberry Pi, asegurándote de que puedes ver la etiqueta `This way up`. Asegúrate de que todos los pines GPIO estén cubiertos por el HAT y presiona firmemente. (El ejemplo usa un encabezado de apilamiento [](https://www.adafruit.com/product/2223){: target = "_ blank"}, lo que alarga los pines)

![Imagen de los pines GPIO asomandose por la parte superior del Build HAT.](images/build_15.jpg) ![Animación que muestra el ajuste de Buildhat a Raspberry Pi](images/haton.gif)

--- /task ---

Ahora debes encender tu Raspberry Pi utilizando el conector de barril de 7.5V en el Build HAT, lo cual te permitirá usar los motores.

--- task ---

Si aún no lo ha hecho, configura tu Raspberry Pi siguiendo estas instrucciones:

[Configurando tu Raspberry Pi](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up){:target="_blank"}

--- /task ---

--- task ---

Una vez que la Raspberry Pi se haya iniciado, abre la herramienta de configuración de Raspberry Pi haciendo clic en el botón Menú de Raspberry y luego seleccionando "Preferencias" y luego "Configuración de Raspberry Pi".

Haz clic en la pestaña "interfaces" y ajusta la configuración Serie como se muestra a continuación:

![Imagen que muestra la pantalla de configuración del sistema operativo Raspberry Pi con el puerto en serie habilitado y la consola en serie deshabilitada](images/configshot.jpg)

--- /task ---

--- task ---

También necesitarás instalar la biblioteca buildhat de python siguiendo estas instrucciones:

--- collapse ---
---
title: Instala la biblioteca buildhat de Python
---

Abre una ventana de terminal en tu Raspberry Pi presionando <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>.

En el indicador, escribe: `sudo pip3 install buildhat`

Presiona <kbd>Entrar</kbd> y espera el mensaje "installation completed".

--- /collapse ---

--- /task ---