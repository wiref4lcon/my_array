from statistics import median

class Array:
    '''
    This is a single-dimensional numeric
    array for scientific computing.

    This array will compute lots of
    basic statistics.

    Parameters
    ----------
    data: list
        List of numbers
    '''

    
    
    def __init__(self, data):
        self.data = data

    def sum(self):
        return sum(self.data)

    def max(self):
        return max(self.data)

    def min(self):
        return min(self.data)

    def mean(self):
        return self.sum() / len(self.data)

    def median(self):
        return median(self.data)