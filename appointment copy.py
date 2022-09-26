"""
Name: Yamlak Shimelis
Partner: Ningyuan Zhang
Date: 03_10_2022
A script meant for tracking appointments by name, start time, and end times.
"""

class Appointment:
    """A class that tracks information about an appointment such as the start 
    and end times and a name for the appointment.
    Attributes:
        name: name of the appointment
        start: start time of the appointment
        end: end time of the appointment
    """
    
    def __init__(self, name, start, end):
        """Initializes a appointment object
        
        Arguments:
            name (str): name of appointment
            start (tuple): a tuple consisting of two integers representing the start time 
            of the appointment. The first integer represents an hour in 24-hour time; the
            second integer represents a number of minutes.
            end (tuple): A tuple similar to start, representing the end time of the 
            appointment.
        """
        self.name = name
        self.start = start
        self.end = end
        
    def overlaps(self, other):
        """Checks to see if appointment times overlap each other
        
        Arguments:
            other: an appointment object
            
        Returns:
            Boolean: Returns a boolean indicating whether appointments overlap each other
        """
        
        return (self.start <= other.start < self.end or 
                self.start < other.end <= self.end)

        
        
        
            