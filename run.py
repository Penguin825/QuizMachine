import tkinter


def start():
    window = tkinter.Tk()
    window.title("Quiz Machine")
    window.geometry("300x300")

    text = tkinter.Label(window, text="\nWelcome to the Quiz Machine\nPlease sign in:\n")
    buttonStudent = tkinter.Button(window, text="Student", command=student)
    buttonLecturer = tkinter.Button(window, text="Lecturer")

    for widget in [text, buttonStudent, buttonLecturer]:
        widget.pack()

    window.mainloop()

def student():
    winStudent = tk.Toplevel(window)
