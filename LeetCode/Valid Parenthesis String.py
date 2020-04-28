class Solution:
    def checkValidString(self, s: str) -> bool:
        ob_stack=[]
        cb_stack=[]
        starc=0
        for c in s:
            if c=='(':
                ob_stack.append(c)
            elif c==')':
                if not not ob_stack:
                    ob_stack.pop()
                else:
                    if starc<1:
                        return False
                    else: starc-=1
            elif c=='*':
                starc+=1
        starc=0
        for c in s[::-1]:
            if c==')':
                cb_stack.append(c)
            elif c=='(':
                if not not cb_stack:
                    cb_stack.pop()
                else:
                    if starc<1:
                        return False
                    else: starc-=1
            elif c=='*':
                starc+=1
        return True
