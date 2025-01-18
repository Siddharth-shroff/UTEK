## store the emergency information of the user

class UserDetails:
    key = ''
    def _init_ (self, strList):
        self.details = strList
        self.filledIndices = [0]
        #self.details
        self.filledDetails = self.details #stores the filled details of the user 
        self.loc = []
        
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
        
