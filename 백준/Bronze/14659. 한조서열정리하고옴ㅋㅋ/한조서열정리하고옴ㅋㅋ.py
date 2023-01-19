N = int(input())

player = [int(i) for i in input().split()]
play_score = list()
for i in range(len(player)) : 
    score = 0
    for j in range(i, len(player)) :
        if(player[i] > player[j]) :
            score += 1
        elif(player[i] < player[j]) :
            break
    play_score.append(score)

print(max(play_score))