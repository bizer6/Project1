from sys import argv
import math
script, x = argv
x=int(x)
if x <= 1.2:
    y = (math.cos(math.pi * x))**2
else:
    y = (math.abs(math.ln(x+0.2)))**0.5
print("y=",y)