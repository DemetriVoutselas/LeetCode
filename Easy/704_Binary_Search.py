class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums)
        c = (a+b)//2

        while target != nums[c]:
            if c == a:
                return -1
            if target > nums[c]:
                a = c
                c = (a+b)//2
            else:
                b = c
                c = (a+b)//2
        return c
