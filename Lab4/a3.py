packets = input()
zero = int(0)
x = int(0)
if not all(char in '01' for char in packets):
 print("Неверный ввод. Используйте только символы '0' и '1'!")
print("Общее количество пакетов: ", len(packets))
print("Количество потерянных пакетов: ", packets.count('0'))
for i in range(0, len(packets)):
 if packets[i] == '0':
     zero += 1
 else:
     if zero > x:
         x = zero
     zero = 0
print ("Длина самой длинной последовательности потерянных пакетов: ", x)
proc = 100*packets.count('0')/len(packets)
print ("Процент потерь: ", proc, "%")
print("Качество связи: ", end='')
if proc <= 1:
    print("Отличное качество")
elif proc <= 5:
    print("Хорошее качество")
elif proc <= 10:
    print("Удовлетворительное качество")
elif proc <= 20:
    print("Плохое качество")
elif proc > 20:
    print("Критическое состояние сети")