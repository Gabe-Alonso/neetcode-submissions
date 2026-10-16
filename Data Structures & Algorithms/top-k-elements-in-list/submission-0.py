class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        for i in range(len(nums)):
            if nums[i] in elements:
                elements[nums[i]] += 1
            else:
                elements[nums[i]] = 1
        freq_tab = [[] for _ in range(len(nums))]
        for num, freq in elements.items():
            freq_tab[freq - 1].append(num)
        i = len(nums) - 1
        j = 0
        top = []
        while k > 0:
            #print(freq_tab[i])
            while j < len(freq_tab[i]):
                top.append(freq_tab[i][j])
                j += 1
                k -= 1
                if k <= 0:
                    return top
            i -= 1
            j = 0
        return top