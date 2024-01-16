class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        result = {} #Variable to store the result
        
        freq = [[] for i in range(len(nums) + 1 )] #[[], [], [], [], [], [], [], []]

        for i in nums:
            result[i]= 1 + result.get(i, 0) 
        for a, b in result.items():                 #value: [[], [0], [2], [], [1], [], [], []]
            freq[b].append(a)

        final = []
        for i in range(len(freq) -1, 0, -1): 
            for x in freq[i]:
                final.append(x)
                if len(final) == k:
                    return final

     
