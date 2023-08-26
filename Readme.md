# Device for monitoring parameter of potato store
___
### The device allows you to control the heater, cooler and humidifier by switching the relay on and off.
The device also displays the system status on the PC using the developed program in Python language

The device allows you to control the heater, cooler and humidifier by switching the relay on and off<br> 
The device also displays the system status on the PC using the developed program in Python language

Can be used in a small potato storage or modified for large areas
___
>Instead of creating a circuit with an Atmega328, you can use <u>Arduino</u>

**main.py** - for PC

**temp_hum.ino** - for circuit (for arduino and arduino.ide)
___
### Required Libraries
- To download the program to the circuit:<br> 
  - Library: DHT.h (library for temperature and humidity sensor DHT11, DHT21, DHT22)<br>

- Necessary for the operation of a computer program 
  - Library: tkinter, pyserial, pygame
___

```python
ser = serial.Serial(
    port='COM3', # <-- you need replace that
    baudrate=9600,
    timeout=10,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
```
### WARING
#### **In main.py on line 14, replace "COM3" with the port on which your device was identified in system**