==============
Hardware Setup
==============

You need to buy a 2-wire magnetic sensor. (Technically, the one I am using has 3 wires, but you only use two of them). I am using the Seco-Larm Overheard Door Mount SM-226L-3Q. You can buy it on `Amazon https://www.amazon.com/gp/product/B005H3GCW0`_. If you use the red wire on that model, it goes high if your garage door is closed and low if it is open. Use the other color if you want to have the opposite situation. You put the red (or other color) on an GPIO wire (and not one that is used for SCL or something like that). Black goes to a ground pin. Depending on your Raspberry Pi model, the Raspberry Pi documentation can help you with figuring out the pin number. Make a note of the pin number you have the red wire connected to. You want the main number, not the GPIO number.

Depending on your garage setup and what version of Raspberry Pi you are using, you may need to buy a wireless dongle. When I was running this program on a Raspberry Pi 1B, I needed the dongle. Right now I'm using the Raspberry Pi Zero W and that one has wireless built in. I believe the second gen Raspberry Pi 3B has WiFi built in, as does the Raspberry Pi 4. Of course, for the non-Zero Raspberry Pis, if you have an ethernet cable in your garage, you can use it there.

You may also want a way to mount the Raspberry Pi to the wall. I find that Scotch Reclosable Fasteners (basically velcro with an adhesive back on each side) works well. For me it held through a pretty humid summer and a usual winter. 

You will definitely want an enclosure for your Raspberry Pi. `Adafruit https://www.adafruit.com`_ has a nice selection for each model. 
