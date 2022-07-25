class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s= ''
        for i in digits:
            s+=str(i)
            
        print(s)
            
        s= int(s)
        print(s)

        s+=1
        s= str(s)
        print(s)
        l= [int(i) for i in s]
        print(l)
        return l