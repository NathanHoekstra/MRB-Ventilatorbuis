from ArduinoHandler import ArduinoHandler

class PIDController:
    def __getError(self):
        return self.setPoint - self.ballPosition

    def __init__(self, Kp : int, Ki : int, Kd : int, pwmPin : int):
        #self.arduino = ArduinoHandler()
        self.ballPosition = None
        self.setPoint = 250
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.pwmPin = pwmPin

    def setBallPosition(self, ballPosition):
        self.ballPosition = ballPosition[1]
        print(self.__getError())

    def setSetpoint(self, setPoint):
        self.setPoint = setPoint[1]
