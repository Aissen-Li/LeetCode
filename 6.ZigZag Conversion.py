class Solution:
    def convert(self, s, numRows):
        out = ['' for i in range(numRows)]
        t = 0
        while t < len(s):
            for i in range(0, numRows):
                out[i] += s[t]
                t += 1
                if t == len(s):
                    break
            if t == len(s):
                break
            for i in range(numRows-2, 0, -1):
                out[i] += s[t]
                t += 1
                if t == len(s):
                    break
        res = ''.join(out)
        return res


"""把输出分为行，正着输入numrows个数字，然后倒着从倒数第二行输入到正数第二行"""


class Solution2:
    def convert(self, s, numRows):
        str_length = len(s)
        node_length = 2*numRows - 2  # 两列之间的差
        result = ""

        if str_length == 0 or numRows == 0 or numRows == 1:
            return s

        for i in range(numRows):  # 从第一行遍历到最后一行
            for j in range(i, str_length, node_length):
                result += s[j]  # 第一行和最后一行  还有普通行的整列数字
                if i != 0 and i != numRows-1 and j - 2*i + node_length < str_length:
                    result += s[j-2*i+node_length]  # 单列行的数字
        return result


"""找规律，直接得到每一行数字之间的关系，除了第一行和最后一行以外，需要额外添加斜边上的数s[j-2*i+node_length]"""

