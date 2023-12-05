import math
r=int(input("Enter the radius :"))
h=int(input("Enter the height :"))
vol=math.pi*r*r*h
area=2*math.pi*r*h+2*math.pi*r*r
print("Surface area of Cylinder :",area)
print("Surface volume of Cylinder :",vol)
