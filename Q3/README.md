# Minimum Time to Type Word on Special Typewriter

## Problem Description
Given a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer, determine the minimum time needed to type a given word. The pointer starts at 'a', and you can perform two types of operations, each taking one second:
1. Move the pointer one character clockwise or counterclockwise
2. Type the character the pointer is currently on

### Examples

#### Example 1
```
Input: word = "abc"
Output: 5
Explanation: 
- Type 'a' (1s)
- Move to 'b' (1s)
- Type 'b' (1s)
- Move to 'c' (1s)
- Type 'c' (1s)
Total = 5 seconds
```

#### Example 2
```
Input: word = "bza"
Output: 7
Explanation:
- Move to 'b' (1s)
- Type 'b' (1s)
- Move to 'z' (2s)
- Type 'z' (1s)
- Move to 'a' (1s)
- Type 'a' (1s)
Total = 7 seconds
```

## Solution Approach

### Algorithm
1. Start with pointer at 'a'
2. For each character in the word:
   - Calculate distance in both directions (clockwise and counterclockwise)
   - Choose minimum distance for movement
   - Add time for movement and typing (1 second per operation)
   - Update pointer position

### Implementation
```python
class Solution(object):
    def minTimeToType(self, word):
        current_pos = 'a'
        total_time = 0
        
        for char in word:
            # Calculate distances
            dist1 = abs(ord(char) - ord(current_pos))
            dist2 = 26 - dist1
            
            # Add minimum movement time plus typing time
            total_time += min(dist1, dist2) + 1
            current_pos = char
            
        return total_time
```

### Complexity Analysis
- Time Complexity: O(n) where n is the length of word
- Space Complexity: O(1) constant space

## Constraints
- 1 ≤ word.length ≤ 100
- word consists of lowercase English letters only

## Test Cases
```python
# Test Case 1
Input: "abc"
Expected Output: 5

# Test Case 2
Input: "bza"
Expected Output: 7

# Test Case 3
Input: "zjpc"
Expected Output: 34
```

## Key Points
1. The pointer can move in either direction
2. Each operation (move or type) takes exactly one second
3. Always choose the shortest path between two characters
4. The typewriter is circular (e.g., you can go from 'z' to 'a' in one move)
5. Initial position is always 'a'

## Tips for Solving
1. Use ASCII values (ord()) to calculate distances between characters
2. Remember to consider both clockwise and counterclockwise movements
3. Don't forget to include typing time (1 second per character)
4. Update current position after each character is typed

## Notes
- The solution requires understanding of circular distance calculation
- Edge cases include wrapping around from 'z' to 'a' or vice versa
- The answer is always deterministic for a given input