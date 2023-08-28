class Solution:
    def mergeTwoLists(self, list1: list, list2: list) -> list:
        for index,item1 in enumerate(list1):
            for item2 in list2:
                if item2 < item1:
                    list1.insert(index,item2)
                else: break
        return list1
    
sol = Solution()
sol.mergeTwoLists([1,2,3],[1,2,3])