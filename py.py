class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1
        for i in range(n):
            j = 0            # j is the current length of the sequence
            while nums[i]!= -1: 
                temp = i   
                j+=1         # update j 
                i = nums[i]  # goes to nums[nums[i]]
                nums[temp] = -1 # mark visited
            res = max(res,j) 
        return res