import math
from tkinter import Y

class projectileMotion():

    # Prereq
    def xVelocity(velocity, angle):
        xVelocity = velocity*(math.cos(math.radians(angle)))
        return xVelocity

    def yVelocity(velocity, angle):
        yVelocity = velocity*(math.sin(math.radians(angle)))
        return yVelocity

    def fTime(angle, velocity, accelorationY, hight):
        yVelocity = yVelocity(velocity, angle)
        if(hight == 0 or hight > 0):
            time = (-1*(yVelocity) - math.sqrt(pow(yVelocity, 2) + -4*hight*(0.5*(accelorationY))))/accelorationY
        elif(hight < 0):
            time = (-1*(yVelocity) + math.sqrt(pow(yVelocity, 2) + -4*hight*(0.5*(accelorationY))))/accelorationY
        return time

    # Actual
    def xMax(angle, velocity, accelorationY, hight):
        xVelocity = xVelocity(velocity, angle)
        hangTime = projectileMotion.fTime(angle, velocity, accelorationY, hight)
        return((xVelocity)*(hangTime))

    def yMax(angle, velocity, accelorationY, hight):
        yVelocity = yVelocity(velocity, angle)
        hangTime = projectileMotion.fTime(angle, velocity, accelorationY, 0)
        yMax = hight + (yVelocity*hangTime) + (0.5*9.8*pow(hangTime, 2))
        return yMax

print(projectileMotion.yMax(20, 40, -9.8, 30))

# yVelocity = 13.68080573
# accelorationY = -9.8
# hight = 0

# print(-1*(yVelocity))
# print(math.sqrt(pow(yVelocity, 2)))
# print(-4*hight*(0.5*(accelorationY)))

# print(-1*(yVelocity) - math.sqrt(pow(yVelocity, 2)))
# print(-1*(yVelocity) - math.sqrt(pow(yVelocity, 2) + -4*hight*(0.5*(accelorationY))))

# print((-1*(yVelocity) - math.sqrt(pow(yVelocity, 2) + -4*hight*(0.5*(accelorationY))))/accelorationY)


