"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=100):
        self.start = start
        self.curr_serial = start
        self.next_serial = start
    
    def generate(self):
        """
        Generates a new serial number and increments SerialGenerator.next_serial by one every time it is called.
        """
        if self.curr_serial == self.start:
            self.next_serial += 1
            self.curr_serial = self.next_serial
            return self.start
        else:
            self.curr_serial = self.next_serial
            self.next_serial += 1
            return self.curr_serial
    
    def reset(self):
        """
        Resets SerialGenerator.curr_serial and SerialGenerator.next_serial back to SerialGenerator.start value
        """
        self.curr_serial = self.start
        self.next_serial = self.start
        

serial = SerialGenerator(start=100)

print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.reset())
print(serial.generate())