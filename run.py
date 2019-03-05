import test, formativeTest, summativeTest, student, lecturer
import os
from tkinter import *

class program:
    #constructors
    def __init__(self, root):
        #create startup page
        self.root = root
        root.title("Log in")
        root.geometry("500x300")

        #page contents
        self.label = Label(root, text="\nWelcome to the Quiz machine!\nPlease log in:\n")
        self.label.pack()

        self.stuButton = Button(root, text="Student", command=self.startStudent)
        self.stuButton.pack()

        self.lecButton = Button(root, text="Lecturer", command=self.startLecturer)
        self.lecButton.pack()

        self.username = Entry(self.root)
        self.username.pack()

    #methods
    def startStudent(self):
        if self.username.get() != "":
            self.user = student.student(str(self.username.get()))
        else:
            return        
        #create new window
        self.winStudent = Toplevel(self.root)
        self.winStudent.title("Logged in as Student")
        self.winStudent.geometry("500x300")

        #page contents
        self.label = Label(self.winStudent, text="\nStudent portal\n")
        self.label.pack()

        self.takeButton = Button(self.winStudent, text="Take a test", command=self.studentTest)
        self.takeButton.pack()

        self.feedButton = Button(self.winStudent, text="Look at feedback", command=self.studentFeedback)
        self.feedButton.pack()
        
        #close startup page
        self.root.withdraw()
        return


    def studentTest(self):
        self.feedButton.destroy()
        
        self.label2 = Label(self.winStudent, text="\nChoose a test:\n")
        self.label2.pack()

        # Look in the tests folder and create a list of all the filenames
        tests = [os.path.splitext(filename)[0] for filename in os.listdir("tests") if os.path.splitext(filename)[1] == ".csv"]

        # Create a dropdown menu with the tests in it
        self.var = StringVar(self.winStudent)
        self.var.set(tests[0])

        self.testMenu = OptionMenu(self.winStudent, self.var, *tests)
        self.testMenu.pack()

        # Create a button that, when clicked, will call student.takeTest and pass the
        # name of the test as a parameter.
        startButton = Button(self.winStudent, text="Start test", command=lambda: self.user.takeTest(self.var.get()))
        startButton.pack()
        
        return


    def studentFeedback(self):
        return


    def startLecturer(self):
        if self.username.get() != "":
            self.user = lecturer.lecturer(str(self.username.get()))
        else:
            return
        
        #create new window
        self.winLecturer = Toplevel(self.root)
        self.winLecturer.title("Logged in as Lecturer")
        self.winLecturer.geometry("500x300")

        #page contents
        self.label = Label(self.winLecturer, text="\nLecturer portal\n")
        self.label.pack()

        self.createButton = Button(self.winLecturer, text="Create a test", command=self.lecturerCreate)
        self.createButton.pack()

        self.modifyButton = Button(self.winLecturer, text="Modify a test", command=self.lecturerModify)
        self.modifyButton.pack()
        
        
        #close startup page
        self.root.withdraw()
        return


    def lecturerCreate(self):
        self.label.destroy()
        self.createButton.destroy()
        self.modifyButton.destroy()

        self.editors = []
        self.radioVars = []

        #page contents
        self.testNameLabel = Label(self.winLecturer, text="Test name:")
        self.testNameLabel.pack()

        self.testNameEntry = Entry(self.winLecturer)
        self.testNameEntry.pack()

        self.addQuestionButton = Button(self.winLecturer, text="Add a question", command=self.addQuestion)
        self.addQuestionButton.pack()

        self.createTestButton = Button(self.winLecturer, text="Create test", command=self.createTest)
        self.createTestButton.pack()
        return

    def addQuestion(self):
        self.editors.append(self.questionEditor())
        for item in self.editors[-1]:
            item.pack()
        return


    def questionEditor(self):
        question = []
        label = Label(self.winLecturer, text="Enter question:")
        question.append(label)

        questionText = Entry(self.winLecturer)
        question.append(questionText)

        options = ["A", "B", "C", "D"]

        for option in options:
            newLabel = Label(self.winLecturer, text="Option {}".format(option))
            question.append(newLabel)

            newEntry = Entry(self.winLecturer)
            question.append(newEntry)

        var = IntVar()
        self.radioVars.append(var)
        newLabel2 = Label(self.winLecturer, text="Correct answer:")
        for option, num in zip(options, range(4)):
            radioButton = Radiobutton(self.winLecturer, text=option, padx=20, variable=var, value=num)
            question.append(radioButton)
            
        return question
        
    def createTest(self):
        data = [self.testNameEntry.get()]
        for question, var in zip(self.editors, self.radioVars):
            currentQuestion = []
            for widget in question:
                if type(widget) == Entry:
                    currentQuestion.append(widget.get())
                elif type(widget) == Radiobutton:
                    currentQuestion.append(var.get())
                    break
            data.append(currentQuestion)
        if self.user.createTest(data):
            self.testNameLabel["text"] = "Test created successfully."
            self.backButton = Button(self.winLecturer, text="OK", command=self.back)
            self.backButton.pack()
            #remove everything from the screen
            self.testNameEntry.destroy()
            self.addQuestionButton.destroy()
            self.createTestButton.destroy()
            for question in self.editors:
                for widget in question:
                    widget.destroy()
        else:
            self.testNameLabel["text"] = "A test with that name already exists!"
            

    def back(self):
        self.testNameLabel.destroy()
        self.backButton.destroy()
        self.winLecturer.destroy()
        self.startLecturer()

    def lecturerModify(self):
        #put code here
        return

#init
root = Tk()
window = program(root)
root.mainloop()
