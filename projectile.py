import math
from tkinter import YView

class projectileMotion():

    # Prereq
    def xVelocityC(velocity, angle):
        xVelocity = velocity*(math.cos(math.radians(angle)))
        return xVelocity

    def yVelocityC(velocity, angle):
        yVelocity = velocity*(math.sin(math.radians(angle)))
        return yVelocity

    def fTime(angle, velocity, accelorationY, hight):
        yVelocity = projectileMotion.yVelocityC(velocity, angle)
        if(hight == 0 or hight > 0):
            time = (-1*(yVelocity) - math.sqrt(pow(yVelocity, 2) + -4*hight*(0.5*(accelorationY))))/accelorationY
        elif(hight < 0):
            time = (-1*(yVelocity) + math.sqrt(pow(yVelocity, 2) + -4*hight*(0.5*(accelorationY))))/accelorationY
        return time

    def solveQuadratic(angle, velocity, accelorationY, hight, time):
        outPut = hight + (velocity*time) + ((0.5*accelorationY)*pow(time, 2))
        return outPut

    # Actual
    def xMax(angle, velocity, accelorationY, hight):
        xVelocity = projectileMotion.xVelocityC(velocity, angle)
        hangTime = projectileMotion.fTime(angle, velocity, accelorationY, hight)
        return((xVelocity)*(hangTime))

    def yMax(angle, velocity, accelorationY, hight):
        yVelocity = projectileMotion.yVelocityC(velocity, angle)
        hangTime = projectileMotion.fTime(angle, velocity, accelorationY, 0)
        yMax = projectileMotion.solveQuadratic(angle, yVelocity, accelorationY, hight, (hangTime/2))
        return yMax

    def xAtTime(angle, velocity, accelorationY, hight, time):
        xVelocity = projectileMotion.xVelocityC(velocity, angle)
        hangTime = projectileMotion.fTime(angle, velocity, accelorationY, hight)
        if(time <= hangTime):
            xAtT = time*xVelocity
        elif(time > hangTime):
            xAtT = hangTime*xVelocity
        return xAtT

    def yAtTime(angle, velocity, accelorationY, hight, time):
        yVelocity = projectileMotion.yVelocityC(velocity, angle)
        hangTime = projectileMotion.fTime(angle, velocity, accelorationY, hight)
        if (time <= hangTime):
            yAtT = projectileMotion.solveQuadratic(angle, yVelocity, accelorationY, hight, time)
        elif (time > hangTime):
            yAtT = projectileMotion.solveQuadratic(angle, velocity, accelorationY, hight, hangTime)
        return yAtT
        


print(projectileMotion.yAtTime(20, 40, -9.8, 30, 2))

# yVelocity = 13.68080573
# accelorationY = -9.8
# hight = 0

# print(-1*(yVelocity))
# print(math.sqrt(pow(yVelocity, 2)))
# print(-4*hight*(0.5*(accelorationY)))

# print(-1*(yVelocity) - math.sqrt(pow(yVelocity, 2)))
# print(-1*(yVelocity) - math.sqrt(pow(yVelocity, 2) + -4*hight*(0.5*(accelorationY))))

# print((-1*(yVelocity) - math.sqrt(pow(yVelocity, 2) + -4*hight*(0.5*(accelorationY))))/accelorationY)


