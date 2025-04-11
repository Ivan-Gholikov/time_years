months = 2

if months not in range(1,13):
    print("Некорректный месяц")
elif months in (1,2,12):
    print('Зима')
elif months in (3,4,5):
    print("Весна")
elif months in (6,7,8):
    print("Лето")
elif months in (9,10,11):
    print("Осень")
    