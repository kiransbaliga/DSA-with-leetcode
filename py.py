# class Solution:
#     def findLUSlength(self, strs: List[str]) -> int:
#         strs=list(sorted(strs,key=len))
#         for i in range(len(strs)-1):
#             for j in range(i+1,len(strs)):
                
class Solution:
        def findLUSlength(self, words):
            def isSubsequence(s, t):
                t = iter(t)
                return all(c in t for c in s)
 
            words.sort(key = lambda x:-len(x))
            for i, word in enumerate(words):
                if all(not isSubsequence(word, words[j]) for j in range(len(words)) if j != i): 
                    return len(word)
        
            return -1