class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while numbers[l] + numbers[r] != target and l < r:
            print("l[" + str(l) + "] : " + str(numbers[l]) + ", r[" + str(r) + "] : " + str(numbers[r]))
            if numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
            print("Current sum is " + str(numbers[l] + numbers[r]))
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            
        return [l + 1, r + 1]