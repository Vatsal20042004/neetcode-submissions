class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_=s.lower().replace(' ','')
        forma=''
        palindrome=''
        for i in s_:
            if i.isalnum():
                forma+=i
        palindrome=forma[::-1]
        if palindrome==forma:
            return True
        return False
        