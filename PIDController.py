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


    def __init__(self, Kp : int, Ki : int, Kd : int, pwmPin : int, arduino : ArduinoHandler):
        self.__arduino = arduino
        self.__controlErrorUpper = 1000
        self.__controlErrorLower = -self.__controlErrorUpper
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

    def __setBallPosition(self, ballPosition):
        if ballPosition is not None:
            self.__ballPosition = ballPosition[1]

    def __setSetpoint(self, setPoint):
        if setPoint is not None:
            self.__setPoint = setPoint[1]

    def __setFrameRate(self, frameRate):
        self.__Dt = 1  / frameRate

    def __pwmOutput(self):
        self.__getError()
        self.__sumError()
        error = (self.__calculateKp() + self.__calculateKd() + self.__calculateKi())
        if error > self.__controlErrorUpper:
            error = self.__controlErrorUpper
        elif error < self.__controlErrorLower:
            error = self.__controlErrorLower

        commandSignal = round(error * -(1 / 1000) + 0.65, 3)
        if commandSignal > 1:
            commandSignal = 1
        if commandSignal < 0:
            commandSignal = 0
        return commandSignal

    def controlPIDFan(self, ballPosition, objectPosition, framerate):
        self.__setBallPosition(ballPosition)
        self.__setSetpoint(objectPosition)
        self.__setFrameRate(framerate)
        self.__arduino.analogWrite(self.__pwmOutput())
