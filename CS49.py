import math

x, y = 0, 0

while True:
    step = input("Type UP/DOWN/LEFT/RIGHT #step number: ")

    if step == "EXIT":
        break

    else:
        step = step.split(" ")

        if step[0] == "UP":
            y = y + int(step[1])
        elif step[0] == "DOWN":
            y = y - int(step[1])
        elif step[0] == "LEFT":
            x = x - int(step[1])
        elif step[0] == "RIGHT":
            x = x + int(step[1])

dist = math.sqrt(x ** 2 + y ** 2)

print("Distance after sequence of movements:", dist)
