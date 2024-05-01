class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        current_water = capacity
        at_river = True        
        for i in range(len(plants)):
            current_water -= plants[i]
            if at_river:
                steps += (i+1)
            else:
                steps += 1
            if i < len(plants) - 1:
                if current_water < plants[i+1]:
                    steps += (i+1)
                    current_water = capacity
                    at_river = True
                else:
                    at_river = False
        return steps