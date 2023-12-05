a=float(input('Enter the First side :'))
b=float(input('Enter the Second side :'))
c=float(input('Enter the Third side :'))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('Area of Triangle is %0.2f'%area)