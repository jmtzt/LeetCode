class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_arr = nums[0]
        curr_sum = nums[0]
        for num in nums[1:]:
            if curr_sum < 0:
                curr_sum = num
            else:
                curr_sum += num
            if curr_sum > max_arr:
                max_arr = curr_sum
        return max_arr
