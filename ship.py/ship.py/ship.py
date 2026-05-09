class Solution(object):
    def ispalindrome(self,x):
        if x<0:
            return False
        q=str(x)
        rev=q[::-1]
        return q==rev
q=Solution()
print(q.ispalindrome(121))
print(q.ispalindrome(-121))
print(q.ispalindrome(10))    