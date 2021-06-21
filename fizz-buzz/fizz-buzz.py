class Solution:
    
    def fizz(self, i) -> str:
        if i == 0: return "Fizz"
        return ""
        
    def buzz(self, i) -> str:
        if i == 0: return "Buzz"
        return ""
    
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for i in range (1, n+1):
            fz, bz = i%3, i%5
            if fz == 0 or bz == 0 : 
                out.append(str(self.fizz(fz) + self.buzz(bz)))
            else: out.append(str(i))
        return out
            