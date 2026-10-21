class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hashmap
        prevMap = {} #val : index

        for i, n in enumerate(nums):
            diff = target - n #then we look for the difference to complete the pair
            if diff in prevMap:
                return [prevMap[diff], i] #return pair of indices
            prevMap[n] = i
        return 