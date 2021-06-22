
        

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # return 1 if there are no flowers to plant or 0 if the flower bed is empty
        if not list: return 0
        elif n == 0: return 1
        prev = None
        nxt = None
        #For each slot in the flowerbed
        for i in range(0, len(flowerbed)):
            # Try to set next if available
            try: nxt = flowerbed[i+1]
            except: nxt = None
            curr = flowerbed[i]
            # if previous and next slot are both empty/dont exist
            if (prev == None or prev == 0) and (nxt == None or nxt == 0 ) and curr == 0:
                # Count down the number of flowers left to plant
                n -= 1
                # Plant the flower in the slot
                flowerbed[i], curr = 1,1
                
            # Set Prev to current
            prev = curr
            if n == 0: break
        if n <= 0:
            return 1
        return 0
            
        