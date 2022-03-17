## LEGO® Spike™ モーターをセットアップする

ロボットを構築する前に、プログラムのテストと開発をする方が簡単です。 そうすることで、モーターがロボットを想定外の方向に送り出して机の上を突進してしまった時に、素晴らしいモデルが台無しになるリスクが減ります(もちろん、 LEGO® を使用する利点はいつでも作り直せることです)。

Raspberry Pi Build HAT とその Python ライブラリを使用すると、Raspberry Pi コンピューターから直接 LEGO® Technic™ モーターを制御できます。

2つのモーターを Raspberry Pi Build HAT のポート A と B に接続します。 電池ケースを Build HAT のバレルジャックに接続して、電源を入れます。

### モーターを回転させる

--- task ---

Raspberry Pi で**プログラミング**メニューから Thonny を開きます。

--- /task ---

--- task ---

次のコードを使用して、両方のモーターを最大速度の50％で10秒間回転させます。 (一緒にではなく、1つずつ実行されます。)

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

プログラムを実行して、モーターが回転することを確認します。

--- /task ---

モーターは車のシャーシに反対向きで取り付けられるため、今回のプログラムではモーター同士を反対方向に動かす必要があります。 つまり、左側のホイールが反時計回りに回転するとロボットは前に移動しますが、一方で右側のホイールは時計回りに回転させる必要があります。

モーターのテストが完了したので、モーターの停止と前進をさせる関数が作成できるようになります。

--- task ---

モーターを10秒間動作させる2行のコードを削除して、次の2つの関数を追加します。 LEGO モーターの `start()` 関数は `run` 関数とは動作が異なり、モーターたちが同時に動きます。

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

次の start-stop-start-stop シーケンスを追加して、機能をテストしましょう。

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


うまく動いたら、ロボットを後ろ・左・右に移動する3つの関数を追加します。

--- task ---

ロボットを後ろに動かすには、両方のモーターの方向を逆にするだけです。

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

ロボットを左に回すには、両方のモーターを同じ方向に回す必要があります。

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

コードをテストするために `for` ループを編集してください。

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

コードを実行して、ホイールが正しく回転することを確認します。

--- /task ---

--- save ---
