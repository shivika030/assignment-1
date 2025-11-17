'''
NAME: SHIVIKA BHAWSAR
ENROLLMENT NO. : 0176CD231134
BATCH: 5
BATCH TIME: 10:30 - 12:10
'''

#IF-ELSE

#Q1: check positive, negative or zero

a=int(input("enter no"))
if a==0:
  print("zero")
elif a>0:
  print("positive no")
else:
  print("negative no")    

#Q2: Write a program to check whether a number is even or odd.

a=int(input("enter no"))
if a%2 == 0:
  print("even no")
else:
  print("odd no")  

#Q3: Write a program to check if a given year is a leap year or not.

a=int(input("enter year"))
if a%4 == 0:
  if a%100 == 0:
    if a%400 == 0:
      print(f"{a} is a leap year")
    else:
      print(f"{a} is not a leap year")
  else:
    print(f"{a} is a leap year")    
else:
  print(f"{a} is not a leap year")   
  

#Q4: Write a program to find the greatest of two numbers.

a=int(input("enter no 1"))
b=int(input("enter no 2"))
if a>b:
  print(f"{a} is greater")
else:
  print(f"{b} is greater")  


#Q5: Write a program to check whether a person is eligible to vote (age >= 18).

a=int(input("enter age"))
if a>=18:
  print("eligible to vote")
else:
  print("not eligible")
  

#Q6: Write a program to check whether a given character is a vowel or consonant.

a=input("enter character: ").lower()
if a in "aeiou":
  print(f"{a} is a vowel")
else:
  print(f"{a} is a consonent")  
  

#Q7:Write a program to check if a number is divisible by 5.

a=int(input("enter no"))
if a%5 ==0:
  print("no is divible by 5")
else:
  print("no is not divisible by 5")  


#Q8: Write a program to determine whether a given number is a single-digit, two-digit, or more than two-digit

a=int(input("enter no"))
if a<10:
  print("single digit no") 
elif a<100:
  print("two digit no")  
else:
  print("more than two digit no")  
  

#Q9: Write a program to check whether a student has passed or failed (passing marks = 40).

a=int(input("enter marks"))
if a>=40:
  print("pass")
else:
  print("failed")  
  

#Q10: Write a program to find whether the entered number is a multiple of both 3 and 7.

a=int(input("enter no"))
if a%3 == 0 and a%7 == 0:
  print(f"{a} is multiple of both 3 and 7")
else:
  print(f"{a} is not a multiple of both 3 and 7")


 # LADDER IF AND NESTED IF 
  

#Q1:Write a program to find the greatest among three numbers.

a=int(input("enter no 1"))
b=int(input("enter no 2"))
c=int(input("enter no 3"))
if a>=b and a>=c:
  print(f"{a} is greatest")
elif b>=a and b>=c:
  print(f"{b} is greatest")
else:
  print(f"{c} is greatest")
  

#Q2: Write a program to classify a person based on age: Child (<13), Teenager (13-19), Adult (20-59), Senior (60+).

a=int(input("enter age"))
if a<13:
  print("child")
elif a<=19:
  print("teenager")
elif a<=59:
  print("adult")
else:
  print("senior")


#Q3: Write a program to assign grades based on marks:90-100: A,75-89: B,50-74: C,35-49: D,<35: Fail.

a=int(input("enter marks"))
if a>=90 and a<=100:
  print("A grade")
elif a>=75 and a<=89:
  print("B grade")  
elif a>=50 and a<=74:
  print("C grade")
elif a>=35 and a<=49:
  print("D grade")
else:
  print("Fail")


#Q4: Write a program to check the type of triangle (equilateral, isosceles, or scalene) based on sides.

a=int(input("enter side 1"))
b=int(input("enter side 2"))
c=int(input("enter side 3"))
if a==b and b==c:
  print("equilateral triangle")
elif a==b or b==c or a==c:
  print("isosceles triangle")
else:
  print("scalene triangle")


#Q5: Write a program to check if a character is uppercase, lowercase, digit, or special symbol.

a=input("enter character")
if a>='A' and a<='Z':
  print(f"{a} is uppercase")
elif a>='a' and a<='z':
  print(f"{a} is lowercase")
elif a>='0' and a<='9':
  print(f"{a} is digit")
else:
  print(f"{a} is special symbol")
  

