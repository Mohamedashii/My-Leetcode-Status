
class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        count = 0

        while any(nums[i] > nums[i+1] for i in range(len(nums)-1)):
            i = min(range(len(nums)-1), key=lambda i: nums[i] + nums[i+1])
            nums[i] += nums[i+1]
            nums.pop(i+1)
            count += 1

        return count

