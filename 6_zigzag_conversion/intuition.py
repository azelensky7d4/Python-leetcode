class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for row in range(numRows)]
        going_down = True
        current_row_index = 0
        for char in s:
            if going_down:
                rows[current_row_index].append(char)
                if current_row_index == numRows - 1:
                    going_down = False
                    current_row_index -= 1
                else:
                    current_row_index += 1
            else:
                rows[current_row_index].append(char)
                if current_row_index == 0:
                    going_down = True
                    current_row_index += 1
                else:
                    current_row_index -= 1
        return ''.join([''.join(row) for row in rows])

if __name__ == '__main__':
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))
    print(s.convert("PAYPALISHIRING", 4))
    print(s.convert("ABC", 1))

