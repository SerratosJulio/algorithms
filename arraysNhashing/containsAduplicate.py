class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        #Using a hashset {}, hashset does not allow duplicates

        my_set = set()

        for i in nums:
            if i in my_set:
                return True
            my_set.add(i)
        
        return False

    


        