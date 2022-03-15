
#problem1
a = 2**3
b = 3**2
if a>b:
    print('Будет больше: 3**2')
else:
    print('Больше будет: 2**3')

#problem2
a = int(input('num1: '))
b = int(input('num2: '))
c = int(input('num3: '))
if a > b > c:
    print('num1, num3')
elif a > c > b:
    print('num1, num2')
elif b > a > c:
    print('num2, num3')
elif b > c > a:
    print('num2,num1')
elif c > a > b:
    print('num3, num2')
elif a < b < c:
    print('num3, num1')
else:
    print('Error')

#problem3
a = 17391
b = 546
c = 934
num1 = a % 17
num2 = b % 17
num3 = c % 17
if a<b and a<c:
    print(a,num1)
elif b<a and b<c:
    print(b,num2)
elif c<a and c<b:
    print(c,num3)
else:
    print('Error')

#problem4
x = 13
x = x**2
if x <= 172:
    x=x**2
print(x)

#problem5
a=int(input('Write a number: '))
if a%2 == 0 and a%3==0 and a**2>1000:
    print('Correct number')
else:
    print('Incorrect number')

#problem6
a = int(input('Write numbers (0-100):  '))
if 0<=a<21 or 57<=a<100:
    print('Yeah!')
else:
    print('Nope!')

#problem7
a=5.0
b=5
if a == b:
    print('Nice!')
else:
    print('Bad')

#problem8
a=1
b=1.0
c=1.1
if a==b:
    if a<c:
        if b<c:
            print('True')
else:
    print('False')

#problem9
a=10//5
b=10/5
if a == b:
    print(f'{a+b}')
else:
    print('Oh no...')

#problem10
a=int(input('Напишите отрицательное число: '))
if a<0:
    print('Да это отрицательное число')
else:
    print('Нет это не отрицательное число')

#problem11
a=10
b=5
if a>0 and b>0:
    print("It's true")
else:
    print('NOOO')

#problem12
a=10
b=5
if a>b:
    print(a+2)
else:
    print(b+2)

