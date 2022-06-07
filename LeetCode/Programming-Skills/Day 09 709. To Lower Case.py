class Solution:
    def toLowerCase(self, s: str) -> str:
        # return ''.join([i.lower() for i in s]) # One liner solution but not good
        sd = ''
        for i in s:
            if i.isupper():
                sd += chr(ord(i)+32)
            else:
                sd += i
        return sd
