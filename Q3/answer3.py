class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Start from position 'a'
        current_pos = 'a'
        total_time = 0
        
        for char in word:
            # Calculate clockwise and counterclockwise distances
            dist1 = abs(ord(char) - ord(current_pos))
            dist2 = 26 - dist1
            
            # Take minimum of clockwise and counterclockwise movement
            moves = min(dist1, dist2)
            
            # Add movement time and typing time
            total_time += moves + 1  # +1 for typing the character
            
            # Update current position
            current_pos = char
            
        return total_time

def test_solution():
    sol = Solution()
    
    # Test case 1
    assert sol.minTimeToType("abc") == 5, "Test case 1 failed"
    print("Test 1: 'abc' ->", sol.minTimeToType("abc"))  # Expected: 5
    
    # Test case 2
    assert sol.minTimeToType("bza") == 7, "Test case 2 failed"
    print("Test 2: 'bza' ->", sol.minTimeToType("bza"))  # Expected: 7
    
    # Test case 3
    assert sol.minTimeToType("zjpc") == 34, "Test case 3 failed"
    print("Test 3: 'zjpc' ->", sol.minTimeToType("zjpc"))  # Expected: 34

test_solution()