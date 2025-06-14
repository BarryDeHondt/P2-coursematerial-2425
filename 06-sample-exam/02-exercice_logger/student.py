from abc import ABC, abstractmethod
from datetime import datetime

class Exercise(ABC):
    def __init__(self, date, distance, duration):
        if not self.is_valid_date(date):
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        if distance <= 0:
            raise ValueError("Distance must be greater than 0.")
        if duration <= 0:
            raise ValueError("Duration must be greater than 0.")

        self.date = date
        self.distance = distance  
        self.duration = duration
        
    def __eq__(self, other):
        return self.calories == other.calories
    
    

        
        
    
    @property
    @abstractmethod
    def calories_factor(self):
        pass
    
    @property
    def calories(self):
        return int((self.distance / (self.duration / 60)) * self.distance * self.calories_factor)

    def is_valid_date(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    
    

class Run(Exercise):
    def __init__(self, date, distance, duration, elevation):
        self.elevation = elevation  
        super().__init__(date, distance, duration)


    @property
    def calories_factor(self):
        return 10 * (1 + self.elevation / 100)


class Swim(Exercise):
    def __init__(self, date, distance, duration):
        super().__init__(date, distance, duration)

    @property
    def calories_factor(self):
        return 40

class Ride(Exercise):
    def __init__(self, date, distance, duration, elevation):
        super().__init__(date, distance, duration)
        self.elevation = elevation # elevation in percentage

    @property
    def calories_factor(self):
        return 2 * (1 + self.elevation / 100)

class ExerciseLog:
    def __init__(self):
        self.__exercises = []

    def add(self, exercise):
        self.__exercises.append(exercise)

    def create_run(self, date, distance, duration, elevation):
        self.add(Run(date, distance, duration, elevation))

    def create_swim(self, date, distance, duration):
        self.add(Swim(date, distance, duration))

    def create_ride(self, date, distance, duration, elevation):
        self.add(Ride(date, distance, duration, elevation))

    def total_calories_burnt(self):
        return sum(exercise.calories for exercise in self.__exercises)


morning_run = Run("2023-10-02", 5, 21, 12)
print(morning_run.calories)

evening_bike_ride = Ride("2023-10-01", 20, 60, 0)
print(evening_bike_ride.calories)

print(morning_run == evening_bike_ride)

# print(morning_run < evening_bike_ride)

# print(morning_run > evening_bike_ride)