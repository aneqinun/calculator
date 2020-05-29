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

    # create buttons and place within grid
    # functions executed when specific button pressed
    button1 = Button(gui, text=' 1 ', fg='black', bg='white smoke',
                     command=lambda: press(1), height=2, width=14)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='white smoke',
                     command=lambda: press(2), height=2, width=14)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='white smoke',
                     command=lambda: press(3), height=2, width=14)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='white smoke',
                     command=lambda: press(4), height=2, width=14)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='white smoke',
                     command=lambda: press(5), height=2, width=14)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='white smoke',
                     command=lambda: press(6), height=2, width=14)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='white smoke',
                     command=lambda: press(7), height=2, width=14)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='white smoke',
                     command=lambda: press(8), height=2, width=14)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='white smoke',
                     command=lambda: press(9), height=2, width=14)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='white smoke',
                     command=lambda: press(0), height=2, width=14)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='white smoke',
                  command=lambda: press("+"), height=2, width=14)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='white smoke',
                   command=lambda: press("-"), height=2, width=14)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='white smoke',
                      command=lambda: press("*"), height=2, width=14)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='white smoke',
                    command=lambda: press("/"), height=2, width=14)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='white smoke',
                   command=equalpress, height=2, width=14)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='C', fg='black', bg='white smoke',
                   command=clear, height=2, width=14)
    clear.grid(row=5, column='1')

    Decimal= Button(gui, text='.', fg='black', bg='white smoke',
                    command=lambda: press('.'), height=2, width=14)
    Decimal.grid(row=6, column=0)

    # start the GUI
    gui.mainloop()