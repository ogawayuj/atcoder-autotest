line = list(map(int, input().split()))
multi = line[0] * line[1]
if multi % 2 == 1 :
    print("Odd")
else :
    print("Even")
