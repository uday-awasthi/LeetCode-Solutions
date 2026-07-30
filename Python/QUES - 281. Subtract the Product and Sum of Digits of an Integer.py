QUES - 281. Subtract the Product and Sum of Digits of an Integer

Given an integer number n, return the difference between the product of its digits and the sum of its digits.

## SOLUTION 
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        sum_ = 0
        product = 1

        while temp>0:
            r = temp%10
            temp//=10
            sum_+=r
            product *=r

        return product-sum_

        
