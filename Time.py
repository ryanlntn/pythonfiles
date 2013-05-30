#
# Time.py
#

class Time:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def convert_to_seconds(self):
        minutes = self.hours * 60 + self.minutes
        seconds = minutes * 60 + self.seconds
        return seconds

    def print_time(time):
        print (str(time.hours) + ":" +
               str(time.minutes) + ":" +
               str(time.seconds))
        
def make_time(seconds):
    time = Time()
    time.hours = seconds/3600
    seconds = seconds - time.hours * 3600
    time.minutes = seconds/60
    seconds = seconds - time.minutes * 60
    time.seconds = seconds
    return time


def add_time(t1, t2):
    seconds = convert_to_seconds(t1) + convert_to_seconds(t2)
    return make_time(seconds)


def after(t1, t2):
    if convert_to_seconds(t1) > convert_to_seconds(t2):
        return True
    else:
        return False


def increment_mod(time, seconds):
    new_time = make_time(convert_to_seconds(time) + seconds)
    time.hours = new_time.hours
    time.minutes = new_time.minutes
    time.seconds = new_time.seconds

def increment_pure(time, seconds):
    new_time = make_time(convert_to_seconds(time) + seconds)
    return new_time
    
