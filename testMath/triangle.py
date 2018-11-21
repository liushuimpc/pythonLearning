import math

# triangle
x=input('Please input length of two side and angle (use comma to separate them):').split(",")
a, b, angle=x
print('a=' + a + ', b=' + b + ', angle=' + angle)

a = float(a)
b = float(b)
angle = float(angle)

c=math.sqrt(math.pow(a, 2) + math.pow(b, 2) - 2*a*b*math.cos(angle*math.pi/180))
print('c='+str(c))

# resistor
r1, r2 = input('Please input 2 resistor values:').split(",")
r1 = float(r1)
r2 = float(r2)
R = 1.0 / (1.0 / r1 + 1.0 / r2)
print('The output resistor value:' + str(R))
