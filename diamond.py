# Prints ascending and decending diamond from 1-9 on each row with one addition of a number each pass. 96 bytes.
def x():print(' '*(9-i)+str(int('1'*i)**2))
for i in range(1, 10):x()
for i in range(8,0,-1):x()