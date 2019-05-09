import sys
import serial.tools.list_ports
import string
from pyfirmata import Arduino, util

class arduinoHandler:
    def __init__(self):
        port = self.__getPort()
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

    # This function is used for writing to digital pins
    def digitalWrite(self, port : int, value : bool):
        self.__board.digital[port].write(value)

    # This function is used for writing to analog pins
    def analogWrite(self, port : string, value : int):
        analog = self.__board.get_pin(port)
        analog.write(value)