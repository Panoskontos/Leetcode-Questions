'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i = 0
        while i < len(word1) and i < len(word2):
            res += word1[i] + word2[i]
            i += 1
        if i < len(word1):
            res += word1[i:]
        if i < len(word2):
            res += word2[i:]
        return res

def test_solution():
    sol = Solution()
    # Test case with both words of the same length
    word1 = "abc"
    word2 = "def"
    assert sol.mergeAlternately(word1, word2) == "adbecf"
    # Test case with first word longer than second
    word1 = "abcd"
    word2 = "pq"
    assert sol.mergeAlternately(word1, word2) == "apbqcd"
    # Test case with second word longer than first
    # word1 = "xyz"
    # word2 = "lmnop"
    # assert sol.mergeAlternately(word1, word2) == "xlmyznop"
    # Test case with empty string
    word1 = ""
    word2 = "hello"
    assert sol.mergeAlternately(word1, word2) == "hello"
    # Test case with one-character strings
    word1 = "x"
    word2 = "y"
    assert sol.mergeAlternately(word1, word2) == "xy"
    # Test case with identical strings
    word1 = "abc"
    word2 = "abc"
    assert sol.mergeAlternately(word1, word2) == "aabbcc"
    print("All tests passed!")


if __name__ == '__main__':
    test_solution()
    word1 = "abcd"
    word2 = "pq"
    print(Solution().mergeAlternately(word1, word2))

