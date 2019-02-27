class test():
    #constructors
    def __init__(self):
        self.questions = []
        self.testResults = []

    def __init__(self, questions, testResults):
        self.questions = questions
        self.testResults = testResults

    #getters
    def getQuestions(self):
        return self.questions

    def getResults(self):
        return self.testResults

    #methods
    def submit(self):
        #put code here
