def calcThrowData(horizontalVel, verticalVel):
    """This function recievs 2 integers/floats - vertical and horizontal velocities.
       This function returns a dictionary with fields 't' and 'distance'
       that describes the time the projectile is airborne
       and the distance the projectile travels in the horizontal direction accordingly"""
    trajectoryData = dict()
    airborneTime = findAirborneTime(verticalVel)
    trajectoryData["t"] = airborneTime
    trajectoryData["distance"] = round(findHorizontalDistance(
        horizontalVel, airborneTime))
    return trajectoryData


def findAirborneTime(verticalVel):
    """This function recies an integer/float that describe a projectile vertical velocity.
       The function returns an integer/float that describes the time the projectile is airborne"""
    g = 9.81
    return 2*verticalVel/g


def findHorizontalDistance(horizontalVel, airborneTime):
    """This function recies 2 integers/floats - a projectile horizontal velocity and the time he is airborne.
       The function returns an integer/float that describes the distance the projectile travels in the horizontal direction"""
    return horizontalVel*airborneTime
