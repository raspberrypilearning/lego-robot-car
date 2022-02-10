## 用Blue Dot控制您的马达

Blue Dot 应用程序和 Python 库可用于从您的设备控制您的乐高（LEGO®）Technic™ 马达。

--- task ---

再次打开 `bt_car.py` 文件，并在文件顶部设置Blue Dot。 您还应该将导入 `sleep` 语句替换为 `from signal import pause`。

--- code ---
---
language: python filename: bt_car.py line_numbers: true line_number_start: 1
line_highlights: 2,3,7
---

from buildhat import Motor    
from bluedot import BlueDot from signal import pause

motor_left = Motor('A')     
motor_right = Motor('B')     
dot = BlueDot()

--- /code ---

--- /task ---

--- task ---

从当前代码中删除 `for` 循环，完整代码如下所示：

--- code ---
---
language: python filename: bt_car.py line_numbers: true line_number_start: 1
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

现在在您的程序底部添加一个使用 Blue Dot **调用** `forward` 函数的函数。

--- code ---
---
language: python filename: bt_car.py line_numbers: true line_number_start: 34
line_highlights:
---

def move(pos):     
if pos.top:     
forward()

--- /code ---

--- /task ---

`move` 函数有一个参数，称为 `pos`。 这个参数依据Blue Dot被触摸的位置而设置并自动传递给函数。

--- task ---

在您代码底部添加两个调用。 这将用于控制汽车前进和停止。 最后的调用确保程序不只是在脚本的底部结束。

--- code ---
---
language: python filename: bt_car.py line_numbers: true line_number_start: 39
line_highlights:
---

dot.when_pressed = move    
dot.when_released = stop   
pause()

--- /code ---

--- /task ---

--- task ---

运行您的代码。 按下设备上的Blue Dot应用程序顶部附近的蓝点，马达应该会转动。 当您将手指从蓝点上移开时，马达应该会停止运行。

--- /task ---

目前，马达只会使向前驱动车轮。 通过使用 `pos` 参数，您可以使它们向各个方向转动。

--- task ---

添加到 `move` 函数中，以便马达可以向后、向左和向右移动汽车。

--- code ---
---
language: python filename: bt_car.py line_numbers: true line_number_start: 32
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

再次运行您的代码，并使用 Blue Dot 应用程序对其进行测试。 现在按下蓝点的右侧、左侧和底部应该可以向不同的方向移动马达。

--- /task ---

您可以在代码中添加一行，使得 Blue Dot 不仅响应按下的操作，还可以响应您的手指在蓝点上的移动。

--- task ---

添加这行代码，就可以使马达响应蓝点上的移动。

--- code ---
---
language: python filename: line_numbers: true line_number_start: 43
line_highlights: 47
---


dot.when_pressed = move    
dot.when_released = stop    
dot.when_moved = move

--- /code ---

--- /task ---

--- task ---

运行您的程序并尝试按下 Android 设备上的蓝点，然后将手指移动到蓝点上的不同位置。 马达应该开始向不同方向转动，并在您将手指从蓝点上移开时停止。

--- /task ---

要阅读 BlueDot 的完整文档， [点击此处](https://bluedot.readthedocs.io/en/latest/)。

--- save ---
