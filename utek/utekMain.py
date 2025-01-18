## Main folder for emergency response suggestions
##

import UserDetails
import HQDetails
import math

CTAS_level_1=('Cardiac arrest, pre arrest, return of spontaneous circulation (ROSC), chest pain with cardiac features, severe dehydration, chemical burn ≥25% body surface area, unconsciousness, seizures, pregnancy >= 20 weeks - presenting fetal parts, prolapsed cord, Pregnancy >= 20 weeks - vaginal bleeding in 3rd trimester, Respiratory arrest, shortness of breath')
CTAS_level2=('chest pain with cardiac features, hypertension, moderate dehydration, dental avulsion, sore throat, neck pain, Epistaxis, chemical exposures to some body parts, allergic reaction, severe headache, pregnancy >= 20 weeks - presenting fetal parts, prolapsed cord, Pregnancy >= 20 weeks, acute vision loss, shortness of breath, Seizure post-ictal, abdominal pain')
CTAS_level3=('chest pain with no cardiac features, Mild dehydration, resolved Seizures, start of CVA symptoms, Menorrhagia, Pregnancy ≥20 weeks, mild/moderate respiratory distress, burn 5-25% body surface area')  
CTAS_level4=('Hypertension, Potential for dehydration, Non pregnant vaginal bleeding, burn <5% body surface area')
CTAS_level_5=('Sore throat, upper respiratory illness, Minor contusions, abrasions or lacerations')
emergencyOptions = []

def main():
    print ("USER SIDE")
    emergencyOptions = ["Latitude", "Longitude"] #get the options for the emergency details
    sheets = sheets_user.col_values(1).count() - 1 # FILL IN WITH THE NUMBER OF ROWS IN THE GOOGLE SHEETS - number of rows in the user sheets - (-1 because the first row is the header)

    #get the initial responser details (parameters and options for the parameter)
    hqParameters = [" ", " "]
    hqParameters = ["latitude", "longitude", "vehicles"]
    rescueOptions = [ [0]*3 for i in range(3)]

    rescue = HQDetails (hqParameters, rescueOptions)
    user = []
    for i in range (1, sheets):
        user.append(eachUser(i), rescue)

    # send over all priority to the GOOGLE SHEETS AND SORT BASED ON PRIORITY
    user = sortingPriority (user)

    


def prioritizing(age, distance, injury):
    priority=1
    if age <= 10:
        priority+=3
    if age <= 15:
        priority+=2
    if age <= 30 and age>15:
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

    #prioritizing based on distance to the fire
    if distance <= 250:
        priority +=10
    elif distance <= 500:
        priority +=9
    elif distance <= 1000:
        priority +=8
    elif distance <= 2000:
        priority +=7
    elif distance <= 3000:
        priority +=5
    elif distance <= 5000:
        priority +=3
    else:
        priority +=1
        
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


#determining each user
def eachUser (rowNumber, rescue):
    ## get the user data from the sheet into a ONE D String list

    userData = sheets_user.row_values(rowNumber) #use a google sheet function to get each row data from the row letter
    user = UserDetails (userData)
    user.getFilledInfo()
    user.loc = [user.filledDetails[(emergencyOptions.index("Latitude"))], user.filledDetails[(emergencyOptions.index("Longitude"))]]

    print("Option 1: " + CTAS_level_1)
    print("Option 2: " + CTAS_level3)
    print("Option 3: " + CTAS_level2)
    print("Option 4: " + CTAS_level4)
    print("Option 5: " + CTAS_level_5)
    injury=int(input("Is your injury best described using options 1,2,3,4, or 5"))
    age = int(input ("what is your age?"))

    #finding the dispatch center that's the closest to the citizen
    nearestRescueLoc = []
    nearestRescueLoc = locationToRescue(user, rescue, emergencyOptions)

    print("The nearest location is the emergency response at a latitude of " + nearestRescueLoc[0] + ", and a longitude of " + nearestRescueLoc[1])

    fireLoc = [0, 0] #FILL IN WITH THE COORDINATES OF THE FIRE
    distanceToFire = locationToFire (user, fireLoc)

    res = prioritizing(age, distanceToFire, injury)
    print("the priority level of person " + " is: ", res)
    user.priority = res
    return user

def sortingPriority (user):
    sortedUser = user
    n = len(user)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if sortedUser[j].priority > sortedUser[j + 1].priority:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                sortedUser[j], sortedUser[j + 1] = sortedUser[j + 1], sortedUser[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return sortedUser
