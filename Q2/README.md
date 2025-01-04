# Degree of Array Problem

## Problem Description
Given a non-empty array of non-negative integers, find the shortest contiguous subarray that has the same degree as the original array.

The **degree** of an array is defined as the maximum frequency of any element in the array.

### Examples

#### Example 1
```
Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
- Array has degree 2 (both elements 1 and 2 appear twice)
- Possible subarrays with same degree:
  * [1,2,2,3,1]  Length: 5
  * [1,2,2,3]    Length: 4
  * [2,2,3,1]    Length: 4
  * [1,2,2]      Length: 3
  * [2,2,3]      Length: 3
  * [2,2]        Length: 2
- Shortest length is 2
```

#### Example 2
```
Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation:
- Degree is 3 (element 2 appears three times)
- Shortest subarray containing all 2's: [2,2,3,1,4,2]
- Length is 6
```

## Solution Approach

### Algorithm
1. Create three dictionaries to track:
   - Count: frequency of each number
   - First: first occurrence index of each number
   - Last: last occurrence index of each number

2. Find the degree (maximum frequency) of the array

3. For each number with frequency equal to degree:
   - Calculate subarray length (last index - first index + 1)
   - Keep track of minimum length found

### Code Implementation
```python
class Solution(object):
    def findShortestSubArray(self, nums):
        count = {}
        first = {}
        last = {}
        
        # Track frequencies and positions
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            count[num] = count.get(num, 0) + 1
        
        # Find shortest subarray
        degree = max(count.values())
        shortest = len(nums)
        for num in count:
            if count[num] == degree:
                curr_length = last[num] - first[num] + 1
                shortest = min(shortest, curr_length)
        
        return shortest
```

### Complexity Analysis
- Time Complexity: O(n) where n is the length of input array
- Space Complexity: O(k) where k is number of unique elements

## Constraints
- 1 ≤ nums.length ≤ 50,000
- 0 ≤ nums[i] ≤ 49,999

## Test Cases
```python
# Test Case 1
nums = [1,2,2,3,1]
Expected Output: 2

# Test Case 2
nums = [1,2,2,3,1,4,2]
Expected Output: 6

# Test Case 3
nums = [1,1,1]
Expected Output: 3
```

## Additional Notes
- The solution requires only a single pass through the array
- Multiple elements might share the maximum frequency
- The shortest subarray must be contiguous
- Empty arrays are not possible according to constraints