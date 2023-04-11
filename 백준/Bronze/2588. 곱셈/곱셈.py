num_1 = int(input())
num_2 = list(map(int, input()))

a = num_1 * num_2[2]  # 1의자리 계산
b = num_1 * num_2[1]  # 10의자리 계산
c = num_1 * num_2[0]  # 100의자리 계산

print(a)
print(b)
print(c)
print(a + (b * 10) + (c * 100))