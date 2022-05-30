class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count=0
        # for i in range(low, high+1):
        #     if i %2!=0:
        #         count+=1
        diff= high+1-low
        if diff%2==0:
            count= diff//2
        elif low%2!=0:
            count= diff//2 +1
        else:
            count= diff//2 
            
            
        return count
                