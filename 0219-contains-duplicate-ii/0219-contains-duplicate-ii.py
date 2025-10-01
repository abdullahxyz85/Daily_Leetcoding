class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}

        for i in range(len(nums)):
            num = nums[i]

            if num in last_seen:
                if i - last_seen[num] <= k:
                    return True

            last_seen[num] = i

        return False
