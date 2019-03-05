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


    #methods
    def startStudent(self):
        #create new window
        winStudent = Toplevel(self.root)
        winStudent.title("Logged in as Student")
        winStudent.geometry("500x300")

        #page contents
        self.label = Label(winStudent, text="\nStudent portal\n")
        self.label.pack()

        self.takeButton = Button(winStudent, text="Take a test", command=lambda: self.studentTest(winStudent))
        self.takeButton.pack()

        self.feedButton = Button(winStudent, text="Look at feedback", command=self.studentFeedback)
        self.feedButton.pack()
        
        #close startup page
        self.root.withdraw()
        return

    def studentTest(self, winStudent):
        self.feedButton.destroy()
        
        self.label2 = Label(winStudent, text="\nChoose a test:\n")
        self.label2.pack()

        tests = [filename for filename in os.listdir("/tests") if os.path.splitext(filename)[1] == ".txt"]
        
        self.testMenu = OptionMenu(winStudent, "", *tests)
        self.testMenu.pack()
        return

    def studentFeedback(self):
        return

    def startLecturer(self):
        #create new window
        winLecturer = Toplevel(self.root)
        winLecturer.title("Logged in as Lecturer")
        winLecturer.geometry("500x300")
        #close startup page
        self.root.withdraw()
        return


#init
root = Tk()
window = program(root)
root.mainloop()
