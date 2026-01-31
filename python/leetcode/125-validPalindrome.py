## ///////////////////////////////////////////
## 125. Valid Palindrome
## ///////////////////////////////////////////


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clear the string and parse
        s = [ x.lower() for x in s if x.isalpha() or x.isdigit() ] # list of chars ['a','m',...]
        s = ''.join(s) #> conver to string list   
        
        return s == s[::-1]


if __name__== '__main__':
	# s = "A man, a plan, a canal: Panama"
	s = "race a car"
	# s = "0P"

	result = Solution()
	print(result.isPalindrome(s))
