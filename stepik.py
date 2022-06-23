'''zumspeed, flashspeed = int(input()), int(input())

if zumspeed > flashspeed:
    print('NO')
elif flashspeed > zumspeed:
    print('YES')
else:
    print("Don't know")
'''

# Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого равны введенным числам

a, b, c =int(input()),int(input()),int(input())

if a == b or a == c or b == c:
    print('Равнобедренный')
elif a == b == c:
    print('Равносторонний')
else:
    print('Разносторонний')