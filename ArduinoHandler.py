import sys
import serial.tools.list_ports
import string
from pyfirmata import Arduino, util
import time

class ArduinoHandler:
    def __init__(self):
        ports = self.__getPorts()
        self.__analogPort = None
        print(ports)
        if ports is None or len(ports) < 2:
            print("Less then two Arduino's found!")
            sys.exit(1)
        else:
            self.__fanBoard = Arduino(ports[0])
            self.__speakerBoard = serial.Serial(ports[1], 9600, timeout=.1)
            print("Board initialized!")

    # Get all com ports from OS and find the Arduino port
    # Note: the function serial.tools.list_ports.comports() is wicked slow
    # Maybe there is a different function that we can use
    @staticmethod
    def __getPorts():
        arduinos = ["",""]
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            if 'Arduino' in p.description or 'CH340' in p.description:
                arduinos[0] = p.device
            # Fake Arduino Uno/Nano serial port (MacOS)
            elif '/dev/cu.wchusbserial' in p.device:
                arduinos[0] = p.device
            elif 'FT232R' in p.description:
                arduinos[1] = p.device
        return arduinos

    # This function is used for writing to digital pins
    def digitalWrite(self, pin : int, value : bool):
        self.__fanBoard.digital[pin].write(value)

    # Set analogport to be used
    def setAnalogPort(self, port : string):
        self.__analogPort = self.__fanBoard.get_pin(port)

    # This function is used for writing to analog pins
    def analogWrite(self, value : float):
        self.__analogPort.write(value)

    def frequencyWrite(self, frequency : int):
        self.__speakerBoard.write(str(frequency).encode())

    @staticmethod
    def delayMicroseconds(value : float):
        time.sleep(value / 1000)