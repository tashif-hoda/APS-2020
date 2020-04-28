class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stackS=[]
        stackT=[]
        for c in S:
            if c=='#' and len(stackS)>0:
                stackS.pop()
            elif c!='#':
                stackS.append(c)
        for c in T:
            if c=='#' and len(stackT)>0:
                stackT.pop()
            elif c!='#':
                stackT.append(c)
        if stackS==stackT:
            return True
        return False
