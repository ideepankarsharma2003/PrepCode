class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        l= [str(i) for i in num]
        s= ''.join(l)
        s= str(int(s)+k)
        l= [int(i) for i in s]
        print(l)
        return l
        