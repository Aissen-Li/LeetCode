from typing import List
from fractions import Fraction
class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        def fractionCount(target, primes):
            count = 0
            left = -1
            largest = 0
            for right in range(1, len(primes)):
                while primes[left + 1] < primes[right] * target:
                    left += 1
                count += left + 1
                if left >= 0:
                    largest = max(largest, Fraction(primes[left], primes[right]))
            return count, largest
        
        low, high = 0.0, 1.0
        while high - low > 1e-9:
            mid = (low + high) / 2.0
            count, largest = fractionCount(mid, A)
            if count < K:
                low = mid
            else:
                high = mid
                res = largest
        return res.numerator, res.denominator