from statistics import median
from array import array

class Array:
    '''
    This is a single-dimensional numeric
    array for scientific computing.

    This array will compute lots of
    basic statistics.

    Attributes
    ----------
    data: list
        List of numbers

    Methods
    -------
    TODO
    '''


    def __init__(self, data):
        # Allow user to pass only an array or a list
        if isinstance(data, array):
            # TODO - check for cases where typecode is not 'b', 'q', or 'd'
            self.data = data
        elif isinstance(data, list):
            if len(data) == 0:
                # hack - forcing array to be a float
                first_item = 0.0
            else:
                first_item = data[0]

            if isinstance(first_item, bool):
                dtype = 'b'
            elif isinstance(first_item, int):
                dtype = 'q'
            elif isinstance(first_item, float):
                dtype = 'd'
            else:
                raise TypeError('List must only contain bool, '
                                'ints, or floats')
            try:
                self.data = array(dtype, data)
            except TypeError:
                self.data = array('d', data)
        else:
            raise TypeError('Array constructor only accepts lists or arrays')
        # b - boolean (1 byte integer)
        # q - interger (8 bytes)
        # d - float (8 bytes)
        self.dtype = self.data.typecode
    def sum(self):
        '''
        Sums all the values in the array

        Returns
        -------
        int or float
        '''
        return sum(self.data)

    def max(self):
        '''
        Finds max of all values in the array

        Returns
        -------
        int or float
        '''
        return max(self.data)

    def min(self):
        '''
        Finds min of all values in the array

        Returns
        -------
        int or float
        '''
        return min(self.data)

    def mean(self):
        '''
        Finds mean of all values in the array

        Returns
        -------
        int or float
        '''
        return self.sum() / len(self.data)

    def median(self):
        '''
        Finds median of all values in the array

        Returns
        -------
        int or float
        '''
        return median(self.data)