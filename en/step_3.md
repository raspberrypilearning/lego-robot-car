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

![andriod1](images/android1.JPG)

Turn Bluetooth on and select the Bluetooth menu
Select Pair new device

![andriod1](images/android2.JPG)

Your Raspberry Pi will appear in the list; select it
Enter a PIN
![andriod1](images/android3.JPG)


On your Raspberry Pi:

Enter the same PIN
Type quit and press Enter to return to the command line

### Testing Bluetooth
