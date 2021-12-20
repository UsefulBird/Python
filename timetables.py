import random
import stopwatch
from stopwatch.stopwatch import Stopwatch

stopwatch = Stopwatch()
stopwatch.reset()
a = input("Which timetable would you like to practice: ")
m = 0 
e = 0
f = int(input("How many questions would you like: "))

for i in range(f):
    b = random.randint(1, 9)
    answer = int(a) * int(b)
    print(str(a) + " X " + str(b) + ": ")
    stopwatch.start()
    c = input("")

    if int(c) == int(answer):
        print("Correct!")
        m += 1
        stopwatch.stop()
        print(str(stopwatch) + "\n")
        stopwatch.reset()
    else:
        print("Incorrect, the correct answer was: " + str(answer) + "\n")
        stopwatch.stop()
        stopwatch.reset()


print("Congratulations, your score is: " + str(m) + " out of " + str(f))

