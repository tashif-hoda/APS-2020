class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out=[]
        comb_that_exist=[]
        
        for i in range(len(strs)):
            dic={}
            for char in strs[i]:
                if char in dic:
                    dic[char]+=1
                else:
                    dic[char]=1
            f=False
            for j in range(len(comb_that_exist)):
                if dic==comb_that_exist[j]:
                    out[j].append(strs[i])
                    f=True
                    break
            if not f:
                out.append([strs[i]])
                comb_that_exist.append(dic)
        return out
                
