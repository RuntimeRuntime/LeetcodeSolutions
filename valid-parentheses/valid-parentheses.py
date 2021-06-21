class Solution:

    
    def isValid(self, s: str) -> bool:
        #check if even
        if(len(s)%2 != 0): return 0
        # do the number of opens and closes match
        if s.count('(') != s.count(')') or s.count('{') != s.count('}') or s.count('[') != s.count(']'):
            return 0
        # find enclosed brackets next to eachother and remove them
        
        while len(s) != 0: 
            prevS = len(s)
            s = s.replace('()', '').replace('[]','').replace('{}', '')
            if prevS == len(s): return 0
        return 1

        
        
       