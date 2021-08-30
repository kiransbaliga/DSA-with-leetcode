class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        cnt=0 # cnt is the number of patches
        summ=0 # summ is the total sum that can be reached from the elements in the array
        i=0 # i is the index of the current element
        m=len(nums)
        while summ<n:  # if the total sum is less than n, then we need to add more elements to the array
            if i >= m or nums[i] > summ+1: # if the current element is greater than the total sum, then we need to add more elements to the array
                summ += summ+1 # add the current element to the total sum
                cnt+=1 # add one patch
            else:
                summ += nums[i] # add the current element to the total sum
                i+=1 # move to the next element
        return cnt 
