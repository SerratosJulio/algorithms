class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean = ''

        if len(s) == 1:
            return True
        else:
            for i in s:
                if i.isalnum():
                    clean += i.lower()


        #temp = s.replace(" ", "").replace(",","").replace(":","").replace(".","")
        #clean = temp.lower()
        
        
        l, r = 0, len(clean) - 1

        while l < r:
            if clean[l] != clean[r]:
                return False
            l += 1
            r -= 1
            
        return True
        

