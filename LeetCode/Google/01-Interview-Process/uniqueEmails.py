from signal import SIG_DFL


def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        count= 0
        for email in emails:
            