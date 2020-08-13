import time
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        start = time.mktime(time.strptime(date1,'%Y-%m-%d'))
        end = time.mktime(time.strptime(date2,'%Y-%m-%d'))
        if start > end:
            start, end = end, start
        return int((end - start)/(24*60*60))