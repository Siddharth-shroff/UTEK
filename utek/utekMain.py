## Main folder for emergency response suggestions
##

import UserDetails
import HQDetails
import math

def main():
    ## get the user data from the sheet into a ONE D String list
    userData = [" ", " "]
    emergencyOptions = ["Latitude", "Longitude"] #get the options for the emergency details

    #get the initial responser details (parameters and options for the parameter)
    hqParameters = [" ", " "]
    hqParameters = ["latitude", "longitude", "vehicles"]
    rescueOptions = [ [0]*3 for i in range(3)]

    user = UserDetails (userData)
    rescue = HQDetails (hqParameters, rescueOptions)
    user.getFilledInfo()

    #finding the dispatch center that's the closest to the citizen
    nearestLoc = []
    nearestLoc = location(user, rescue, emergencyOptions)
    print("The nearest location is the emergency response at a latitude of " + nearestLoc[0] + ", and a longitude of " + nearestLoc[1])

def location (user, rescue, emergencyOption):
    userLoc = [0, 0] #index 0 = latitude, 1 = longitude
    allRescueLat = rescue.responseOptions[:, rescue.responseParameters.index("Latitude")] #getting all latitudes of the rescue centers
    allRescueLong = rescue.responseOptions[:, rescue.responseParameters.index("Longitude")]

    rescueLoc = [0, 0]
    userLoc[0] = user.filledDetails[(emergencyOptions.index("Latitude"))]
    userLoc[1] = user.filledDetails[(emergencyOptions.index("Longitude"))]

    distances = []
    for i in range(len(allRescueLat)):
        distances[i] = math.sqrt(math.pow((userLoc[0] - allRescueLat[i]), 2) + math.pow((userLoc[1] - allRescueLong[i]), 2))
    indexOfNearestLoc = 0
    smallestDis = 100000000000
    for x in distances:
        if x <= smallestDis:
            smallestDis = x
            indexOfNearestLoc = distances.index(x)
    rescueLoc[0] = allRescueLat[indexOfNearestLoc]
    rescueLoc[1] = allRescueLong[indexOfNearestLoc]

    return rescueLoc


