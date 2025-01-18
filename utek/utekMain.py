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
    user.loc = [user.filledDetails[(emergencyOptions.index("Latitude"))], user.filledDetails[(emergencyOptions.index("Longitude"))]]
    
    #finding the dispatch center that's the closest to the citizen
    nearestRescueLoc = []
    nearestRescueLoc = locationToRescue(user, rescue, emergencyOptions)

    print("The nearest location is the emergency response at a latitude of " + nearestRescueLoc[0] + ", and a longitude of " + nearestRescueLoc[1])

    fireLoc = [0, 0] #FILL IN WITH THE COORDINATES OF THE FIRE
    distanceToFire = locationToFire (user, fireLoc)

    #inputting the age and injury type
    age = int(input ("what is your age?"))
    lat_location = float(input("what is your latitude?"))
    long_location = float(input("what is your longitude?"))
    
    print("Option 1:" CTAS_level_1)
    print("Option 2:" CTAS_level3)
    print("Option 3:" CTAS_level2)
    print("Option 4:" CTAS_level4)
    print("Option 5:" CTAS_level_5)
    
    injury=int(input("Is your injury best described using options 1,2,3,4, or 5"))
    res = prioritizing(age,lat_location, long_location, injury)
    print("the priority level of this person is: ", res)


def prioritizing(age,lat_location, long_location, injury):
    priority=1

    if age <= 15:
        priority+=2
    if age <= 30 and >15:
        priority+=1
    if injury == "1":
        priority+=5
    if injury == "2":
        priority+=4
    if injury == "3":
        priority+=3
    if injury == "4":
        priority+=2
    if injury == "5":
        priority+=1
    return priority




#figure out the closest dispatcher to the user 
def locationToRescue (user, rescue):
    allRescueLat = rescue.responseOptions[:, rescue.responseParameters.index("Latitude")] #getting all latitudes of the rescue centers
    allRescueLong = rescue.responseOptions[:, rescue.responseParameters.index("Longitude")]
    rescueLoc = [0, 0]

    distances = []
    for i in range(len(allRescueLat)):
        distances[i] = math.sqrt(math.pow((user.loc[0] - allRescueLat[i]), 2) + math.pow((user.loc[1] - allRescueLong[i]), 2))
    indexOfNearestLoc = 0
    smallestDis = 100000000000
    for x in distances:
        if x <= smallestDis:
            smallestDis = x
            indexOfNearestLoc = distances.index(x)
    rescueLoc[0] = allRescueLat[indexOfNearestLoc]
    rescueLoc[1] = allRescueLong[indexOfNearestLoc]

    return rescueLoc

#figure out the distance of the user to the fire using pythagorean theorem
def locationToFire (user, fireLoc):
    distance = math.sqrt(math.pow((user.loc[0] - fireLoc[0]), 2) + math.pow((user.loc[1] - fireLoc[0]), 2))
    return distance



