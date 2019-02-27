import test, formativeTest, summativeTest
import student, lecturer
from tkinter import *

class program:
    #constructors
    def __init__(self, master):
        self.master = master
        master.title("QuizMachine v0.1")

        self.label = Label(master, text="Welcome to the Quiz machine!\nPlease log in:")
        self.label.pack()

        self.startButton = Button(master, text="Student", command=self.startStudent)
        self.startButton.pack()

        self.closeButton = Button(master, text="Lecturer", command=self.startLecturer)
        self.closeButton.pack(side="left")

    #methods
    def startStudent(self):
        return

    def startLecturer(self):
        return


#init
root = Tk()
window = program(root)
root.mainloop()
