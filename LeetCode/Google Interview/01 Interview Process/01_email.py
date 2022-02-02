class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        l1 = []

        for email in emails:
            x = email.find("@")
            new_email01 = email[:x]
            new_email02 = email[x:]

            while '.' in new_email01:
                new_email01 = new_email01.replace('.', '')
            if '+' in new_email01:
                pp = new_email01.find('+')
                new_email01 = new_email01[:pp]

            if (new_email01+new_email02) not in l1:
                l1.append((new_email01+new_email02))

        return len(l1)
