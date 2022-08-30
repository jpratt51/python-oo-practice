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
    def __init__(self,start):
        """Make new serial generator, starting at start value"""
        self.start = self.next = start
    def __repr__(self):
        """Lists the start value of the generator and the next number"""
        return f"<Number {self.start}, next number {self.next}"
    def generate(self):
        """Returns start value initially, and then the next sequential number each time generate is called"""
        self.next += 1
        return self.next - 1

        
    def reset(self):
        """Resets start value"""
        self.next = self.start
