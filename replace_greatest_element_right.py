from typing import List
def replaceElements(arr: List[int]) -> List[int]:
    max, length = -1, len(arr) - 1 
    while length >= 0:
        if arr[length] > max:
            arr[length], max = max, arr[length]
        else:
            arr[length] = max
        length = length - 1
    return arr