def is_Disarium(N):
    arr = []
    j = 1
    Count = 0
    for i in range(len(N)):
        arr.append(int(N[i])**j)
        j = j + 1
    for i in range(len(arr)):
        Count = Count + arr[i]
    
    if Count == int(N) :
        return True
    else:
        return False




Number = int(input("Please enter the number: "))
Number = str(Number)

print(is_Disarium(Number))

