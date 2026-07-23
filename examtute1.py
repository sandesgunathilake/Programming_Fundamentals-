
def linear_s(arr,target):
    position = -1
    index = 0
    while index < len(arr):
            if arr[index] ==  target:
                position = index
                break
        
        index=index+1
    return position

arr=[22,11,55,77,99,88,111]
target=55

x=linear_s(arr,target)
print(x)
if x == -1:
    print(f"The value is not found.")
else:
    print(f"The value is at {x} index.")
