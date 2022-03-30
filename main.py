from random import *

a = 0
while 1:
    b = random() * 1000000
    a = random() * 1000000
    print(int(b))
    print(int(a), "\n")
    if int(b) == int(a):
        print('end')
        break
