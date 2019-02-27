class test():
    #constructors
    def __init__(self):
        self.questions = []
        self.testResults = []

    def __init__(self, questions, testResults):
        self.questions = questions
        self.testResults = testResults
        #create .txt file in the tests folder to store test data
        #generate a filename that isnt' already being used

    #getters
    def getQuestions(self):
        return self.questions

    def getResults(self):
        return self.testResults

    #methods
    def submit(self):
        #put test results in database.csv
        #open file and write to the end of it
        return
