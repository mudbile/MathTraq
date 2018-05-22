from random import random
import mpmath


def schop(num, decimal_places):
    """
    Takes a number (string, an int, a float or an mpmath.mpf), 
    and returns a string with decimal_places decimal places.
    The string is padded to the right with "0".
    """
    s = str(num)
    if s.find('.') == -1:
        before_d = s
        after_d = '0'
    else:
        before_d, after_d = s.split('.')

    #add the digits before the cecimal point
    ret = before_d + '.'

    #add the digits after the decimal point
    for i in range(0, decimal_places):
        if i < len(after_d):
            ret += after_d[i]
        else:
            ret += '0'
    return ret




def get_random(min, max, max_decimal_places):
    """
    Returns a pseudo-random mpmath.mpf value between
    min and max (inclusive) with at most max_decimal_places.
    Assumes max is greater than min.
    """
    #step 1: make sure min and max have the right number of dps
    #e.g. min: 4.5 ; max: 7.8 ; dps: 1
    min = mpmath.mpf(schop(min, max_decimal_places))
    max = mpmath.mpf(schop(max, max_decimal_places))

    #step 2: instead of dealing with -ve numbers directly, we bump
    #them positive and bump the random number back later
    bump_value = mpmath.fabs(min) + 1
    bump_back = False
    if min < 1:
        min += bump_value
        max += bump_value
        bump_back = True

    #step 3: take 0.5*10^(-dp) away from min, add the same to max
    #this is so rounding will give min and max a fair go
    #e.g. min: 4.45 ; max: 7.85 ; dps: 1
    min -= mpmath.mpf(0.5) * mpmath.power(10, -max_decimal_places)
    max += mpmath.mpf(0.5) * mpmath.power(10, -max_decimal_places)

    #step 4: get a random number between [min, max) using normal rand()
    #e.g. intermediary: [0, 1) * 3.4 + 4.45 = [4.45, 7.85)
    intermediary = mpmath.rand() * (max - min) + min

    #step 5: round that number to dps
    #e.g.   ret can't be < 4.5 because intermediary >= 4.45
    #       ret can't be > 7.8 because intermediary < 7.85
    ret = mpmath.mpf(sround(intermediary, max_decimal_places))

    #step 6: bump back if necesary
    if bump_back:
        ret -= bump_value

    return ret



def sround(num, decimal_places):
    """
    Rounds away from 0. works for ints, floats and mpmath.mpf. 
    returns string. 
    """
    s = str(num)
    #get the digits after the decimal
    
    if s.find('.') == -1:
        after_d = '0'
    else:
        after_d = s.split('.')[1]

    #only worry about rounding if there's enough dps to make a difference
    if len(after_d) > decimal_places and after_d[decimal_places] >= '5':
        #we round away from 0
        if num >= 0:
            #e.g num: 234.23356 ; dp: 3 -> 234.23456
            num += mpmath.mpf(1.0) * mpmath.power(10, -decimal_places)
        else:
            num -= mpmath.mpf(1.0) * mpmath.power(10, -decimal_places)

    #there still might be trailing digits whcih we chop off
    #e.g num: 234.23456 -> 234.234
    return schop(num, decimal_places)