class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[hi]:
                if target >= nums[mid] and target <= nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1
            else:
                if target >= nums[lo] and target <= nums[mid]:
                    hi = mid-1
                else:
                    lo = mid+1
        return -1