#Q6: Write a program to calculate electricity bill based on units:Up to 100 units: ₹5 per unit,101–200 units: ₹7 per unit,Above 200 units: ₹10 per unit.

a=int(input("enter units"))
if a<=100:
  bill=a*5
elif a<=200:
  bill=a*7
else:
  bill=a*10
print(f"electricity bill is {bill}")


#Q7: Write a program to determine the largest of four numbers using nested if.

a=int(input("enter no 1"))
b=int(input("enter no 2"))
c=int(input("enter no 3"))  
d=int(input("enter no 4"))
if a>=b and a>=c and a>=d:
  print(f"{a} is greatest")
elif b>=a and b>=c and b>=d:
  print(f"{b} is greatest")
elif c>=a and c>=b and c>=d:
  print(f"{c} is greatest")
else:
  print(f"{d} is greatest")
  

#Q8: Write a program to check if a given year is a century year and also a leap year.

a=int(input("enter year"))
if a%100 == 0:
  if a%400 == 0:
    print(f"{a} is a century leap year")
  else:
    print(f"{a} is a century year but not a leap year")
else:
  print(f"{a} is not a century year")
  

#Q9: Write a program to classify BMI value: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9),Obese (30+).

a=float(input("enter bmi value"))
if a<18.5:
  print("underweight")
elif a<=24.9:
  print("normal")
elif a<=29.9:
  print("overweight")
else:
  print("obese")
  

#Q10: wap to check smallest no among three using nested if

a=int(input("enter no 1"))
b=int(input("enter no 2"))
c=int(input("enter no 3"))
if a<=b and a<=c:
  print(f"{a} is smallest")
elif b<=a and b<=c:
  print(f"{b} is smallest")
else:
  print(f"{c} is smallest")


#FOR LOOP
  

#Q1: Write a program using a for loop to print all Armstrong numbers between 100 and 999. (Armstrong number:sum of cubes of digits equals the number itself. Example: 153 => 13+53+33 = 153).

a=float(input("enter no"))
b=len(str(a))
aa=a
c=0
for i in range(b):
  d=a%10
  c+=d**3
  a=a//10
if c==aa:
  print("armstrong no")
else:
  print("not armstrong no")  
  

#Q2: Write a program to generate and display the first n prime numbers using a for loop.

