lowervalue=int(input("enter the lower range :"))
highervalue=int(input("enter the Higher range :"))
print("The prime Number the given range")
for number in range(lowervalue,highervalue+1):
    if number>1:
        for i in range(2,number):
            if(number%i)==0:
                break
        else:
                print(number)