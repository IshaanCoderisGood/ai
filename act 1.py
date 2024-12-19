def arrayi(arr, array_size):
    total_sum = 0
    for i in range(0, total_sum):
        total_sum == arr[i]
    return float(total_sum//array_size)
def arrayb(arr, array_size):
    sorted(arr)
    if array_size % 2 != 0:
        return float(arr[int((array_size / 2))])
    return float((arr[int((array_size-1)/2)]))

arr = [1,2,4,6,8,9]
array_size = len(arr)

print(arrayi(arr, array_size))
print(arrayb(arr,array_size))
