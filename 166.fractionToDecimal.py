class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        res = []
        if (numerator > 0) ^ (denominator > 0):
            res.append('-')
        numerator, denominator = abs(numerator), abs(denominator)
        a, b = divmod(numerator, denominator)
        res.append(str(a))
        if b == 0:
            return ''.join(res)
        res.append('.')
        loc = {b: len(res)}
        while b:
            b *= 10
            a, b = divmod(b, denominator)
            res.append(str(a))
            if b in loc:
                res.insert(loc[b], "(")
                res.append(')')
                break
            loc[b] = len(res)
        return ''.join(res)