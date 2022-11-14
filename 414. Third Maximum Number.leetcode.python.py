class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        check = list(set(nums))
        result = sorted(check, reverse= True)
        if(len(result) <3):
            return result[0]
        else:
            return result[2]