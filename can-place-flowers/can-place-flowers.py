
        

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # return 1 if there are no flowers to plant or 0 if the flower bed is empty
        if not list: return 0
        elif n == 0: return 1
        prev = 0
        nxt = 0
        
        #pad back of bed with a 0
        bed = flowerbed + [0]
        
        #For each slot in bed
        for i in range(0, len(flowerbed)):
            nxt = bed[i+1]
            # if previous and next slot are both empty
            if prev == 0 and nxt == 0 and bed[i] == 0:
                # Count down the number of flowers left to plant
                n -= 1
                # Plant the flower in the slot
                bed[i] = 1
            # Set Prev to current
            prev = bed[i]
            if n == 0: break
        if n <= 0:
            return 1
        return 0
            
        
