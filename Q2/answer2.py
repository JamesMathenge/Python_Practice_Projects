class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Dictionary to store frequency of each number
        count = {}
        # Dictionary to store first occurrence of each number
        first = {}
        # Dictionary to store last occurrence of each number
        last = {}
        
        # Populate the dictionaries
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            count[num] = count.get(num, 0) + 1
        
        # Find the degree (maximum frequency)
        degree = max(count.values())
        
        # Find shortest subarray with same degree
        shortest = len(nums)
        for num in count:
            if count[num] == degree:
                # Length = last occurrence - first occurrence + 1
                curr_length = last[num] - first[num] + 1
                shortest = min(shortest, curr_length)
        
        return shortest

# Test cases
def test_solution():
    sol = Solution()
    
    # Test case 1
    nums1 = [1, 2, 2, 3, 1]
    print("Test 1:", sol.findShortestSubArray(nums1))  # Expected: 2
    
    # Test case 2
    nums2 = [1, 2, 2, 3, 1, 4, 2]
    print("Test 2:", sol.findShortestSubArray(nums2))  # Expected: 6
    
    # Additional test case
    nums3 = [1, 1, 1]
    print("Test 3:", sol.findShortestSubArray(nums3))  # Expected: 3

test_solution()