T = int(input())
button = {"A":0, "B":0, "C":0}
count = 0

while True :
    if(T == 0 or (T != 0 and T < 10)) :
        break

    if(T >= 600) :
        T -= 600
        button["A"] = button.get("A") + 1
    elif(T >= 60) :
        T -= 60
        button["B"] = button.get("B") + 1
    elif(T >= 10) :
        T -= 10
        button["C"] = button.get("C") + 1

if(T == 0) :
    for i in list(button.values()) :
        print(i, end=" ") 
else :
    print(-1)