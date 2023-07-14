import random
import time
z = open("data/z.txt", "a")
y = open("data/y.txt", "a")
x = open("data/x.txt", "a")
j = float(input("timeout?  "))
f = "y"
h=0
g=0
while f == "y":
    e = 0
    d = int(input("how many iterations?  "))
    for i in range(d):
        a = 1
        b = 1
        while b == 1:
            c = random.randint(0, a)
            if c == 0:
                b = 0
                a += 1
            else:
                a += 1
        if d<4000:
            print (a)
        x.write(f"value2 ({a})  ")
        e += a
    print (f"average: {e/d}")
    z.write(f"average: ({e/d})  ")
    f = input("keep playing? ")
    h +=1
    g += (e/d)
print (f"full average  {g/h}  ")
y.write(f"full average  ({g/h})  ")
start = time.time()
while time.time() < start + j :
    a += 1
    a -= 1
