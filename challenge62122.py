def validPalindrome(self, s: str) -> bool:
    
    def isPal(t):
        return t == t[::-1]
    l, r = 0, len(s) - 1
    if len(s) == 1:
        return True
    while(l < r):
        if s[l] != s[r]:
            # delete the character at position l and check if it's a palindrome
            if isPal(s[l + 1:r+1]):
                return True
            #delete the character at postion r and check if it's a plaindrome
            elif isPal(s[l:r]):
                return True
            #if neither are palindromes then it's not poaaible
            else:
                return False
        l += 1
        r -= 1
    
    #if code gets here the characters at position l and r were always equal meaning it is palindrome without any deletions
    return True 