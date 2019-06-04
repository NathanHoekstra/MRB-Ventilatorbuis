import sys
import serial.tools.list_ports
import time

class ArduinoHandler:
    def __init__(self):
        self.__port = self.__getPort()
        self.__analogPort = None
        if self.__port is None:
            print("No Arduino found!")
            sys.exit(1)
        else:
            self.__serial = serial.Serial(self.__port, 119200, timeout=.1)
            # Give the board time to reset, 4 seconds should be enough
            time.sleep(4)
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
        if value:
            self.__serial.write('1'.encode())
        else:
            self.__serial.write('0'.encode())

    def delayMicroseconds(self, value : float):
        time.sleep(value / 1000)