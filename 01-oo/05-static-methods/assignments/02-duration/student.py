class Duration:
    def __init__(self, *, time):
        self.time = time
        
    @staticmethod
    def from_seconds(amount):
        return Duration(time=amount)
        
    @staticmethod
    def from_minutes(amount):
        return Duration(time=amount * 60)
        
    @staticmethod
    def from_hours(amount):
        return Duration(time=amount * 3600)
         
    def seconds(self):
        return self.time 
        
    def minutes(self):
        return self.time / 60
    
    def hours(self):
        return self.time / 3600
    
    def __str__(self):
        return f"{self.time}"
        

# Example usage
duration = Duration.from_seconds(60)
print(duration.seconds())  # Should print 60
print(duration.minutes())  # Should print 1.0

duration = Duration.from_hours(1)
print(duration.minutes())  # Should print 60.0
print(duration.seconds())  # Should print 3600
