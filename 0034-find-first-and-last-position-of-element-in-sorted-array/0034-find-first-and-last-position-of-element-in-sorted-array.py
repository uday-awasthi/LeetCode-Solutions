class Solution:
    def searchRange(self, nums, target):
        
        def lower_bound(x):
            l, r = 0, len(nums)
            
            while l < r:
                mid = (l + r) // 2
                
                if nums[mid] < x:
                    l = mid + 1
                else:
                    r = mid
                    
            return l

        def upper_bound(x):
            l, r = 0, len(nums)
            
            while l < r:
                mid = (l + r) // 2
                
                if nums[mid] <= x:
                    l = mid + 1
                else:
                    r = mid
                    
            return l

        first = lower_bound(target)
        last = upper_bound(target) - 1

        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        return [first, last]