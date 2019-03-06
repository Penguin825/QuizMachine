import csv

class lecturer():
    #constructors
    def __init__(self):
        self.name = ""
        return

    def __init__(self, name):
        self.name = name
        return


    #methods
    def readDatabase(self):
        with open("database.csv", "r") as file:
            reader = csv.reader(file)
            records = list(reader)
        return records

    
    def searchDatabase(self, searchTerm):
        data = self.readDatabase()
        results = []
        for record in data:
            # If any of the items in the current row of the database
            # contain the search term, return the whole row.
            if any(searchTerm in x for x in record):
                results.append(record)
        if len(results) == 0:
            return ["No results found"]
        else:
            return results


    def createTest(self, data):
        testName = "tests/{}.csv".format(data[0])
        data = data[1:]

        #create test file
        try:
            with open(testName) as file:
                return False
        except IOError:
            with open(testName, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(data)
                return True

