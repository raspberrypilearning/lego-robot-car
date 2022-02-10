## 设置乐高（LEGO®）Spike™ 马达

在构建机器人之前就开始开发和测试程序会更容易。 这可以降低破坏您完美的模型的风险，比如当马达意外将机器人送至错误的方向，导致它从您的办公桌上滑落（当然，使用乐高（LEGO®）的好处是您可以随时重建它）。

Raspberry Pi Build HAT 及配套的 Python 库允许您直接用Raspberry Pi 控制乐高（LEGO®）Technic™ 马达。

将两个马达分别插入 Raspberry Pi Build HAT 上的端口 A 和 B。 将您的电池组连接到 Build HAT 上的筒形插孔并开启电源。

### 让马达转起来

--- task ---

从Raspberry Pi 上的Programming 菜单中启动 **Thonny**。

--- /task ---

--- task ---

使用以下代码让两个马达以最大速度的 50% 的速率旋转10 秒。 （他们将逐个运行，而不是一起运行。）

--- code ---
---
language: python
filename: bt_car.py
line_numbers: true
line_number_start: 
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

运行程序并检查马达的转动。

--- /task ---

因为马达将安装在汽车底盘的两侧，您当前的程序应该以相反的方向转动马达。 因此，逆时针旋转左轮将使机器人向前移动，右轮则需要顺时针旋转。

现在您已经测试了马达，您可以创建函数来使马达停止和向前驱动。

--- task ---

去掉那两行让马达运行10秒的代码，加上这两个函数。 乐高（LEGO®）马达的`start()` 函数和`run` 函数的工作方式不同，所以这次两个马达将一起运行。

--- code ---
---
language: python
filename: bt_car.py
line_numbers: true
line_number_start: 
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

添加以下 ”开始-暂停-开始-暂停“ 序列来测试您的函数：

--- code ---
---
language: python
filename: bt_car.py
line_numbers: true
line_number_start: 17
line_highlights: 
---

for i in range(2):    
  forward()    
  sleep(1)    
  stop()    
  sleep(1)  

--- /code ---
--- /task ---


如果成功了，再添加三个函数来分别实现向后、向左和向右移动机器人。

--- task ---

要向后移动机器人，只需反转两个马达的旋转方向即可。

--- code ---
---
language: python
filename: bt_car.py
line_numbers: true
line_number_start: 17
line_highlights: 
---

def back():    
  motor_left.start(-50)     
  motor_right.start(50)


--- /code ---

--- /task ---

--- task ---

要将机器人向左转动，两个马达需要向同一方向转动。

--- code ---
---
language: python
filename: bt_car.py
line_numbers: true
line_number_start: 22
line_highlights: 
---

def left():
  motor_left.start(50)
  motor_right.start(50)


def right():
  motor_left.start(-50)
  motor_right.start(-50)


--- /code ---

--- /task ---

--- task ---

您可以编辑 `for` 循环来测试您的代码。

--- code ---
---
language: python
filename: bt_car.py
line_numbers: true
line_number_start: 32
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

运行您的代码，检查轮子是否正确转动。

--- /task ---

--- save ---
