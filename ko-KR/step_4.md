## Blue Dot으로 모터 제어하기

Blue Dot 앱과 Python 라이브러리를 사용하여 스마트폰에서 LEGO® Technic™ 모터를 제어할 수 있습니다.

--- task ---

`bt_car.py` 파일을 다시 열고 파일 상단에 Blue Dot을 설정합니다. `sleep` import 를 </code>from signal import pause` 로 바꿔야 합니다.</p>

--- code ---
---
language: python
filename: bt_car.py
line_numbers: true
line_number_start: 1
line_highlights: 2,3,7
---

from buildhat import Motor
from bluedot import BlueDot
from signal import pause

motor_left = Motor('A')
motor_right = Motor('B')
dot = BlueDot() 

--- /code ---

--- /task ---

--- task ---

전체 코드가 다음과 같이 보이도록 현재 코드에서 `for` 루프를 제거하도록 합니다.

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

motor_left = Motor('A')     
motor_right = Motor('B')     
dot = BlueDot()


def stop():     
    motor_left.stop()     
    motor_right.stop()


def forward():     
    motor_left.start(-100)     
    motor_right.start(100)


def backward():     
    motor_left.start(100)     
    motor_right.start(-100)


def right():     
    motor_left.start(-100)     
    motor_right.start(-100)


def left():     
    motor_left.start(100)     
    motor_right.start(100)     
--- /code ---

--- /task ---

--- task ---

이제 Blue Dot이 `forward` 함수를 **호출** 하도 스크립트 맨 아래에 코드를 추가하세요.

--- code ---
---
language: python 
filename: bt_car.py 
line_numbers: true 
line_number_start: 34
line_highlights:
---

def move(pos):     
    if pos.top:     
        forward()

--- /code ---

--- /task ---

`move` 함수에는 `pos`이라고 하는 1개의 매개변수가 있습니다. Blue Dot을 터치한 위치에 따라 함수에 자동으로 전달되게 됩니다.

--- task ---

코드 맨 아래에 두 개의 메서드 호출을 추가합니다. 이것들은 차가 앞으로 움직이고 멈추도록 할 것입니다. 마지막 호출은 프로그램이 스크립트 맨 아래에서 끝나지 않도록 합니다.

--- code ---
---
language: python 
filename: bt_car.py 
line_numbers: true 
line_number_start: 39
line_highlights:
---

dot.when_pressed = move    
dot.when_released = stop   
pause()

--- /code ---

--- /task ---

--- task ---

코드를 테스트해 보세요. 기기의 Blue Dot 앱에서 상단 근처의 파란색 점을 누르면 모터가 회전해야 합니다. 파란색 점에서 손가락을 떼면 모터가 정지해야 합니다.

--- /task ---

현재 모터는 바퀴를 앞으로만 돌립니다. `pos` 매개변수를 사용하여 모든 방향으로 회전하도록 할 수 있습니다.

--- task ---

모터가 자동차를 전후좌우로 움직이도록 `move` 함수에 아래 코드를 추가하십시오.

--- code ---
---
language: python 
filename: bt_car.py 
line_numbers: true 
line_number_start: 32
line_highlights: 37-42
---


def move(pos):    
    if pos.top:    
        forward()    
    elif pos.bottom:    
        backward()    
    elif pos.left:    
        left()     
    elif pos.right:    
        right()


--- /code ---

--- /task ---

--- task ---

코드를 다시 실행하고 Blue Dot 앱으로 테스트합니다. 파란색 점의 오른쪽, 왼쪽, 아래쪽을 누르면 이제 모터가 다른 방향으로 움직여야 합니다.

--- /task ---

코드에 한 줄을 더 추가하면 Blue Dot이 누르는 것뿐만 아니라 손가락이 파란색 점 위로 움직일 때에도 응답하도록 할 수 있습니다.

--- task ---

모터가 파란색 점 위의 움직임에 반응하도록 다음 코드를 추가합니다.

--- code ---
---
language: python 
filename: 
line_numbers: true 
line_number_start: 43
line_highlights: 47
---


dot.when_pressed = move    
dot.when_released = stop    
dot.when_moved = move

--- /code ---

--- /task ---

--- task ---

프로그램을 실행하고 Android 기기에서 파란색 점을 누르고 손가락을 다른 위치로 이동하여 실험해 봅니다. 모터는 다른 방향으로 회전해야 하며 파란색 점에서 손가락을 떼면 정지하도록 해야 합니다.

--- /task ---

BlueDot에 대한 전체 설명서를 읽으려면 [여기를 클릭하십시오](https://bluedot.readthedocs.io/ko-KR/latest/).

--- save ---
