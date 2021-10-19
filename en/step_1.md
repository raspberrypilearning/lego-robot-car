## Introduction

Use LEGO® and the Raspberry Pi Build HAT to build a robot car, then program it so you can control it with a Bluetooth connection from your Android phone. Then add some LEDs to dazzle your friends.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">The name [Bluetooth](https://en.wikipedia.org/wiki/Bluetooth)</span> was proposed in 1997 by Jim Kardach of Intel. At the time of this proposal, he was reading Frans G. Bengtsson's historical novel *The Long Ships* about Vikings and the 10th-century Danish king Harald Bluetooth. Bluetooth was King Harald's nickname, and he united the Danish tribes into a single kingdom, just as Bluetooth unites communication protocols.
</p>

You will:
+ Control LEGO® Technic™ motors using the Raspberry Pi Build HAT
+ Use Bluetooth to send signals to the Raspberry Pi
+ Learn how to control LEDs using gpiozero on the Raspberry Pi

--- no-print ---

![A photo of the finished LEGO® wheeled bot with the Raspberry Pi and Build HAT centrally mounted. There is a breadboard with wires attached to LEDs on top of the stack.](images/lego-bot.gif)

--- /no-print ---

You will build a wheeled car. Its movement will be determined by two separately driven wheels placed on either side of the car, allowing it to move forwards, backwards, and turn. You can optionally add LEDs to the car to act as brake lights, indicators, or headlights.

--- print-only ---

![Complete project.](images/buggy.JPG)

--- /print-only ---

### You will need

+ A Raspberry Pi computer running the latest Desktop version of Raspberry Pi OS
+ A Raspberry Pi Build HAT
+ 2× LEGO® Technic™ motors
+ An assortment of LEGO®, including two wheels (we used a selection from the [LEGO® Education SPIKE™ Prime kit](https://education.lego.com/en-gb/product/spike-prime))
+ An Android mobile phone or tablet
+ 5× AA batteries and a holder pack with a barrel jack 

### Software

+ Build HAT Python library to control the Build HAT
+ Blue Dot Python library and Blue Dot Android app
+ gpiozero Python library


--- collapse ---
---
title: Additional information for educators
---

You can download the complete project [here](https://rpf.io/p/en/bt-robot-car-go).

If you need to print this project, please use the [printer-friendly version](https://projects.raspberrypi.org/en/projects/bt-robot-car/print){:target="_blank"}.

--- /collapse ---

Before you begin, you'll need to have set up your Raspberry Pi computer and attached your Build HAT:

--- task ---

Mount your Raspberry Pi on to the LEGO Build Plate using M2 bolts and nuts, making sure the Raspberry Pi is on the side without the 'edge':

 ![Raspberry Pi bolted to a magenta LEGO Build Plate.](images/build_11.jpg)

--- /task ---

Mounting the Raspberry Pi this way round enables easy access to the ports as well as the SD card slot. The Build Plate will allow you to connect the Raspberry Pi to the main structure of your dashboard more easily.

--- task ---

Line up the Build HAT with the Raspberry Pi, ensuring you can see the `This way up` label. Make sure all the GPIO pins are covered by the HAT, and press down firmly. (The example uses a [stacking header](https://www.adafruit.com/product/2223){:target="_blank"}, which makes the pins longer.)

![Image of GPIO pins poking through the top of the Build HAT.](images/build_15.jpg)
![Animation showing Buildhat fitting to Raspberry Pi](images/haton.gif)

--- /task ---

You should now power your Raspberry Pi using the 7.5V barrel jack on the Build HAT, which will allow you to use the motors.

--- task ---

If you have not already done so, set up your Raspberry Pi by following these instructions:

[Setting up your Raspberry Pi](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up){:target="_blank"}

--- /task ---

--- task ---

Once the Raspberry Pi has booted, open the Raspberry Pi Configuration tool by clicking on the Raspberry Menu button and then selecting “Preferences” and then “Raspberry Pi Configuration”.

Click on the “interfaces” tab and adjust the Serial settings as shown below:

![Image showing Raspberry Pi OS config screen with serial port enabled and serial console disabled](images/configshot.jpg)

--- /task ---

--- task ---
You will also need to install the buildhat python library by following these instructions: 

--- collapse ---
---
title: Install the buildhat Python library
---

Open a terminal window on your Raspberry Pi by pressing <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>.

At the prompt type: `sudo pip3 install buildhat`

Press <kbd>Enter</kbd> and wait for the "installation completed" message.

--- /collapse ---

--- /task ---