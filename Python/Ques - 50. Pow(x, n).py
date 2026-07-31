Ques - 50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

## SOLUTION 


class Solution:
    def findPow(self, x, n):
        # Base case
        if n == 0:
            return 1

        # Recursive call
        a = self.findPow(x, n // 2)

        if n % 2 == 0:
            return a * a
        else:
            return a * a * x

    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            return self.findPow(x, n)
        else:
            return 1 / self.findPow(x, -n)
