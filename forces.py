import math

#Forces

class friction():
    def forceGravity(mass, gravity):
        return(mass * gravity)
    
    def forceNeautral(fGravity, slopeAngle):
        return(fGravity*math.cos(math.radians(slopeAngle)))

    def gravityAlongSlope(mass, gravity, sAngle):
        gravityAlongSlope = friction.forceGravity(mass, gravity) * math.sin(math.radians(sAngle))
        return (gravityAlongSlope)

    def forceFriction(coeficent, mass, gravity, forceY):
        forceFriction = coeficent*(friction.forceGravity(friction.forceGravity(mass, gravity))+forceY)
        return (forceFriction)

    def startMoving(sAngle, coenficentStatic, forceX, forceY, gravity, mass):
        fGravitySlope = friction.gravityAlongSlope(mass, gravity, sAngle)
        fFriction = friction.forceFriction(coenficentStatic, mass, gravity, forceY)
        if (fGravitySlope + forceX <= fFriction):
            return False
        elif (fGravitySlope + forceX > fFriction):
            return True

    def accelorationAlongPlane(sAngle, coenficentStatic, coenficentKenetic, forceX, forceY, gravity, mass):
        if friction.startMoving(sAngle, coenficentStatic, forceX, gravity, forceY, mass): 
            fFriction = friction.forceFriction(coenficentKenetic, mass, gravity, forceY)
            fGravitySlope = friction.gravityAlongSlope(mass, gravity, sAngle)
            fTotal = (fGravitySlope+forceX)-fFriction
            return (fTotal / mass)
        else:
            return 0
    
    
