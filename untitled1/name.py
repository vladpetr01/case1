import math


number = float(input())
while number > 1:
    print(int(math.fmod(number, 2)))
    number = number - math.fmod(number, 2)
    number = number / 2
if number == 1:
    print(1)
else:
    print(0)


