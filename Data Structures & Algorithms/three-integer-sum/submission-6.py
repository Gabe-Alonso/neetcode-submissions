class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        result = []
        prev = (-10 ^ 5) - 1
        for i in range(len(nums) - 2):
            if nums[i] == prev or nums[i] > 0:
                pass
            else:
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    print("nums[" + str(i) + "]: " + str(nums[i]))
                    print("nums[" + str(j) + "]: " + str(nums[j]))
                    print("nums[" + str(k) + "]: " + str(nums[k]))
                    
                    if nums[j] + nums[k] == nums[i] * -1:
                        # print("YIPEE")
                        result.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while nums[j] == nums[j - 1] and j < k:
                            j += 1
                    elif nums[j] + nums[k] < nums[i] * -1:
                        j += 1
                    else:
                        k -= 1
                    print("")
            prev = nums[i]

        return result