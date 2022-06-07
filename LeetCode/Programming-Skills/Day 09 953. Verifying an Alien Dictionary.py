class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        #         def check(w1, w2, order):
        #             pass

        #         for i in range(len(words)-1):
        #             w1= words[i]
        #             w2= words[i+1]
        #             l= check(w1, w2, order)
        #             if not l:
        #                 return False
        #         return True

        return sorted(words, key=lambda x: [order.index(c) for c in x]) == words
