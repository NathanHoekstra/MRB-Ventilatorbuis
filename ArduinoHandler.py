import sys
import serial.tools.list_ports
import string
from pyfirmata import Arduino, util
import time

class ArduinoHandler:
    def __init__(self, pin : int):
        port = self.__getPort()
        self.__pin = pin
        self.__analogPort = None
        if port is None:
            print("No Arduino found!")
            sys.exit(1)
        else:
            self.__board = Arduino(port)
            print("Board initialized!")

    # Get all com ports from OS and find the Arduino port
    # Note: the function serial.tools.list_ports.comports() is wicked slow
    # Maybe there is a different function that we can use
    @staticmethod
    def __getPort():
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            if 'Arduino' in p.description:
                return p.device
            # Fake Arduino Uno/Nano serial port (MacOS)
            elif '/dev/cu.wchusbserial' in p.device:
                return p.device

    # This function is used for writing to digital pins
    def digitalWrite(self, value : bool):
        self.__board.digital[self.__pin].write(value)

    # Set analogport to be used
    def setAnalogPort(self, port : string):
        self.__analogPort = self.__board.get_pin(port)

    # This function is used for writing to analog pins
    def analogWrite(self, value : float):
        self.__analogPort.write(value)

    def delayMicroseconds(self, value : float):
        time.sleep(value / 1000)