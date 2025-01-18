# store how many resources / rescue dipatchers the emergency responders have

class HQDetails:

    def _init_ (self, responseParametersList, responseOptions): #allCitizenParameters, userParameters (other parameters?)
        self.responseParameters = responseParametersList #store all emergency rescue options
        self.availableRescue = responseOptions #store all available rescue options (2D list)