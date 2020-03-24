## Bluetooth control

To remotely pilot your robot, you're going to use the Blue Dot library.
This will let you control the robot from an Android phone or tablet.

### Pairing your Raspberry Pi with your Android device

Later on, you will need to login to your Raspberry Pi to enable the pairing via the command line. Therefore it makes sense to use that method rather than using the Desktop.

On your Raspberry Pi:

Open a Terminal window.

Type `bluetoothctl` and press Enter to open Bluetooth control

At the [bluetooth]# prompt enter the following commands:

discoverable on
pairable on
default-agent

Depending on the version of Android you are running, the steps to follow on your device may vary slightly but should be close to:

Open Settings
Select Connected Devices

![andriod1](images/android1.png)

Turn Bluetooth on and select the Bluetooth menu
Select Pair new device

![andriod1](images/android2.png)

Your Raspberry Pi will appear in the list; select it
Enter a PIN
![andriod1](images/android3.png)


On your Raspberry Pi:

Enter the same PIN
Type quit and press Enter to return to the command line

### Testing Bluedot

Now test that Blue Dot.

Create a new Python file on your Raspberry Pi called bluedot_test.py:

```python
from bluedot import BlueDot
bd = BlueDot()
print('Waiting...')
bd.wait_for_press()
print("It worked!")
```
Run this program and then grab your Android phone or tablet and  open the app on that device. The first screen will show you a list of something????

Click on the Raspberry Pi entry.

You should then see a big blue dot on your screen. Tap the dot.

Back on the Raspberry Pi you should see that your program has accepted the Bluetooth connection and successfully responded to you pressing the blue dot.  

![thonny1](images/thonny1.png)

### More than just a blue dot

The Blue Dot app is more than just a simnple button. The Blue Dot can also be used as a joystick when the middle, top, bottom, left or right areas of the dot are touched.

You can change the robot to use variable speeds, so the further towards the edge you press the Blue Dot, the faster the robot will go.

The distance attribute returns how far from the centre the Blue Dot was pressed, which can be passed to the robot’s functions to change its speed:
