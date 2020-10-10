==============
Configuration
==============

You will need two configuration files. They should be in: $HOME/.config/raspigaragealert/ . If you run the program at least once, it will create that directory for you.

mqtt.conf
^^^^^^^^^

The channel is what your MQTT clients will subscribe to in order to get the messages. For example, I use 'garage/door1'. So if I had another garage door, I would have that send on 'garage/door2'. This would allow the client to subscribe to 'garage' to know about all doors. Or 'garage/door#' if it only cared about one or the other door. The server is the MQTT server you're connecting to. I run my own mosquitto server and it's extremely easy. But there are both free and paid ones available out there; just do some googling. The client ID isn't too important, except for debugging on your server. It can help you figure out which device is delivering the data to the server.

.. highlight:: json
   {
   "channel":"something/somethingelse",
   "server":"mqtt server url or ip address",
   "client_id":"client_if for raspberry pi"
   }

matrix.conf
^^^^^^^^^^^

You will probably want to create your own user for the raspigaragearlert, if you are allowed to do so on the server. Your room ID will not be the pretty name that you type into your Matrix client. It will look like !asdflkhasl;fhasl;jhasldhf:server.com. To find it, on the Element web interface right-click on the room's name and then settings. Click on advanced and then you want the internal room ID.

.. highlight:: json
   {
   "server":"url or IP address of server",
   "room":"room ID will look like !randomletters:server.com"
   "username":"name of user for posting",
   "password":"password for that user"
   }


