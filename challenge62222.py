def maximum69Number (self, num: int) -> int:
        # With numbers the further left the digit is the greater the value.
        # The solution is to find the first 6 going left to right and replacing it with 9
        # You never want to replace a 9 with 6 because you would be decreasing value.
        s = str(num)
        for i,val in enumerate(s):
            if val == '6':
                # replacing 6 at that position to 9
                ans = s[:i] + '9' + s[i+1:]
                return int(ans)
        return num
