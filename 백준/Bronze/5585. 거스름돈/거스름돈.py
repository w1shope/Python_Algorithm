change = 1000 - int(input())  # 거스름돈

coin = [500, 100, 50, 10, 5, 1] # 거스름돈을 지불할 동전, 내림차순 정렬
count = 0

for i in coin :
    count += (change // i)
    change %= i

print(count)