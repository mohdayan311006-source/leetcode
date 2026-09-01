class Solution(object):
    def minEatingSpeed(self, piles, h):
        def eating_speed():
            speed=0 ##total_time to eat all plies
            for i in piles:
                if i%guess==0:
                    speed+=(i//guess)
                else:
                    speed+=(i//guess)+1
            return speed
        low=1
        high=piles[0]
        for x in piles:
            if x>high:
                high=x
        res=-1
        while low<=high:
            guess=(low+high)//2
            hours=eating_speed()
            if hours>h:
                low=guess+1
            else:
                res=guess
                high=guess-1
        return res
                
        
            
        




        