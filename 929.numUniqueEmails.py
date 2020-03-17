from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        if not emails:
            return 0
        res = set()
        for email in emails:
            local, area = email.split('@')
            while '.' in local:
                dotIndex = local.index('.')
                local = local[:dotIndex]+local[dotIndex+1:]
            if '+' in local:
                addIndex = local.index('+')
                local = local[:addIndex]
            processedEmail = local + '@' + area
            res.add(processedEmail)
        return len(res)


s = Solution()
s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])