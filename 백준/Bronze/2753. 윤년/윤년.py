year = int(input())

result = 0
if year % 4 == 0: # 4의 배수라면
    result = 1
    if year % 100 == 0 and year % 400 != 0: result = 0
print(result)