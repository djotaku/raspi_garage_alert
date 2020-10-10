.. raspigaragealert documentation master file, created by
   sphinx-quickstart on Sat Oct 10 22:12:50 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to raspigaragealert's documentation!
============================================

This is a program that is meant to run on a Raspberry Pi to alert you whether your garage door is open. Right now it works with MQTT and Matrix (basically an open source Slack). MQTT is literally an industrial standard for sending short status messages with very little overhead. I use it to pass the data to Home Assistant. But you can very easily code up an MQTT client with the paho-mqtt library and do whatever you want with the data.

You will want to either use a publicly available MQTT server or run your own. I run my own using the mosquitto Docker/Podman container. It works rather well. You can also use MQTT software for debugging. I use MQTT Explorer.

Right now my code expects you to both use MQTT and Matrix. I will eventually add some flags to allow you to turn that off and on.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   hardware
   configuration



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
