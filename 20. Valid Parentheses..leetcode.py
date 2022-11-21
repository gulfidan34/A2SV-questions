class Solution:
    def isValid(self, s: str) -> bool:
        # str is odd ror not
        if len(s) % 2 != 0:
            return False
        
        params = {'(':')','[':']','{':'}'}
        stack=[]
        for i in s:
            if i in params:
                stack.append(i)
            else:
                if stack==[]:
                    return False
                ob= stack.pop()
                if i != params[ob]:
                    return False
        return stack == []


