# raspi_garage_alert
Generate an alert when your garage door is left open

I was inspired by the work done by this guy: https://github.com/rllynch/pi_garage_alert, but I wanted to make pretty drastic changes and I thought it would be rude to so radically change someone's code in a fork.

The exact magnetic sensor he used was unavailable, so I bought a similar model, SM-226L-3Q. (https://www.amazon.com/gp/product/B005H3GCW0).

On that model, if you connect it with the red wire, it goes high (1) if the garage is closed and low (0) if open.

As of v0.3.0 it now works with MQTT and is useful for using with Home Assistant:

![mqtt animated gif](https://raw.githubusercontent.com/djotaku/raspi_garage_alert/master/screenshots/mqtt.gif)

You should have the following config files in $HOME/.config/raspigaragealert/: mqtt.conf and matrix.conf

*mqtt.conf*
```json
{
"channel":"something/somethingelse",
"server":"mqtt server url or ip address",
"client_id":"client_if for raspberry pi"
}
```

*matrix.conf*
```json
{
"server":"url or IP address of server",
"room":"room ID will look like !randomletters:server.com"
"username":"name of user for posting",
"password":"password for that user"
}
```
