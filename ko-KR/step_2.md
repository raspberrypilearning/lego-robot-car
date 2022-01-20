## LEGO® Spike™ 모터설정

로봇을 만들기 전에 프로그램을 테스트하고 개발하는 것이 더 좋습니다. 이렇게 하면 모터가 예기치 않게 로봇을 잘못된 방향으로 보내 책상 아래로 떨어져, 멋진 모델을 망칠 위험이 줄어듭니다(물론 LEGO® 사용의 좋은 점은 부서지더라도 언제든지 다시 조립할 수 있다는 점입니다).

Raspberry Pi Build HAT 그리고 Python 라이브러리를 사용하면 Raspberry Pi 컴퓨터에서 직접 LEGO® Technic™ 모터를 제어할 수 있습니다.

두 개의 모터를 Raspberry Pi Build HAT의 포트 A와 B에 연결하세요. 배터리팩을 Build HAT의 배럴 잭에 연결하고 켭니다.

### 모터 회전시키기

--- task ---

**프로그래밍** 메뉴에서 Raspberry Pi의 Thonny를 엽니다.

--- /task ---

--- task ---

다음 코드를 사용하여 10초 동안 최대 속도의 50%로 두 모터를 모두 회전시키도록 하세요. (함께가 아니라 한 번에 하나씩 실행되게 됩니다.)

--- code ---
---
language: python filename: bt_car.py line_numbers: true line_number_start:
line_highlights:
---

from buildhat import Motor   
from time import sleep

motor_left = Motor('A')   
motor_right = Motor('B')   
motor_left.run_for_seconds(seconds=10, speed=50)   
motor_right.run_for_seconds(seconds=10, speed=-50)

--- /code ---

--- /task ---

--- task ---

프로그램을 실행하고 모터 회전을 확인하세요.

--- /task ---

모터는 자동차 섀시의 반대쪽에 장착되므로 현재 프로그램은 모터를 반대 방향으로 움직이도록 구현해야 합니다. 따라서 왼쪽 바퀴에서 시계 반대 방향으로 회전하면 로봇이 앞으로 이동하는 반면, 오른쪽에서는 시계 방향으로 회전하도록 해야 합니다.

이제 모터를 테스트했으므로 모터를 정지하고 앞으로 이동하는 기능을 만들 수 있습니다.

--- task ---

모터가 10초 동안 작동하도록 하는 두 줄의 코드를 제거하고 이 두 함수를 추가하세요. LEGO 모터에서 `start()` 함수는 `run` 함수와 다르게 작동하므로 이번에는 함께 실행됩니다.

--- code ---
---
language: python filename: bt_car.py line_numbers: true line_number_start:
line_highlights: 7-14
---

from buildhat import Motor   
from time import sleep

motor_left = Motor('A')    
motor_right = Motor('B')

def stop():    
motor_left.stop()    
motor_right.stop()


def forward():     
motor_left.start(50)     
motor_right.start(-50)


--- /code ---

--- /task ---

--- task ---

다음 시작-중지-시작-중지 기능을 추가하여 테스트합니다.

--- code ---
---
language: python filename: bt_car.py line_numbers: true line_number_start: 17
line_highlights:
---

for i in range(2):    
forward()    
sleep(1)    
stop()    
sleep(1)

--- /code --- --- /task ---


이 기능이 잘 작동하면 세 가지 기능을 추가하여 로봇을 전후좌우로 이동합니다.

--- task ---

로봇을 뒤로 움직이려면 두 모터의 방향을 반대로 하면 되겠습니다.

--- code ---
---
language: python filename: bt_car.py line_numbers: true line_number_start: 17
line_highlights:
---

def back():    
motor_left.start(-50)     
motor_right.start(50)


--- /code ---

--- /task ---

--- task ---

로봇을 왼쪽으로 돌리려면 두 모터가 같은 방향으로 회전하도록 해야 합니다.

--- code ---
---
language: python filename: bt_car.py line_numbers: true line_number_start: 22
line_highlights:
---

def left(): motor_left.start(50) motor_right.start(50)


def right(): motor_left.start(-50) motor_right.start(-50)


--- /code ---

--- /task ---

--- task ---

코드를 테스트하기 위해서, `for` 반복을 편집할 수 있습니다.

--- code ---
---
language: python filename: bt_car.py line_numbers: true line_number_start: 32
line_highlights:
---

for i in range(2):    
forward()     
sleep(1)     
back()     
sleep(1)     
right()     
sleep(1)     
left()      
sleep(1)      
stop()

--- /code ---

--- /task ---

--- task ---

코드를 실행하고 바퀴가 올바르게 회전하는지 확인하세요.

--- /task ---

--- save ---
