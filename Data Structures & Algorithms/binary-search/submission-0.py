class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        l = 0
        r = len(nums) - 1
        ll = l
        rr = r
        while l != r:
            ll = l
            rr = r
            #print("L: " + str(l))
            #print("R: " + str(r))
            i = (l + r) // 2
            #print(i)
            #print(nums[i])
            if nums[i] == target:
                return i
            elif (l + r) % 2 == 1 and nums[i + 1] == target:
                return i + 1
            if target < nums[i]:
                r = i
            else:
                l = i
            if l == ll and r == rr:
                return result

        if len(nums) == 1 and nums[0] == target:
            return 0
        return result