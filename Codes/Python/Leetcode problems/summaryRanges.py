# Author: Sanket Dalvi
# Question Link: https://leetcode.com/problems/summary-ranges/


from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Check if list is empty
        if not len(nums): return []
        result = []
        start = 0
        difference = 1
        while start+difference < len(nums):
            if nums[start]+difference==nums[start+difference]:
                difference += 1
            elif difference==1:
                result.append(str(nums[start]))
                start += 1
                difference = 1
            else:
                result.append("{}->{}".format(nums[start], nums[start+difference-1]))
                start += difference
                difference = 1
        # Adding the last element
        if difference==1:
            result.append(str(nums[start]))
        else:
            result.append("{}->{}".format(nums[start], nums[start+difference-1]))
        return result


# Test case 1
print(Solution().summaryRanges([0,1,2,4,5,7]))
# Test case 2
print(Solution().summaryRanges([0,2,3,4,6,8,9]))