class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute force, too long to execute
        
        #max_volume = 0
        #if(len(height) == 2): return min(height[0], height[1])
        ## Loop through every element in hieghts
        #for i in range (0, len(height)-1):
        #        for j in range(i+1, len(height)):
        #            # If i and j are equal, ignore
        #            if i == j: continue
        #            smallest = min(height[i],height[j])
        #            largest = max(height[i],height[j])
        #            # Volume is the smallest of the two heights * the distance between
        #            volume = smallest * (max(i,j) - min(i,j))
        #            if volume > max_volume:
        #                max_volume = volume
        #return max_volume
         
        
        max_volume = 0
        i,j = 0,len(height)-1
        while i < j:
            max_volume = max(max_volume, min(height[i],height[j]) * (j - i))
            if  height[i] < height[j]: i += 1
            else: j -= 1
        return max_volume
            
        