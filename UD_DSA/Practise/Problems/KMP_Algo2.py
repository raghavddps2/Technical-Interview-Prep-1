class Solution:
    def LPS_compute(self,pattern,M,lps):
        len1 = 0
        i = 0
            
        lps[0] = 0
        while i < M:
            # print("hiss")
            if pattern[i] == pattern[len1]:
                lps[i] = len1 + 1
                len1 = len1 + 1
                i = i + 1
                    
            else:
                    #Handling for 2 cases if that does noot match.
                if len1  != 0:
                    len1 = lps[i-1]
                    i = i + 1
                else:
                    lps[i] = 0
                    i = i + 1
        
    def KMPAlgorithm(self,text,pattern):
            
        if text == "" and pattern == "":
            return 0
        if pattern == "":
            return 0
            #I maintain this pointer for the text.
        i = 0
        j = 0
        N = len(text)
        M = len(pattern)
        LPS = [0]*M
        self.LPS_compute(pattern,M,LPS)
        # print("hi")
        while i < N:
            # print("hissd")
            if text[i] == pattern[j]:
                i = i + 1
                j = j + 1
            else:
                if j != 0:
                    j = LPS[j-1]
                    i = i + 1
                else:
                    i = i + 1
                    
            if j == M:
                # print(i)
                # print(j)
                ans = (i-j)
                return ans
                # return
        return -1
        # return
    def strStr(self, haystack: str, needle: str) -> int:
        return self.KMPAlgorithm(haystack,needle)        

a = Solution()
print(a.KMPAlgorithm("mississippi","issipi"))