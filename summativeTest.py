import datetime
from test import test

class summativeTest(test):
    #constructors
    def __init__(self):
        super().__init__()
        self.resultsDate = datetime.datetime

    def __init__(self, resultsDate):
        super().__init__()
        self.resultsDate = resultsDate

    def __init__(self, resultsDate, questions, testResults):
        super().__init__(questions, testResults)
        self.resultsDate = resultsDate

    #getters
    def getResultsDate(self):
        return resultsDate

    #methods
    def submit(self):
        #submit data to dabtabse etc etc
        self.viewResult(test)
        return
    
    def viewResult(self, test):
        #opens the file for that test and finds your result
        return #return test result
