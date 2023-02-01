class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        s = set()
        count=0
        for email in emails:
            ind = email.index('@')
            name = email[:ind]
            domain = email[ind:]
            name = name.replace('.', '')
            if '+' in name:
                pInd = name.index('+')
                name = name[:pInd]
            email = name+domain
            if email not in s:
                s.add(email)
                # print(email)
                count+=1
        # print(count)
        return count



emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
obj = Solution()
obj.numUniqueEmails(emails)

