from ArduinoHandler import ArduinoHandler

class PIDController:
    def __getError(self):
        self.__previousError = self.__currentError
        self.__currentError = self.__setPoint - self.__ballPosition

    def __calculateKi(self):
        return self.__errorSum * self.__Dt * self.__Ki

    def __calculateKd(self):
        return self.__Kd * ((self.__currentError - self.__previousError) / self.__Dt)

    def __calculateKp(self):
        return self.__Kp * self.__currentError

    def __sumError(self):
        self.__errorSum += self.__currentError


    def __init__(self, Kp : int, Ki : int, Kd : int, pwmPin : int):
        #self.arduino = ArduinoHandler()
        self.__errorSum = 1
        self.__previousError = 1
        self.__currentError = 1
        self.__ballPosition = 1
        self.__setPoint = 250
        self.__Kp = Kp
        self.__Ki = Ki
        self.__Kd = Kd
        self.__Dt = 0.05
        self.__pwmPin = pwmPin

    def setBallPosition(self, ballPosition):
        if ballPosition is not None:
            self.__ballPosition = ballPosition[1]

    def setSetpoint(self, setPoint):
        if setPoint is not None:
            self.__setPoint = setPoint[1]

    def setFrameRate(self, frameRate):
        self.__Dt = 1  / frameRate

    def pwmOutput(self):
        self.__getError()
        self.__sumError()
        return self.__calculateKp() + self.__calculateKd() + self.__calculateKi()
