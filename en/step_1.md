## Introduction

Use LEGO and the Raspberry Pi Build HAT to build a robot car, then program it so you can control it with a Bluetooth connection from your Android phone. Then add some LEDs to dazzle your friends.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">The name [Bluetooth](https://en.wikipedia.org/wiki/Bluetooth)</span> was proposed in 1997 by Jim Kardach of Intel. At the time of this proposal, he was reading Frans G. Bengtsson's historical novel *The Long Ships* about Vikings and the 10th-century Danish king Harald Bluetooth. Bluetooth was King Harald's nickname, and he united the Danish tribes into a single kingdom, just as Bluetooth unites communication protocols.
</p>

You will:
+ Learn to control LEGO motors using the Raspberry Pi Build HAT
+ Learn to use Bluetooth to send signals to the Raspberry Pi
+ Learn how to control LEDs using gpiozero on the Raspberry Pi

--- no-print ---

![A photo of the finished LEGO wheeled bot with the Raspberry Pi and Build HAT centrally mounted. There is a breadboard with wires attached to LEDs on top of the stack.](images/lego-bot.gif)

--- /no-print ---

You will be building a wheeled car. Its movement will be determined by two separately driven wheels placed on either side of the car, allowing it to move forwards, backwards, and turn. You can optionally add LEDs to the car to act as brake lights, indicators, or headlights.

--- print-only ---

![Complete project.](images/buggy.JPG)

--- /print-only ---

### You will need

+ A Raspberry Pi computer running the latest Desktop version of Raspberry Pi OS
+ A Raspberry Pi Build HAT
+ 2 Lego Spike motors
+ An assortment of LEGO, including two wheels (we used a selection from the [LEGO Spike Prime kit](https://education.lego.com/en-gb/product/spike-prime))
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
