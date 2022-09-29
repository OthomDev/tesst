def large_gap(A):
    result = []
    A.sort()
    for i in range(len(A) - 1):
        result.append(A[i+1] - A[i])
    return max(result)

size = int(input("Enter the size of the array: "))
arr = []
for i in range(size):
    arr.append(int(input("Enter the element of the array, then press enter: ")))

print(large_gap(arr))


