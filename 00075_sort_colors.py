from typing import List

def sortColors(nums: List[int]) -> None:
    bucket: dict = { 0: 0,
                     1: 0,
                     2: 0
                 }  
    
    for num in nums:
        bucket[num] += 1

    j = 0
    
    for key in bucket:
        for i in range(0, bucket[key]):
            nums[j] = key
            j += 1

colors_list: list[int] = [2,0,2,1,1,0]

sortColors(colors_list)

print(colors_list)

