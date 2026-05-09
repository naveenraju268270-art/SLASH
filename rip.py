class Solution:
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x
        left = 1
        right = x
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
obj = Solution()
x1 = 4
result1 = obj.mySqrt(x1)
print("Example 1")
print("Input:", x1)
print("Output:", result1)
x2 = 8
result2 = obj.mySqrt(x2)
print("\nExample 2")
print("Input:", x2)
print("Output:", result2)