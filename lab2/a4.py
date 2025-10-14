a = int(input ("Введите первое число а: "))
b = int(input ("Введите второе число b: "))
if a<=0 or a>1000 or b<=0 or b>1000:
    print ("Допустимы числа лежащие в диапазоне от 1 до 1000")

else :
    result = "Числа равны" if a == b else "Числа не равны"
    print ("result")
    result = [a, b][a <= b]
    print("Наибольшее число:", result)


