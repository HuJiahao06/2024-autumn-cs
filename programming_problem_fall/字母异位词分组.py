class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        dic={}
        jdg=[]
        for i in strs:
            buffer=list(i)
            buffer.sort(key=lambda x:ord(x))
            if buffer not in jdg:
                jdg.append(buffer)
                dic[jdg.index(buffer)]=[]
                dic[jdg.index(buffer)].append(i)
            else:
                dic[jdg.index(buffer)].append(i)
        for i in range(len(jdg)):
            ans.append(dic[i])
        return ans