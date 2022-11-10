# class Queue:
#     def __init__(self) -> None:
#         self.lst=[]
#     def is_empty(self):
#         return len(self.lst)==0
#     def enqueue(self, elem):
#         self.lst.append(elem)
#     def dequeue(self):
#         return self.lst.pop(0)
#     # def printq(self):
#     #     print(f'queue= {self.lst}')


def bfs(x, num):
    # q= Queue()
    q= []
    # q.enqueue(num)
    q.append(num)
    # l=[]
    maxnum= num
    while(not len(q)==0):
        num= q.pop(0)
        if num<=x:
            if num>maxnum:
                maxnum=num
            # l.append(num)
            last_digit= num%10
            if last_digit==0:
                q.append((num*10)+1)
            elif last_digit==9:
                q.append(num*10+8)
            else:
                q.append(num*10 + (last_digit-1))
                q.append(num*10 + (last_digit+1))
    # print(f'l= {l}', end=', ')
    # print(f'maxnum= {maxnum}')
    return maxnum
    
    
class Solution:
    def jumpingNums(self, X):
        # print (str(0), end =' ')
        # l= [0]
        maxnum= 0
        for i in range(1, 10):
            num=bfs(X, i)
            if num>maxnum:
                maxnum=num
        return maxnum
