class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{str(self.hour).zfill(2)}:" \
               f"{str(self.minute).zfill(2)}:" \
               f"{str(self.second).zfill(2)}"
t = Time(2,13,41)

print(t)
print("the time is " +str(t))
