import test, formativeTest, summativeTest
import os
from student import student
from lecturer import lecturer
from tkinter import *

def main(wnd):
    wnd.title("Log in")
    wnd.geometry("500x300")
    widgets = []
    widgets.append(Label(wnd, text="\nWelcome to the Quiz machine!\nPlease log in:\n"))
    widgets.append(Button(wnd, text="Student", command=lambda : startStudent(wnd, widgets, username.get())))
    widgets.append(Button(wnd, text="Lecturer", command=lambda : startLecturer(wnd, widgets, username.get())))
    username = Entry(wnd)
    widgets.append(username)
    show(widgets)


def show(widgets):
    for widget in widgets:
        widget.pack()


def remove(widgets):
    for widget in widgets:
        widget.destroy()
    return []


def startStudent(wnd, widgets, username):
    if username != "":
        user = student(username)
    else:
        return
    wnd.title("Logged in as Student")
    widgets = remove(widgets)
    widgets.append(Label(wnd, text="\nStudent portal\n"))
    widgets.append(Button(wnd, text="Take a test", command=lambda : studentTest(wnd, widgets, user)))
    widgets.append(Button(wnd, text="Look at feedback", command=lambda : studentFeedback(wnd, widgets, user)))
    show(widgets)


def studentTest(wnd, widgets, user):
    wnd.title("Take a test")
    widgets = remove(widgets)
    tests = [os.path.splitext(filename)[0] for filename in os.listdir("tests") if os.path.splitext(filename)[1] == ".csv"]
    var = StringVar(wnd)
    var.set(tests[0])
    widgets.append(Label(wnd, text="\nChoose a test:\n"))
    widgets.append(OptionMenu(wnd, var, *tests))
    widgets.append(Button(wnd, text="Start Test", command=lambda : user.takeTest(var.get())))
    show(widgets)


def studentFeedback(wnd, widgets, user):
    wnd.title("Get feedback")
    widgets = remove(widgets)


def startLecturer(wnd, widgets, username):
    if username != "":
        user = lecturer(username)
    else:
        return
    wnd.title("Logged in as Lecturer")
    widgets = remove(widgets)
    widgets.append(Label(wnd, text="\nLecturer portal\n"))
    widgets.append(Button(wnd, text="Create a test", command=lambda : lecturerCreate(wnd, widgets, user)))
    widgets.append(Button(wnd, text="Modify a test", command=lambda : lecturerModify(wnd, widgets, user)))
    show(widgets)


def lecturerCreate(wnd, widgets, user):
    wnd.title("Create a test")
    widgets = remove(widgets)
    editors = []
    widgets.append(Label(wnd, text="\nTest name:"))
    widgets.append(Entry(wnd))
    widgets.append(Button(wnd, text="Add a question", command=lambda : editors.append(addQuestion(wnd, widgets))))
    widgets.append(Button(wnd, text="Create test", command=lambda : createTest(wnd, widgets, editors, user)))
    show(widgets)


def addQuestion(wnd, widgets):
    editor = questionEditor(wnd)
    show(editor)
    return editor


def questionEditor(wnd):
    question = []
    question.append(Label(wnd, text="\nEnter question:"))
    question.append(Entry(wnd))
    question.append(Label(wnd, text="Correct answer:"))
    question.append(Entry(wnd))
    question.append(Label(wnd, text="Incorrect answers:"))
    for x in range(3):
        question.append(Entry(wnd))
    return question


def createTest(wnd, widgets, editors, user):
    data = [widgets[1].get()]
    for editor in editors:
        currentQuestion = []
        for widget in editor:
            if type(widget) == Entry:
                currentQuestion.append(widget.get())
        data.append(currentQuestion)
    if user.createTest(data):
        wnd.title("Test created")
        widgets = remove(widgets)
        for editor in editors:
            remove(editor)
        widgets.append(Label(wnd, text="\nTest created successfully.\n"))
        widgets.append(Button(wnd, text="OK", command=lambda : back(wnd, widgets, user)))
        show(widgets)
    else:
        widgets[0]["text"] = "\nA test with that name already exists!"


def back(wnd, widgets, user):
    if type(user) == student:
        startStudent(wnd, widgets, user.name)
    elif type(user) == lecturer:
        startLecturer(wnd, widgets, user.name)


def lecturerModify():
    pass


# Start the program
wnd = Tk()
main(wnd)
wnd.mainloop()
