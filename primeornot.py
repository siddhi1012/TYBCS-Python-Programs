number=int(input("Enter the Number :"))
if number>1:
        for i in range(2,int(number/2)+1):
            if(number % i)==0:
                print(number, "is not a prime number")
                break
        else:
            print(number,"number is prime")
else:
        print(number,"number is not prime")
