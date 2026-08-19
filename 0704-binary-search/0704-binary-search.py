class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left = 0
        # right = len(nums) - 1

        # while left <= right:
        #     mid = left +(right - left)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         left =  mid + 1
        #     else:
        #         right = mid - 1
        # return -1

        n = len(nums)

        l = 0
        r = n -1

        while l <=r:
            mid = l + (r - l) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                # right
                l = mid+1
            else:
                #left
                r = mid - 1

        return -1

            