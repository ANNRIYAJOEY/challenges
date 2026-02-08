number=int(input('Enter a number:-'))
length=len(str(number))

temp=number
sum=0

while temp>0:
    digit=temp%10
    digit=digit**length
    sum=sum+digit
    temp=temp//10

if sum==number:
    print("It's an Armstrong number")
else:
    print("It's not an Armstrong number")



    
