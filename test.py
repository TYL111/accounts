class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        sum = []
        for x in range(0,len(nums)):
            zeros = 0
            ones = 0 
            for i in range(0,x):
                if nums[i] == 0:
                    zeros +=1 
            for j in range(x,len(nums)):
                if nums[j] == 1:
                    ones += 1  
            sum += f"{zeros+ones}"

        zeros = 0
        for x in range(0,len(nums)):
            if nums[x] == 0:
                zeros+=1
        sum += f"{zeros}"
        max_index = []
        for k in range(0,len(sum)):
            if sum[k] == max(sum):
               max_index+= f"{k}" 
        output = "["
        for x in max_
