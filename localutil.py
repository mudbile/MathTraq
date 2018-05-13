import mpmath
import os

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False  


def round_to_num_decimals(value, num_decimals):
    """
    Returns mpf float rounded to max of num_decimals decimal places
    """
    #ensure we have enough after the decimal
    temp = str(value) + ('0' * num_decimals) + '0'
    pos_of_dec = temp.find('.')
    index_of_eventual_last = pos_of_dec + num_decimals
    #if num_decimals == 0
    if temp[index_of_eventual_last] == '.':
        index_of_eventual_last -= 1
    decider =  temp[pos_of_dec + num_decimals + 1]
    eventual_last = int(temp[index_of_eventual_last])
    if decider >= '5':
        eventual_last += 1
    temp = temp[:index_of_eventual_last] + str(eventual_last)
    return mpmath.mpf(temp)


def get_random(minimum, maximum, max_decimal_places):
        """
        Returns a random mpmath.mpf between [minimum, maximum)
        with, at most, max_decimal_places digits after the decimal point.
        Note: would-be integers have .0 attached in mpf land
        """
        #get a random number between [minimum, maximum)
        num = mpmath.rand() * (maximum-minimum) + minimum
        #scale it up
        num *= mpmath.power(10, max_decimal_places)
        #cut off it's tail
        temp = str(num).split('.')[0]
        num = mpmath.mpf(temp)
        #scale it back down
        num *= mpmath.power(10, -max_decimal_places)
        return num


def is_positive_int_compatible(val):
        """
        True if val can be converted to int which would 
        be posisitve
        """
        try:
            i = int(val)
            return i > 0
        except ValueError:
            return False


def is_positive_float_compatible(val):
    try:
        f = float(val)
        return f > 0
    except:
        return False


def remove_file_if_exists(filename):
    """
    Remove file if it exists
    """
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass

def create_dir_if_absent(dirname):
    """
    create folder if it doesn't exist
    """
    try:
        os.makedirs(dirname)
    except FileExistsError :
        pass

