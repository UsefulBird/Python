

from turtle import *
def turtle_controller(do, val):
    i = 0
    do = do.upper()
    if do == "F":
        forward(val)
    elif do == "B":
        backward(val)
    elif do == "L":
        left(val)
    elif do == "R":
        right(val)
    elif do == "U":
        penup()
    elif do == "D":
        pendown()
    elif do == "N":
        reset()
    elif do == "C":
        circle(val)
    elif do == "P":
        goto(0, 0)
        forward(200)
        right(90)
        circle(50)
        left(270)
        penup()
        left(90)
        forward(100)
        pendown()
        circle(50)
        right(90)
        forward(200)
        for i in range(12):
            forward(13)
            right(15)
        forward(13)
    elif do == "S":
        while i < 1000:
            circle(i)
            i += 10
    else:
        print("Unrecognized command")

def string_artist(program):
    cmd_list = program.split("-")
    for command in cmd_list:
        cmd_len = len(command)
        if cmd_len == 0:
            continue
        cmd_type = command[0]
        num = 0
        if cmd_len > 1:
            num_string = command[1:]
            num = int(num_string)
        print(command, ":", cmd_type, num)
        turtle_controller(cmd_type, num)

instruction = '''Enter a program for the turtle:
eg F100-R45-U-F100-L45-D-F11-R90-B50
N = New Drawing
U/D = Pen Up/ Pen Down
F100 = Forward 100
B50 = Backwards 50
R90 = Right turn 90 deg
L45 = Left turn 45 deg
C40 = 40 segment circle
P = Easter egg
S = Loads of circles'''
screen = getscreen()
while True:
    t_program = screen.textinput("Drawing Machine", instruction)
    print(t_program)
    if t_program == None or t_program.upper() == "END":
        break
    string_artist(t_program)
    