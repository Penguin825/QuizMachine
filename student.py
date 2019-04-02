import csv

class student():
    #constructors
    def __init__(self):
        self.name = ""
        return

    def __init__(self, name):
        self.name = name
        return

    #getters
    def getName():
        return self.name

    #methods
    def takeTest(self, testName):
        testName = "tests/{}.csv".format(testName)
        testData = []
        with open(testName, "r") as test:
            reader = csv.reader(test, delimiter=",")
            for question in reader:
                testData.append(question)
        return testData

    def checkAnswers(self, testName, answers):
        testName = "tests/{}.csv".format(testName)
        results = []
        with open(testName, "r") as test:
            reader = csv.reader(test, delimiter=",")
            for question, answer in zip(reader, answers):
                results.append(True if question[1] == answer else False)
        return results
