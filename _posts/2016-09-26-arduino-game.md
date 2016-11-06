---
title: "Game with 8x8 LED matrix on Arduino"
date: 2016-09-26
layout: post
description: "A simple game I created on Arduino with 8x8 LED matrix on a single breadboard"
tags: [electronics]
comments: true
share: false
---

In this article I want to share a simple game I created on Arduino with 8x8 LED matrix created on a single breadboard. The main goal was to build a game console with all components located on a single breadboard.

![](/images/arduino-game/game-preview.gif)

## Components

1. Breadboard
2. Arduino UNO
3. 8x8 LED matrix
4. Driver MAX7219
5. 4 Buttons
6. Bunch of wires
7. four 470 Ohm resistors
8. one 10 kOhm resistor

## Software requirements

You need to have:

1. Arduino IDE
2. [LedControl library](http://playground.arduino.cc/Main/LedControl)
3. [Game's source code](https://github.com/itdxer/ArduinoGame)

## Connections

I won't explain it in details. I just will put a couple of photos that will show you how to set up the most important connections.

![](/images/arduino-game/console-front.jpg)

Arduino is on the backside of the breadboard.

![](/images/arduino-game/console-back.jpg)

Arduino is not attached to the back side of the breadboard. Wires are strained in this way just to simply hold Arduino in place.

![](/images/arduino-game/console-stretched.jpg)
![](/images/arduino-game/arduino-pins.jpg)

Four buttons are connected to the Analog Input PINs from A0 to A3.

* A0 - Connects to the button that shoots from the right side of the spaceship
* A1 - Connects to the button that shoots from the left side of the spaceship
* A2 - Connects to the button that moves spaceship to the left
* A3 - Connects to the button that moves spaceship to the right

Three wires are connected to PINs 10, 11 and 12.

* PING 12 - DATA IN-pin
* PING 11 - CLK-pin
* PING 10 - LOAD(/CS)-pin

![](/images/arduino-game/fire-buttons.jpg)
![](/images/arduino-game/movment-buttons.jpg)

The most messy part is the one that connects MAX7219 driver to LED matrix.

![](/images/arduino-game/led-and-driver.jpg)

The first matrix input goes into the hole near number 25 at the bottom of the photo.

![](/images/arduino-game/led-and-driver-encircled.jpg)

It's hard to understand something just by looking at this photo. In case if need some more information you can check this [Tutorial](http://tronixstuff.com/2013/10/11/tutorial-arduino-max7219-led-display-driver-ic/). It has a [scheme](http://tronixstuff.com/wp-content/uploads/2013/09/MAX7219_example_LED_matrix_circuit.jpg) that helps you connect these components.

## Useful resources

During the building process I found a few useful resources that helped me build this device.

1. [Tutorial](http://tronixstuff.com/2013/10/11/tutorial-arduino-max7219-led-display-driver-ic/) that helps connect MAX7219 driver and LED matrix
2. [Online tool](http://blog.riyas.org/2013/12/online-led-matrix-font-generator-with.html) that helps create binary images and save them as an array of hex/binary values.

## Source code

The main source code you can find at my [GitHub repository](https://github.com/itdxer/ArduinoGame). If you find a bug feel free to create an issue or pull request.
