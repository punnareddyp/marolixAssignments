def max_number(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
                if not swapped:
                    break
lst=[8,6,66,3,44,33,48,90,28]
max_number(lst)
print("sorted list:",lst)
print(lst[-1])