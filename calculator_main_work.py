initialise 'held object' as 0
initialise 'held equation' as 0

heldObject = null
heldEquation = null

"""
# first user input

if 'first user input' is a number:
    overwrite 'held object'

else if the 'first user input' is an operator:
    do nothing

# second user input

if the 'second user input' is a number:
    append 'second user input' to 'held object'

else if the 'second user input' is an operation:
    append the 'held object' to the 'held operation'
    append the operation to the 'held equation'
    clear 'held object'

# next user input

if the 'second user input' is a number apply following conditions:

    if the 'next user input' is a number:
        append the number to the held object

    else if the 'next user input' is an operation:
        append the 'held object' to the 'held equation'
        append the operation to the 'held equation'
        clear 'held object'


else if the second user input is an operator:

    if the 'next user input' is a number:
        append the number to the 'held object'

    else if the 'next user input' is an operation:
        overwrite 'held object'

"""