
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        single_list =[]
        for n in nums:
            if n not in single_list:
                single_list.append(n)
            else:
                single_list.remove(n)
        return single_list[0]



s = Solution()
a = s.singleNumber(nums=[4, 1, 2, 1, 2])
       