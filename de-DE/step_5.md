## Zusammenbau des Roboters

Deinn Motorcode funktioniert jetzt und es ist Zeit, deinen Roboter zu konstruieren und zu testen.

Das Grunddesign muss fünf Hauptanforderungen erfüllen:

- Ein montierter Raspberry Pi mit Build HAT
- Zwei parallel zueinander montierte Motoren
- Zwei Räder
- Eine Lenkrolle oder eine Stütze an der Vorderseite
- Ein befestigtes Batteriefach mit Hohlstecker

Der Raspberry Pi und das Build HAT können mit M2 Maschinenschrauben und Muttern an LEGO® Teilen befestigt werden.

![Eine M2-Maschinenschraube und -mutter.](images/m2_machine_screws.jpg)

![Ein LEGO®-Teil, das mit einer M2-Maschinenschraube an einem Raspberry Pi befestigt ist.](images/m2_rpi_attached.jpg)

[[[attach_rpi_to_lego]]]

Du kannst den Raspberry Pi und das Build HAT mit einer Batterie mit Strom versorgen, die an einen Hohlstecker angeschlossen ist. Es werden mindestens fünf AA-Batterien oder eine 9-V-Batterie benötigt.

![Fünf AA-Batterien in einem Batteriegehäuse, verbunden mit einem Hohlstecker.](images/AA_battery.jpg)

![Eine 9-V-Batterie, die an einen Hohlstecker angeschlossen ist.](images/9V_battery.jpg)

Die folgenden Fotos zeigen einige unterschiedliche Designs für den Bau deines LEGO® Autos, die Raspberry Pi, Build HAT und Batterien enthalten.

![Ein einfaches Roboterauto aus vier verschiedenen Blickwinkeln.](images/basic_bot.png)

![Vier Ansichten eines möglichen Roboterautodesigns.](images/bot-grid_2.png)

![Komplexer Jeep-Buggy aus drei Blickwinkeln.](images/buggy3grid.jpg)

--- task ---

Verwende alle LEGO®-Elemente, die du hast, um den Roboter zu bauen, und lassen Sie deiner Fantasie freien Lauf.

--- /task ---

### Testen

Sobald deiin Roboter zusammengebaut ist, solltest du ihn über Bluetooth mit deinem Android-Gerät testen.

--- task ---

Schalte deinen Raspberry Pi ein und führe dann dein Programm `bt_car.py` aus. Teste, ob dein Auto funktioniert, wenn du Bluetooth und die Blue Dot-App von deinem Android-Gerät verwendest.

--- /task ---

Möglicherweise musst du deinen Code ändern, je nachdem, auf welcher Seite des Autos du bist und wie deine Motoren angeschlossen sind.

Als nächstes musst du dafür sorgen, dass dein Raspberry Pi **Headless**läuft. Dies bedeutet, dass dein Code ausgeführt wird, ohne dass ein Monitor, eine Tastatur oder eine Maus angeschlossen sein muss.

Stelle zunächst sicher, dass dein Raspberry Pi [mit einem WiFi-Netzwerk verbunden ist](https://www.raspberrypi.org/documentation/configuration/wireless/desktop.md).

Jetzt kannst du ein Programm namens **cron** verwenden, um dein Python-Skript jedes Mal auszuführen, wenn der Raspberry Pi gebootet wird.

--- task ---

Öffne ein Terminal, indem du <kbd>Strg</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd> auf deiner Tastatur drückst.

--- /task ---

--- task ---

Gib `crontab -e` in das Terminalfenster ein. Wenn du **crontab** zum ersten Mal verwendest, wirst du gefragt, welchen Editor du verwenden möchtest.

```bash
pi@raspberrypi:~ $ crontab -e
no crontab for pi - using an empty one

Select an editor. Um diese Auswahl später zu ändern, führe 'select-editor' aus.
  1. /bin/nano        <---- easiest
  2. /usr/bin/vim.tiny
  3. /bin/ed

Choose 1-3 [1]: 
```

Sofern du keine Erfahrung mit **vim** hast, wähle `1. /bin/nano`.

--- /task ---

Nano wird geöffnet und zeigt die Standardvorlagendatei an.

--- task ---

Verwende die Cursortasten, um zum Ende der Datei zu scrollen. Du kannst dann diese Zeile hinzufügen, die 30 Sekunden wartet und dann deine `bt_car.py` Datei ausführt.

```bash
# m h  dom mon dow   command
@reboot sleep 30 && python3 /home/pi/bt_car.py
```

--- /task ---

--- task ---

Starte deinen Raspberry Pi neu, warte 30 Sekunden und verwende dann deine Blue Dot-App auf deinem Android-Gerät, um eine Verbindung zu deinem Auto herzustellen und es zu steuern.

--- /task ---





