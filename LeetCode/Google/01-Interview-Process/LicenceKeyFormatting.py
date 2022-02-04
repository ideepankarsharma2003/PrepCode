# class Solution(object):
#     def licenseKeyFormatting(self, s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: str
#         """
#         modifyKey=''
        
#         return modifyKey

# obj = Solution()
# print(obj.licenseKeyFormatting(s="2-5g-3-J", k=2))

s = "2-5g-3-J"
k=2
modKey= ''
lMod=[]
s= s.replace('-', '')
s= s.upper()
# print(s)
# for i in range(len(s)-1, -1, -2):
#     r=''
#     r+=s[i-1:i+1]
#     lMod.append(r)
#     print(r)

# lst= [char for char in s]
# print(lst)
# for i in range(len(lst)-1, -1, -k):
#     r=''
#     r+=s[i-k+1:i+1]
#     print(r)

print(s[:1])
# print(lMod)