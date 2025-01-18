## Main folder for emergency response suggestions
##

#google spreadsheet link below:
#https://docs.google.com/spreadsheets/d/10TbyUgVjGJbbiXXNkypdKx-fHO-W6i74ddiMj8DkQJk/edit?usp=sharing

import gspread
from google.oauth2.service_account import Credentials
import UserDetails
import HQDetails
import math

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("C:/Users/karen/Desktop/UTEK/credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "10TbyUgVjGJbbiXXNkypdKx-fHO-W6i74ddiMj8DkQJk"
workbook = client.open_by_key(sheet_id)

sheets_user = workbook.worksheet("User")
sheets_hq = workbook.worksheet("Emergency")
sheets_fire = workbook.worksheet ("Fire")



CTAS_level_1 = '\n - Cardiac arrest\n - pre arrest\n - return of spontaneous circulation (ROSC)\n - chest pain with cardiac features\n - severe dehydration\n - chemical burn ≥25% body surface area\n - unconsciousness\n - seizures\n - pregnancy >= 20 weeks - presenting fetal parts, prolapsed cord\n - Pregnancy >= 20 weeks - vaginal bleeding in 3rd trimester\n - Respiratory arrest\n - shortness of breath'
CTAS_level_2 = '\n - chest pain with cardiac features\n - hypertension\n -  moderate dehydration\n - dental avulsion\n - sore throat\n - neck pain\n - Epistaxis\n - chemical exposures to some body parts\n - allergic reaction\n - severe headache\n - pregnancy >= 20 weeks - presenting fetal parts, prolapsed cord\n - Pregnancy >= 20 weeks\n - acute vision loss\n - shortness of breath\n - Seizure post-ictal\n - abdominal pain'
CTAS_level_3 = '\n - chest pain with no cardiac features\n - Mild dehydration\n - resolved Seizures\n - start of CVA symptoms\n - Menorrhagia\n - Pregnancy ≥20 weeks\n - mild/moderate respiratory distress\n - burn 5-25% body surface area'
CTAS_level_4 = '\n - Hypertension \n - Potential for dehydration\n - Non pregnant vaginal bleeding\n - burn <5% body surface area'
CTAS_level_5 = '\n - Sore throat \n - upper respiratory illness\n - Minor contusions, abrasions or lacerations'


## store the emergency information of the user
class UserDetails:
    key = ''
    def __init__ (self, strList):
        self.filledDetails = strList
        self.loc = []
        filledDetails = strList
        self.priority = 0  
        self.injury = 0 
        """
        for i in range (len(self.filledDetails)):
            print (str(i) + "\t" + filledDetails[i])
        """
        
        
        #self.filledIndices = [0]
        #self.details
        #self.filledDetails = self.details #stores the filled details of the user 
    """
    def getFilledInfo (self):
        i = 0
        #userFilledDetails = self.details #
        for x in self.details:
            self.filledIndices.add(i) #creating how many citizen parameters there are (empty and filled parameters)
            i = i+1
        for i in self.details.count():
            if self.details[i] == "":
                self.userFilledDetails.pop(i)
                self.filledIndices.pop(i)
        #return userFilledDetails
    """
    def string (self):
        for i in range(len(self.filledDetails)):
            strDetails = strDetails + self.filledDetails[i] + " | "
        return strDetails
    
        
# store how many resources / rescue dipatchers the emergency responders have

class HQDetails:

    def __init__ (self, responseParametersList, responseOptions): #allCitizenParameters, userParameters (other parameters?)
        self.responseParameters = responseParametersList #store all emergency rescue options
        self.availableRescue = responseOptions #store all available rescue options (2D list)


emergencyOptions = sheets_user.row_values(1) #get the options for the emergency details

def main():
    print ("USER SIDE")
    """if "Latitude" in emergencyOptions and "Longitude" in emergencyOptions:
        lat_index = emergencyOptions.index("Latitude")
        long_index = emergencyOptions.index("Longitude")
        user.loc = [user.filledDetails[lat_index], user.filledDetails[long_index]]
    else:
        print("Error: Latitude or Longitude not found in emergency options.")
    """

    #get the initial responser details (parameters and options for the parameter)
    hqParameters = sheets_hq.row_values(1)
    #print(hqParameters)
    
    rescueOptions = sheets_hq.get_all_values()
    rescue = HQDetails(hqParameters, rescueOptions)

    user = []
    for i in range (0, 5):
        user.append(eachUser(i))
        

    emergencyOptions = sheets_user.row_values(1) #get the options for the emergency details
    

    """print ("Emergency options at index latitude " + str(emergencyOptions.index('Latitude')))
    print ("user filled details:  " + x for x in user.filledDetails )
    print(len(user.filledDetails))
    """

    ## sort users based on priority
    user = sortingPriority (user)
    
    print ("\nRESPONDER SIDE")
    assignDispatchers (user, rescue)

"""
    #finding the dispatch center that's the closest to the citizen
    nearestRescueLoc = []
    nearestRescueLoc = locationToRescue(user, rescue)

    print("The nearest location is the emergency response at a latitude of " + str(nearestRescueLoc[0]) + ", and a longitude of " + str(nearestRescueLoc[1]))
"""


#input citizens in need
def eachUser (rowNumber):
    print("Option 1: " + CTAS_level_1)
    print("\n")
    print("Option 2: " + CTAS_level_2)
    print("\n")
    print("Option 3: " + CTAS_level_3)
    print("\n")
    print("Option 4: " + CTAS_level_4)
    print("\n")
    print("Option 5: " + CTAS_level_5)
    print("\n")
    print("Option 6: None of the above (no medical emergency)\n")


    name = input("Please enter your full name:\n")
    injury=int(input("Is your injury best described using options 1, 2, 3, 4, 5, or 6\n"))
    while (injury > 6 or injury < 1):
        injury=int(input("Please input an integer from 1 to 6. Is your injury best described using options 1, 2, 3, 4, 5, or 6\n"))
    if (injury == 6):
        injury= int(input("Do you require assistance from the fire department (7) or police department (8)\n"))
        while (injury > 8 or injury < 7):
            injury= int(input("Please input either 7 or 8. Do you require assistance from the fire department (7) or police department (8)\n"))
    age = int(input ("What is your age?\n"))



    ## get the user data from the sheet into a ONE D String list
    userData = sheets_user.row_values(rowNumber+1)

    #add the name, age, injury into the spreadsheet
    line_num = rowNumber+2 #note: line_num += 1 after each iteration
    sheets_user.update_acell('B'+str(line_num), name)
    sheets_user.update_acell('F'+str(line_num), injury)
    sheets_user.update_acell('E'+str(line_num), age)

    user = UserDetails(userData)
    user.injury = injury




    user.loc = [float(sheets_user.cell(rowNumber+2, 3).value), float(sheets_user.cell(rowNumber+2, 4).value)]
    #print (user.loc[0] + " " + user.loc[1] + " LONG AND LAT PF ISER")

    fireLoc = [sheets_fire.acell('A2').value, sheets_fire.acell('B2').value] #coordinates of the fire
    distanceToFire = locationToFire (user, fireLoc)

    

    res = prioritizing(age, distanceToFire, injury)
    #print("the priority level of person " + str(i) + " is: ", res)
    user.priority = res
    sheets_user.update_acell('G'+str(line_num),res)

    return user

#sorting all the users based on priority
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

##prioritizing each user based on their age, distance to the fire, and their physical injury
def prioritizing(age, distance, injury):
    priority=1
    if age <= 10:
        priority+=3
    if age <= 15:
        priority+=2
    if age <= 30 and age>15:
        priority+=1

    if injury == "1":
        priority+=6
    if injury == "2":
        priority+=5
    if injury == "3":
        priority+=4
    if injury == "7" or injury == "8": #prioritizing fire and police departments over health levels 4 and 5
        priority+=3
    if injury == "4":
        priority+=2
    if injury == "5":
        priority +=1

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
    allRescueLat = [float(row[rescue.responseParameters.index("Latitude")]) for row in rescue.availableRescue[1:]] #getting all latitudes of the rescue centers
    allRescueLong = [float(row[rescue.responseParameters.index("Longitude")]) for row in rescue.availableRescue[1:]]
    rescueLoc = [0, 0]

    distances = []
    for i in range(len(allRescueLat)):
        rescue_lat = float(allRescueLat[i])  # Convert to float
        rescue_long = float(allRescueLong[i])  # Convert to float
        distance = math.sqrt(math.pow(float(user.loc[0]) - rescue_lat, 2) + math.pow(float(user.loc[1]) - rescue_long, 2))
        distances.append(distance)
    indexOfNearestLoc = 0
    smallestDis = 100000000000
    for x in distances:
        if x <= smallestDis:
            smallestDis = x
            indexOfNearestLoc = distances.index(x)
    rescueLoc[0] = allRescueLat[indexOfNearestLoc]
    rescueLoc[1] = allRescueLong[indexOfNearestLoc]

    return indexOfNearestLoc

#figure out the distance of the user to the fire using pythagorean theorem
def locationToFire(user, fireLoc):
    distance = math.sqrt((float(user.loc[0]) - float(fireLoc[0]))**2 + (float(user.loc[1]) - float(fireLoc[1]))**2)
    return distance

#assign dispatchers to highly prioritized citizens
def assignDispatchers (users, rescue):
    print ("Must aid these 5 citizens: ")
    for i in range (0, 5):
        print (str(i) + " " + users[i].string(users[i]) + "\n")
        indexOfnearestRescueLoc = 0
        indexOfnearestRescueLoc = locationToRescue(users[i], rescue, emergencyOptions)
        print ("Dispatch " + rescue[indexOfnearestRescueLoc][rescue.responseParameters.index("Response center")] + " with ")
        if (users[i].injury == 1 or users[i].injury == 2 or users[i].injury == 3 or users[i].injury == 4 or users[i].injury == 5):
            print (str(1))
        else: 
            print (str(0))
        print (" ambulances + ")
        if (users[i].injury ==7):
            print (str(1))
        else: 
            print (str(0))
        print (" firetrucks + ")
        if (users[i].injury ==8):
            print (str(1))
        else: 
            print (str(0))
        print (" police cars + ")
        

main()

#User - column that says priority
#Priority is stored in the User sheet

#Sorting- try to do that 

#after sorted - take the first few roles and then 