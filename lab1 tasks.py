task#01
reversing_a_no
n=int(input("Enter an integer"))
rev_no=0
while (n>0):
    remainder=n%10
    rev_no=(rev_no*10)+remainder
    n=n//10
print("The reversed number is"+ " "+format(rev_no).  

 task#2

n=int(input("enter numbers to add : "))
even=0
odd=0

for num in range(1,n+1):
    n=int(input("enter the values : "))
    if(num%2==0):
        even=even+num
    else:
       odd=odd+num

print("total of even numbers=",even)
print("total of odd numbers=",odd)

 task#3

n=int(input("enter the terms : "))
fe=0
se=1
if n<0:
    print("enter positive values")
else:
    print(fe,se,end="")
for x in range(2,n):
    next=fe+se
    print(next,end="")
    fe=se
    se=next

 Task#4
    
n = int(input('Enter a marks of student:'))

if n>100 or n<0:
    print('invalid input')
else:
    if n<50:
        print('You Got F Grade, Better luck next time:',n)
    elif n>50 and n<60:
        print(' Your Grade is E, Improvement suggested',n)
    elif n>61 and n<70:
        print('D is your Grade',n)
    elif n>71 and n<80:
        print('C is your Grade',n)
    elif n>81 and n<90:
        print('Your Grade is B,Good',n)
    elif n>91 and n<100:
        print('Your Scored a Great Deal, Excelent',n)

 Task#5

 n=int(input("entr a number="))
fact=1
if n<0:
    print("please enter positive number")
elif n==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("factorial is=",fact)
