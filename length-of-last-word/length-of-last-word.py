class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split the string into segments
        s = s.split(" ")
        # filter out any empty segments
        s = list(filter(None, s))
        if len(s) == 0: return 0
        return len(s[-1])