## Напишите программу, которая принимает на вход координаты двух точек и находит расстояние
## между ними в 2D пространстве.

## Пример:

## - A (3,6); B (2,1) -> 5,09
## - A (7,-5); B (1,-1) -> 7,21


x1 = int(input("введите координаты x1\n"))
x2 = int(input("введите координаты x1\n"))
y1 = int(input("введите координаты y1\n"))
y2 = int(input("введите координаты y2\n"))

A = ((x1-y1)**2+(x2-y2)**2)**(0.5)
A = ('%.3f' % A)[:-1]
print(f'расстояние между точкой {x1,x2} и {y1,y2} равно {A}')