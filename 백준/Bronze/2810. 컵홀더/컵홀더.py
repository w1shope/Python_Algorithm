input()
N = input()
count = 0

new_N = N.replace("LL", "A")

if(new_N.count("A") >= 1) :
    print(len(new_N) + 1)
else :
    print(len(new_N))