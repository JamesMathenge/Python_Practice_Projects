class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # Define the three keyboard rows
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        # List to store valid words
        result = []
        
        # Check each word
        for word in words:
            # Convert to lowercase and get unique characters
            word_chars = set(word.lower())
            
            # If word's characters are all in any one row, add to result
            if (word_chars.issubset(row1) or 
                word_chars.issubset(row2) or 
                word_chars.issubset(row3)):
                result.append(word)
        
        return result
    
# Create an instance of the Solution class
solution = Solution()

# Test cases
test1 = ["Hello","Alaska","Dad","Peace"]
test2 = ["omk"]
test3 = ["adsdf","sfd"]

# Run the tests using the class method
print("Test 1:", solution.findWords(test1))  # ["Alaska","Dad"]
print("Test 2:", solution.findWords(test2))  # []
print("Test 3:", solution.findWords(test3))  # ["adsdf","sfd"]