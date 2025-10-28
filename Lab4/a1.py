import random
import time

N = int(input("Введите количество примеров: "))
start_time1 = time.time()
p = int(0)
for i in range(N):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    while True:
        try:
            start_time = time.time()
            answer = int(input(f"{a} × {b} = "))
            time_spend = time.time() - start_time
            if answer != a*b:
                 print("Неверно! Верно: ", a*b, "Время(", time_spend, ")")
            else:
                print("Верно!", "Время(", time_spend, ")")
                p += 1
            break
        except ValueError:
         print("Пожалуйста, введите целое число!")

time_spend1 = time.time() - start_time1
print("СТАТИСТИКА\n", "Общее время:", time_spend1, "\nСреднее время на вопрос: ", time_spend1/N,
      "\nПравильных ответов:", p, "/", N, "\nПроцент правильных ответов: ", p/N*100)