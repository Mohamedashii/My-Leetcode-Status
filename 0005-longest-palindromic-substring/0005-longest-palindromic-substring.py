class Solution:
    def longestPalindrome(self, s: str) -> str:
      ans=""
      for i in range(len(s)):
        for j in range(i,len(s)):
            sub=s[i:j+1]
            if sub[::-1]==sub:
                if len(sub)>len(ans):
                    ans=sub
      return ans