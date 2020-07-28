class Solution:
    def majorityElement(self, nums) -> int:
        major = 0
        n = len(nums)
        count = 0
        for i in range(n):
            if count == 0:
                major = nums[i] 
                count = 1
            elif major == nums[i]:
                count += 1
            else:
                count -= 1
        return major
            