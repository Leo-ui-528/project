s = int(input("Введите время в секундах: "))
h = str(s // 3600)
m = str(s // 60)
s = str(s % 60)
print(h + ':' + m + ':'+s)
