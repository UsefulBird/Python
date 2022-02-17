Number = int(input(": "))
number_backup = str(Number)
Result = []
d = 2
while Number % d == 0:
    Result.append(d)
    q = int(Number/d)
    Number = q
d = 3
while d <= Number:
    while Number % d == 0:
        Result.append(d)
        q = int(Number / d)
        Number = q
    d += 2
length = len(Result)

if length == 1:
    print(number_backup + " is a prime number!")
    print(Result)
else:
    print(Result)

