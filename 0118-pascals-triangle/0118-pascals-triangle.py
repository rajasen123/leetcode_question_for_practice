class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []
        for i in range(numRows):
            row = []
            ans = 1
            for j in range(i + 1):
                if j == 0:
                    ans = 1
                else:
                    ans = (ans * (i - j + 1)) // j
                row.append(ans)
            result.append(row)
        return result