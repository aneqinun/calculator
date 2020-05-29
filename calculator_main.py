# import everything from tkinter
from tkinter import *

# declare the heldExpression variable
heldExpression = ""

# update heldExpression in the input box on press
def press(number):
    global heldExpression

    # append to heldExpression on press
    heldExpression = heldExpression + str(number)

    # set heldExpression
    equation.set(heldExpression)


# evaluate heldExpression on equals press
def equalpress():


    try:

        global heldExpression

        # evaluate heldExpression, str function converts result to string
        total = str(eval(heldExpression))
        equation.set(total)

        # initialze heldExpression to empty string
        heldExpression = ""

    # handles evaluation errors such as division by zero
    except:

        equation.set(" error ")
        heldExpression = ""


# Clear input box to empty string
def clear():
    global heldExpression
    heldExpression = ""
    equation.set("")

# Driver code
if __name__ == "__main__":
    # create window
    gui = Tk()

    # set the window colour, title, dimensions
    gui.configure(background="gainsboro")
    gui.title("Calculator")
    gui.geometry("490x270")

    # create instance of StringVar()
    equation = StringVar()

    # create user entry box to show heldExpression
    heldExpression_field = Entry(gui, textvariable=equation)

    # apply grid method to place buttons
    heldExpression_field.grid(columnspan=8, ipadx=153)

    # start the GUI
    gui.mainloop()