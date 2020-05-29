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
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="gainsboro")

    # set the title of GUI window
    gui.title("Calculator")

    # set the configuration of GUI window
    gui.geometry("490x270")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the heldExpression
    heldExpression_field = Entry(gui, textvariable=equation)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    heldExpression_field.grid(columnspan=8, ipadx=153)

    # start the GUI
    gui.mainloop()