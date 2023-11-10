from typing import List
def remove_element(nums: List[int], val: int) -> int:
    slow = 0
    for num in nums:
        if num != val:
            nums[slow] = num
            slow += 1 
            
    return slow


if __name__ == "__main__":
    nums = [2,2,2]
    val = 2
    print(remove_element(nums, val))
    print(nums)