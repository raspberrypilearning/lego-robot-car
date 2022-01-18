## Steuern der Motoren mit Blue Dot

Die Blue Dot-App und die Python-Bibliothek können verwendet werden, um deine LEGO® Technic™-Motoren von deinem Gerät aus zu steuern.

--- task ---

Öffne die Datei `bt_car.py` erneut und richte Blue Dot oben in der Datei ein. Außerdem solltest du den Import von `sleep` durch `from signal import pause` ersetzen.

--- code ---
---
language: python 
filename: bt_car.py 
line_numbers: true 
line_number_start: 1
line_highlights: 2,3,7
---

from buildhat import Motor    
from bluedot import BlueDot from signal import pause

motor_links = Motor('A')     
motor_rechts = Motor('B')     
punkt = BlueDot()

--- /code ---

--- /task ---

--- task ---

Entferne die `for` Schleife aus deinem aktuellen Code, sodass der vollständige Code wie folgt aussieht:

--- code ---
---
language: python 
filename: bt_car.py 
line_numbers: true 
line_number_start: 1
line_highlights:
---

from buildhat import Motor    
from bluedot import BlueDot     
from signal import pause

motor_links = Motor('A')     
motor_rechts = Motor('B')     
punkt = BlueDot()


def stop():     
    motor_links.stop()     
    motor_rechts.stop()


def vorwaerts():     
    motor_links.start(-100)     
    motor_rechts.start(100)


def zurueck():     
    motor_links.start(100)     
    motor_rechts.start(-100)


def rechts():     
    motor_links.start(-100)     
    motor_rechts.start(-100)


def links():     
    motor_links.start(100)     
    motor_rechts.start(100)     
--- /code ---

--- /task ---

--- task ---

Füge nun am Ende deines Skripts eine Funktion hinzu, die Blue Dot verwendet, um die **vorwaerts** Funktion `aufzurufen`.

--- code ---
---
language: python 
filename: bt_car.py 
line_numbers: true 
line_number_start: 34
line_highlights:
---

def bewege(pos):     
    if pos.top:     
        vorwaerts()

--- /code ---

--- /task ---

Die Funktion `bewege` hat einen einzigen Parameter, nämlich `pos`. Dieser wird automatisch an die Funktion übergeben, je nachdem wo der Blaue Punkt berührt wird.

--- task ---

Füge am Ende deines Codes zwei Methodenaufrufe hinzu. Diese lassen das Auto vorwärts fahren und anhalten. Der letzte Befehl stellt sicher, dass das Programm nicht einfach am Ende des Skripts endet.

--- code ---
---
language: python 
filename: bt_car.py 
line_numbers: true 
line_number_start: 39
line_highlights:
---

punkt.when_pressed = bewege    
punkt.when_released = stop   
pause()

--- /code ---

--- /task ---

--- task ---

Führe deinen Code aus. Drücke in der Blue Dot-App auf deinem Gerät auf den blauen Punkt oben und die Motoren sollten sich drehen. Wenn du deinen Finger vom blauen Punkt nimmst, sollten die Motoren stoppen.

--- /task ---

Im Moment drehen die Motoren die Räder nur in Vorwärtsrichtung. Mit dem Parameter `pos` kannst du sie in alle Richtungen drehen lassen.

--- task ---

Füge deiner `bewege` Funktion Code hinzu, damit die Motoren das Auto nach hinten, links und rechts bewegen.

--- code ---
---
language: python 
filename: bt_car.py 
line_numbers: true 
line_number_start: 32
line_highlights: 37-42
---


def bewege(pos):    
    if pos.top:    
        vorwaerts()    
    elif pos.bottom:    
        zurueck()    
    elif pos.left:    
        links()     
    elif pos.right:    
        rechts()


--- /code ---

--- /task ---

--- task ---

Führe deinen Code erneut aus und teste ihn mit der Blue Dot-App. Wenn du rechts, links und unten auf den blauen Punkt drückst, sollten sich die Motoren jetzt in verschiedene Richtungen bewegen.

--- /task ---

Du kannst deinem Code eine einzelne Zeile hinzufügen, sodass Blue Dot nicht nur auf Drücken reagiert, sondern auch darauf, wenn dein Finger über den blauen Punkt fährt.

--- task ---

Fügee diese einzelne Linie hinzu, damit die Motoren auf Bewegungen auf dem blauen Punkt reagieren.

--- code ---
---
language: python 
filename: 
line_numbers: true 
line_number_start: 43
line_highlights: 47
---


punkt.when_pressed = bewege    
punkt.when_released = stop    
punkt.when_moved = bewege

--- /code ---

--- /task ---

--- task ---

Führe dein Programm aus und experimentiere damit, den blauen Punkt auf deinem Android-Gerät zu drücken und deinen Finger an verschiedene Positionen zu bewegen. Die Motoren sollten sich in verschiedene Richtungen drehen und stoppen, wenn du deinen Finger vom blauen Punkt nimmst.

--- /task ---

Um die vollständige Dokumentation zu BlueDot zu lesen, [klicke hier](https://bluedot.readthedocs.io/de-DE/latest/).

--- save ---
