# Last updated: 9/6/2026, 2:55:15 PM
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return[celsius + 273.15, celsius * 1.80 + 32.00]
