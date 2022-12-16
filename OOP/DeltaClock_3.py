import time
class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
    def get_time(self):
        return self.hours*3600 + self.minutes*60 + self.seconds
    
class DeltaClock:
    def __init__(self, clock1, clock2):
        self.start = clock1
        self.end = clock2
    
    def delta(self):
        return self.start.hours - self.end.hours,\
                self.start.minutes - self.end.minutes,\
                self.start.seconds - self.end.seconds
    
    def __len__(self):
        out = self.start.get_time() - self.end.get_time()
        return out if out > 0 else 0
    
    def __str__(self):
        return time.strftime('%H: %M: %S', time.gmtime(len(self)))

dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
