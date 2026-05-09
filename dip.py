class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
obj = Solution()
nums1 = [1, 3, 5, 6]
target1 = 5
result1 = obj.searchInsert(nums1, target1)
print("Example 1")
print("Array:", nums1)
print("Target:", target1)
print("Output:", result1)
nums2 = [1, 3, 5, 6]
target2 = 2
result2 = obj.searchInsert(nums2, target2)
print("\nExample 2")
print("Array:", nums2)
print("Target:", target2)
print("Output:", result2)
nums3 = [1, 3, 5, 6]
target3 = 7
result3 = obj.searchInsert(nums3, target3)
print("\nExample 3")
print("Array:", nums3)
print("Target:", target3)
print("Output:", result3)