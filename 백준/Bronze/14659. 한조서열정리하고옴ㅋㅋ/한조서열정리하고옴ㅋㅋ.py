import sys

N = int(sys.stdin.readline())

player = [int(i) for i in sys.stdin.readline().split()] 
best_score = 0
for i in range(N) : 
    # 현재 활잡이가 처치한 적의 수 > 남은 활잡이 수이면 더 이상 탐색할 필요가 없다
    if(len(range(i, N)) <= best_score) :
        break
    score = 0
    for j in range(i, N) :
        if(player[i] > player[j]) :
            score += 1
        elif(player[i] < player[j]) :
            break
    best_score = max(best_score, score)

print(best_score)
