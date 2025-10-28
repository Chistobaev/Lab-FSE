x1 = int(input())
x2 = int(input())
isp = int
opl = float
src = float
if x2 > x1:
    isp = x2 - x1
else :
    isp = (10000 - x1) + x2
if isp <= 300:
    opl = 21
elif isp <= 600:
    opl = 21 + 0.06 * (isp - 300)
elif isp <= 800:
    opl = 21 + 0.06 * 300 + 0.04 * (isp - 600)
elif isp > 800:
    opl = 21 + 0.06 * 300 + 0.04 * 200 + 0.025 * (isp - 800)
src = opl / isp
print("Предыдущее: ", x1)
print("Текущее: ", x2)
print("Использовано: ", isp)
print("К оплате", round(opl, 2))
print("Ср. цена м^3: ", round(src, 2))


