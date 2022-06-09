import math
from tkinter import Y

class projectileMotion():
    def fTime(angle, velocity, accelorationY, hight):
        yVelocity = velocity*(math.sin(math.radians(angle)))
        if(hight == 0 or hight > 0):
            time = (-1*(yVelocity) - math.sqrt(pow(yVelocity, 2) + -4*hight*(0.5*(accelorationY))))/accelorationY
        elif(hight < 0):
            time = (-1*(yVelocity) + math.sqrt(pow(yVelocity, 2) + -4*hight*(0.5*(accelorationY))))/accelorationY
        return time
    # Angle, Velocity, Gravitational Acceloration, Initial Hight
    def xMax(angle, velocity, accelorationY, hight):
        xVelocity = velocity*(math.cos(math.radians(angle)))
        hangTime = projectileMotion.fTime(angle, velocity, accelorationY, hight)
        return((xVelocity)*(hangTime))
    def yMax(angle, velocity, accelorationY, hight):
        hangTime = projectileMotion.fTime(angle, velocity, accelorationY, 0)

print(projectileMotion.xMax(20, 40, -9.8, 0))

# yVelocity = 13.68080573
# accelorationY = -9.8
# hight = 0

# print(-1*(yVelocity))
# print(math.sqrt(pow(yVelocity, 2)))
# print(-4*hight*(0.5*(accelorationY)))

# print(-1*(yVelocity) - math.sqrt(pow(yVelocity, 2)))
# print(-1*(yVelocity) - math.sqrt(pow(yVelocity, 2) + -4*hight*(0.5*(accelorationY))))

# print((-1*(yVelocity) - math.sqrt(pow(yVelocity, 2) + -4*hight*(0.5*(accelorationY))))/accelorationY)


