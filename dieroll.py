from fractions import Fraction

buf = input()
buf = buf.split(' ')
y = int(buf[0])
x = int(buf[1])

if x > y:
    big = x
else:
    big = y
possibleNumbers = 6 - big + 1
if Fraction(possibleNumbers, 6) == 1:
    print('1/1')
else:
    print(Fraction(possibleNumbers, 6))
