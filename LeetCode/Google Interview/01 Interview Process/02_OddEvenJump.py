def largest(arr):
    l1 =arr
    l1.sort()
    return (l1[-1])

def smallest(arr):
    l1 =arr
    l1.sort()
    return (l1[0])


class Solution(object):
    def oddEvenJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # arr = [2, 3, 1, 1, 4]
        jumps=0
        for m in range(len(arr)): # all the elements of the list
            for j in range(m, len(arr)):
                i=m # counter for jumps
                while(i>=len(arr)-1):
                    if i%2==0:
                        if (i+1)==arr.find(largest(arr[i:])) and arr[i]>=arr[j]

            
        
        return jumps
                
