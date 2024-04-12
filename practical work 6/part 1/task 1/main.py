D = [1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
T = []

for i in range(1, len(D),2):
    T.append(D[i])
sumT = sum(T)
countT = len(T)
print(f"Массив D: {D}")
print(f"Массив T: {T}")
print(f"Сумма элементов в  T: {sumT}")
print(f"Количество элементов в T: {countT}")
