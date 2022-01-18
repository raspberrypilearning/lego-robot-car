## Einrichten der LEGO® Spike™ Motoren

Es ist einfacher, dein Programm zu testen und zu entwickeln, bevor du deinen Roboter baust. Dies verringert die Gefahr, dass dein wunderschönes Modell ruiniert wird, wenn ein Motor den Roboter unerwartet in die falsche Richtung schickt und er von deinem Schreibtisch rauscht (obwohl das Gute an LEGO® natürlich ist, dass du ihn immer wieder aufbauen kannst).

Mit dem Raspberry Pi Build HAT und seiner Python-Bibliothek kannst du LEGO® Technic™-Motoren direkt von deinem Raspberry Pi-Computer aus steuern.

Stecke zwei Motoren in die Ports A und B des Raspberry Pi Build HAT. Verbinde deinen Batteriehalter mit der Hohlstecker-Buchse am Build HAT und schalte ihn ein.

### Lass die Motoren drehen

--- task ---

Öffne Thonny auf deinem Raspberry Pi aus dem Menü **Programmierung**.

--- /task ---

--- task ---

Verwende den folgenden Code, um beide Motoren 10 Sekunden lang mit 50% ihrer maximalen Geschwindigkeit laufen zu lassen. (Sie werden nacheinander laufen, nicht zusammen.)

--- code ---
---
language: python filename: bt_car.py line_numbers: true line_number_start:
line_highlights:
---

from buildhat import Motor   
from time import sleep

motor_links = Motor('A')   
motor_rechts = Motor('B')   
motor_links.run_for_seconds(seconds=10, speed=50)   
motor_rechts.run_for_seconds(seconds=10, speed=-50)

--- /code ---

--- /task ---

--- task ---

Führe dein Programm aus und überprüfe, ob sich die Motoren drehen.

--- /task ---

Dein aktuelles Programm sollte die Motoren in entgegengesetzte Richtungen bewegen, da die Motoren auf gegenüberliegenden Seiten des Fahrzeugchassis montiert werden. Eine Drehung gegen den Uhrzeigersinn am linken Rad bewegt den Roboter also vorwärts, während auf der rechten Seite eine Drehung im Uhrzeigersinn erforderlich ist.

Nachdem du die Motoren getestet hast, kannst du Funktionen erstellen, um die Motoren zum Stoppen und Vorwärtsfahren zu bringen.

--- task ---

Entferne die beiden Codezeilen, die die Motoren 10 Sekunden lang laufen lassen, und füge diese beiden Funktionen hinzu. Die Funktion `start()` funktioniert anders als die `run` Funktion der LEGO-Motoren, sodass sie diesmal gleichzeitig laufen.

--- code ---
---
language: python filename: bt_car.py line_numbers: true line_number_start:
line_highlights: 7-14
---

from buildhat import Motor   
from time import sleep

motor_links = Motor('A')    
motor_rechts = Motor('B')

def stop():    
motor_links.stop()    
motor_rechts.stop()


def vorwaerts():     
motor_links.start(50)     
motor_rechts.start(-50)


--- /code ---

--- /task ---

--- task ---

Teste deine Funktionen, indem du die folgende Start-Stopp-Start-Stopp-Sequenz hinzufügst:

--- code ---
---
language: python filename: bt_car.py line_numbers: true line_number_start: 17
line_highlights:
---

for i in range(2):    
vorwaerts()    
sleep(1)    
stop()    
sleep(1)

--- /code --- --- /task ---


Sobald das funktioniert, füge drei weitere Funktionen hinzu, um den Roboter nach hinten, links und rechts zu bewegen.

--- task ---

Kehre einfach die Richtungen beider Motoren um, um den Roboter rückwärts zu bewegen.

--- code ---
---
language: python filename: bt_car.py line_numbers: true line_number_start: 17
line_highlights:
---

def zurueck():    
motor_links.start(-50)     
motor_rechts.start(50)


--- /code ---

--- /task ---

--- task ---

Um den Roboter nach links zu drehen, müssen sich beide Motoren in die gleiche Richtung drehen.

--- code ---
---
language: python filename: bt_car.py line_numbers: true line_number_start: 22
line_highlights:
---

def links(): motor_links.start(50) motor_rechts.start(50)


def rechts(): motor_links.start(-50) motor_rechts.start(-50)


--- /code ---

--- /task ---

--- task ---

Um deinen Code zu testen, kannst du deine `for` Schleife bearbeiten.

--- code ---
---
language: python filename: bt_car.py line_numbers: true line_number_start: 32
line_highlights:
---

for i in range(2):    
vorwaerts()     
sleep(1)     
zurueck()     
sleep(1)     
rechts()     
sleep(1)     
links()      
sleep(1)      
stop()

--- /code ---

--- /task ---

--- task ---

Führe deinen Code aus und überprüfe, ob sich die Räder richtig drehen.

--- /task ---

--- save ---
