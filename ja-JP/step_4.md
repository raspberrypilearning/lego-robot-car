## Blue Dotでモーターを制御する

Blue Dot アプリと Python ライブラリを使用すると、デバイスから LEGO® Technic™ モーターを制御することができます。

--- task ---

`bt_car.py` ファイルを再度開いて、ファイルの先頭に Blue Dot を設定します。 また、 `sleep` のインポートを `from signal import pause` に入れ替える必要もあります。

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

現在のコードから `for` ループを削除して、コード全体が次のとおりになるようにします。

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

次に、Blue Dotを使って `forward` 関数を**コール**するための関数を、スクリプトの最後に追加します。

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

`move` 関数には `pos` というパラメーターがひとつあります。 これは、青いドットがタッチされた場所を関数に自動的に渡します。

--- task ---

コードの最後に2つのメソッドの呼び出しを追加します。 これで車は前進と停止ができるようになります。 最後の呼び出しは、プログラムがスクリプトの最後で終了しないようにします。

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

コードを実行しましょう。 デバイスの Blue Dot アプリで、青いドットの上のほうを押すと、モーターが回転します。 青いドットから指を離すと、モーターは停止します。

--- /task ---

いまの状態では、モーターは前の方向にだけ車輪を回転させます。 `pos` パラメータを使用することで、すべての方向に回転させられるようになります。

--- task ---

`move` 関数に追加して、モーターが車を後ろや左右に動けるようにします。

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

コードをもう一度実行して、 Blue Dot アプリでテストしましょう。 青いドットの右、左、下を押すと、モーターがいろいろな方向に移動します。

--- /task ---

コードに1行を追加することで、 Blue Dot が押した時だけでなく、指が青いドットの上を移動したときにも応答するようにできます。

--- task ---

青いドットの上の動きにモーターが反応できるように、次の1行を追加します。

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

プログラムを実行して、 Android デバイス上の青いドットを押し、指をいろいろな場所に動かしてみてください。 モーターは色々な方向に回転し、青いドットから指を離すと停止します。

--- /task ---

BlueDot のドキュメントを読むには、[ここをクリックしてください](https://bluedot.readthedocs.io/ja-JP/latest/)。

--- save ---
