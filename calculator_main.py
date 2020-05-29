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