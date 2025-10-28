n = int(input())
m = int(input())
def pr(a, b):
 for i in range(a):
    for j in range(b):
        print('#', end='')
    print("")
def tr(a, b):
 for i in range(a):
     for j in range(b):
      if j <= i:
       print('#', end='')
     print("")
def ramka(a, b):
 for i in range(a):
    for j in range(b):
      if i == 0 or j == 0 or i == a-1 or j == b-1:
          print('#', end='')
      elif i > 1 or j != b - 1:
          print(' ', end='')
    print("")
#Основа:
print("ПРЯМОУГОЛЬНИК ", n, "x", m)
pr(n,m)
print("ПРАВЫЙ ТРЕУГОЛЬНИК")
tr(n,m)
print("РАМКА ", n, "x", m)
ramka(n,m)