a=int(input("enter n value"))
s=0
while s==a:
  for i in range(2,a//2):
    if a%i == 0:
      print("not prime no")
      break
  else:
    print("prime no")


#Q3: Write a program to display all numbers from 1 to 500 that are divisible by 3, but the sum of their digits should not exceed 10.


for i in range(1,501):
  if i%3==0:
    c=0
    ii=i
    while ii>0:
      d=ii%10
      c+=d
      ii=ii//10
    if c<=10:
      print(i)  


#Q4: Write a program using a for loop to print a pyramid of stars (*) of height n. Example for n=4:

n=int(input("enter height of pyramid"))
for i in range(n):
  print(" "*(n-i-1)+"*"*(2*i+1))
      

#Q5: Write a program to accept a string and check whether it is a pangram (contains all 26 alphabets at least once) using a for loop.

a=(input("enter string")).lower()
f=0
for i in "abcdefghijklmnopqrstuvwxyz":
  if i in a:
    f=f+1
if f==26:
  print("its a pangram") 
else:
  print("its not a pangram")     
  

#Q6: 

#Q7:Write a program that accepts a number from the user and prints whether it is a Harshad number (number divisible by the sum of its digits) using a for loop.

a=int(input("enter no"))
b=len(str(a))
aa=a
c=0
for i in range(b):
  d=a%10
  c+=d 
  a=a//10
if aa%c == 0:
  print(f"{aa} is a harshad no")  
else:
  print(f"{aa} is not a harshad no")   
  

#Q8: 

#Q9: Write a program using a for loop to display the sum of the series: 12 + 22 + 32 + ... + n2

l=int(input("enter limit"))
s=0
for i in range(1,l+1):
  s+=i*i
print(f"sum of series of squares is {s}")


#Q10: Write a program that accepts a number from the user and prints whether it is a Strong number (sum of factorials of digits = number itself) using a for loop. Example: 145 => 1! + 4! + 5! = 145.

no=int(input("enter no"))
b=len(str(no))
aa=no
c=0
for i in range(b):
  d=no%10
  s=1
  for j in range(d,0,-1):
    s=s*j
  c+=s 
  no=no//10
if aa==c:
  print(f"{aa} is a strong no")  
else:
  print(f"{aa} is not a strong no") 
  


#WHILE LOOP

#Q11: Write a program using a while loop to find the reverse of a number and check if the reversed number is prime. Example: Input = 73 → Reverse = 37 → Prime.

a=int(input("enter no: "))
aa=a
c=0
while a>0:
    d=a%10
    c=(c*10)+d
    a=a//10
f=0
i=2
while i<=c//2:
    if c%i==0:
        f=1
        break
    i=i+1
if f==1:
    print(f"reverse of {aa}={c} is not a prime no")
else:
    print(f"reverse of {aa}={c} is a prime no")
  

#Q12: Write a program that continues to accept numbers from the user until the sum of digits of all numbers entered becomes greater than 100.

a=0
while a<=100:
  no=int(input("enter no"))
  a=a+no
  print(f"sum is {a}")
print("limit exceeded")


#Q13: Write a program using a while loop to check whether a number is a Duck number (a number containing zero but not starting with zero, e.g., 202, 1203).

no=int(input("enter no"))
nno=no
f=0
while no>0:
  d=no%10
  no=no//10
  if d==0:
    f=1
    break
if f==1:
  print(f"{nno} is a duck no")
else:
  print(f"{nno} is not a duck no")  


#Q14: Write a program using a while loop to accept a number and check if it is a Happy number. (A number is happy if repeatedly replacing it with the sum of squares of its digits eventually reaches 1). Example: 19 is a happy number.

a=int(input("enter no"))
aa=a
while a!=1:
  c=0
  no=a
  while no>0:
    d=no%10
    c+=d**2
    no=no//10
    print(c)
  a=c
if a==1:
  print(f"{aa} is happy no")
else:
  print(f"{aa} is not happy no")   

  
#Q15: Write a program using a while loop to find the largest prime factor of a given number.

a=int(input("enter no"))
aa=a
i=2
while a>1:
  if a%i == 0:
    a=a//i
  else:
    i=i+1
print(f"largest prime factor of {aa} is {i}")    
  

#Q16: Write a program to repeatedly accept a string from the user until the string entered is a palindrome.

f=1
while f==1:
  sttr=input("enter string")
  rev=sttr[::-1]
  if sttr==rev:
    f=0
    break
if f==0:
  print(f"{sttr} is a palindrome")
  

#Q17:Write a program using a while loop to compute the sum of digits of a number until the result becomes a single-digit number (Digital root). Example: 9875 => 9+8+7+5=29 => 2+9=11 => 1+1=2.

a=int(input("enter no"))
while a>9:
  c=0
  while a>0:
    d=a%10
    c+=d
    a=a//10
  a=c
  print(c)
  

#Q18: Write a program using a while loop to generate the Collatz sequence for a given number. (Rule: If n is even => n/2, if odd => 3n+1. Continue until n=1).

a=int(input("enter no"))
while a>1:
  if a%2 == 0:
    a=a//2
  else:
    a=3*a+1
  print(a)    
  

#Q19: Write a program using a while loop to accept a number and check whether it is a Kaprekar number.(Kaprekar number: if square of the number can be split into two parts whose sum equals the number.Example: 452=2025 => 20+25=45).

i=int(input("enter no"))
ii=i
i=i*i
st=str(i)
mid=len((st))//2
out=int(st[:mid])+int(st[mid:])
if out==ii:
  print(f"{ii} is a kaprekar no")
else:
  print(f"{ii} is not a kaprekar no")


#Q20: Write a program to simulate an ATM machine using a while loop where a user can:• Check balance• Deposit money• Withdraw money (only if balance is sufficient)• ExitContinue until the user chooses to exit.

balance=1000
while True:
  print("1. check balance")
  print("2. deposit money")
  print("3. withdraw money")
  print("4. exit")
  choice=int(input("enter your choice"))
  if choice==1:
    print(f"your balance is {balance}")
  elif choice==2:
    amount=int(input("enter amount to deposit"))
    balance=balance+amount
    print(f"your new balance is {balance}")
  elif choice==3:
    amount=int(input("enter amount to withdraw"))
    if amount<=balance:
      balance=balance-amount
      print(f"your new balance is {balance}")
    else:
      print("insufficient balance")
  elif choice==4:
    print("thankyou for using our services")
    break
  else:
    print("invalid choice")


