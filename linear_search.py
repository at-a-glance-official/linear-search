def linear_search(arr,element):
    for i in range(len(arr)):
        if arr[i] == element:
            return f'Element found at index {i}'
    return 'Not Found!'

arr = [10,51,23,48,100,541,784,651,5700,1]
print(linear_search(arr,element=8845))