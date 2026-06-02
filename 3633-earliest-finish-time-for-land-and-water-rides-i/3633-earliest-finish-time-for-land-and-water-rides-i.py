
class Solution:
    def calculate(self, prev_end: int, next_start: int, next_duration: int) -> int:
        wait = max(0, next_start - prev_end)
        return prev_end + wait + next_duration

    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:
        
        total = float('inf')

        for ls, ld in zip(landStartTime, landDuration):
            for ws, wd in zip(waterStartTime, waterDuration):
            
                land_end = ls + ld
                land_water = self.calculate(land_end, ws, wd)
                water_end = ws + wd
                water_land = self.calculate(water_end, ls, ld)

                total = min(total, land_water, water_land)

        return total