n1=int(input("Enter the First Number :"))
n2=int(input("Enter the second :"))
print("Enter the Which Operation do you want to perform")
ch=input("Enter any specific opreation + - * / :")
result=0
if ch=='+':
    result=n1+n2
elif ch=='-':
    result=n1-n2
elif ch=='*':
    result=n1*n2
elif ch=='/':
    result=n1/n2
else:
    print("Invalid")
print(n1,ch,n2,":",result)