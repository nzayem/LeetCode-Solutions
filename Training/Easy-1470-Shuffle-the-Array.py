# Shuffle the array
# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
	# Using extend is 2 times faster than append
            result.extend([nums[i], nums[i + n]])
        return result

