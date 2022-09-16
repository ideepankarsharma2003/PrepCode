class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        original= []
        changed.sort()
        l= len(changed)
        
        if l%2!=0: 
            return []
        
        d= Counter(changed)
        print(d)
        
        for i in changed:
            if i==0 and d[i]>=2:
                original.append(i)
                d[i]-=2
                
            elif i>0 and d[i]>0 and d[i*2]>0:
                d[i]-=1
                d[i*2]-=1
                original.append(i)
        
        if len(original)==l//2:
            return original
        else:
            return []
