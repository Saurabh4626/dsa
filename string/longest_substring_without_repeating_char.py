## using sliding window complexity O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:return 0
        i,j=0,0
        ans=0
        n=len(s)
        arr=list()
        while j<n:
            if s[j] in arr:
                while s[j] in arr:
                    arr.remove(s[i])
                    i+=1
                arr.append(s[j])
                ans=max(ans,j-i+1)
                j+=1
            else:
                arr.append(s[j])
                ans=max(ans,j-i+1)
                j+=1
        return ans