class Solution:
    def removeElement(self, nums, val):
        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k]=nums[i]
                k += 1
        return k 
obj = Solution()
nums1 = [3, 2, 2, 3]
val1 = 3
k1 = obj.removeElement(nums1, val1)
print("Example 1")
print("Number of elements:", k1)
print("Updated array:", nums1[:k1])
nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
k2 = obj.removeElement(nums2, val2)
print("\nExample 2")
print("Number of elements:", k2)
print("Updated array:", nums2[:k2])    
        