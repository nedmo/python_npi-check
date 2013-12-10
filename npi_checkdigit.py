#!/usr/bin/env python
"""This module contains 2 functions: 
- getNPIchecksum calculates the Luhn checksum of an NPI from the first 9/14 digits.
- NPIisGood uses getNPIchecksum to verify an entire 10- or 15-digit NPI number.
Contact: Ned Mossman, Oregon Osteoporosis Center (nmossman__at__orost__dot__com)
You may use, modify, and distribute this code freely.  It has been tested on 
Python 2.4 and 2.5, but is provided AS IS with NO WARRANTY OR GUARANTEES.""" 

import sys
import string
def getNPIchecksum(npiLeft=''):
    """Accepts first 9 or 14 digits of 10- or 15-digit NPI as a string or int and 
    returns the last (checksum) digit as a string, or a longer descriptive string on
    an error.  If 10-digit format is used (leftmost 9 digits supplied), USA prefix 
    of 80840 is assumed."""
    
    #if input is not a string, convert it first for easier manipulation
    if type(npiLeft)!=type('string'):
        npiLeft=str(npiLeft)
    if npiLeft.isdigit() and (len(npiLeft)==9 or len(npiLeft)==14):
        try:
            #USA prefix is 80840 - adds 24
            if len(npiLeft)==9:
                sum=24
            else:
                sum=0
            #reverse input to read R-L
            nr=npiLeft[::-1]
            #create odd/even switch
            j=-1
            for i in range(len(nr)):
                k=int(nr[i])
                if j==-1:
                    #convert char in string to integer
                    #If k>4, the result of k*2 is 2 digits. If so, add these digits
                    # together.  Otherwise, just use k*2
                    if k>4:
                        #sum+=((k*2)%10)+1
                        #  ^This works fine, but it's easier to just subtract 9 
                        #   since k*2 can't be more than 18
                        sum+=(k*2)-9
                    else:
                        sum+=k*2
                else:
                    sum+=k
                #toggle odd/even    
                j=~j
            #Return (10-x) where x is the tenths digit of sum.
            #If x=0, return 0 not 10.
            r = (10 - (sum%10))%10
            return str(r)
        except:
            return 'Error: there was an error calculating the checksum from the digits provided. Check your entry and try again.'
    else:
        return 'Error: input must consist of leftmost 9 digits from a 10-digit NPI or 14 digits from a 15-digit NPI.  The NPI entered is not valid.'
        
def NPIisGood(npi=''):
    """Uses getNPIchecksum to determine if the NPI provided is valid.
    Accepts entire NPI as string or int, returns True if checksum digit
    is valid, False if invalid, and an error string if not evaluable.
    Works for 10 or 15-digit NPIs."""

    #force to string
    if type(npi)!=type('string'):
        npi=str(npi)
    #check to make sure checksum is a digit since it isn't passed to getNPIchecksum()
    if npi[-1].isdigit() == False:
        return 'Error: Improper NPI format. Checksum digit must be numeric.'
    else:
        cs=getNPIchecksum(npi[:-1])
        #If a single digit was successfully returned, return result of comparison of 
        #entered vs. calculated checksum digit as boolean
        if len(cs) > 1:
            return 'Error: Improper NPI format.  Cannot determine the validity of the checksum.  Enter a 10 or 15 digit NPI number as a string or integer.'
        else:
            return cs == npi[-1]
            
if __name__ == "__main__":
    print NPIisGood(sys.argv[1])
