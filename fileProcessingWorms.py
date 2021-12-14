# Script Purpose: File Processing
# Script Version: 1.0 August 31, 2021
# Script Author:  Tala Vahedi

# Script Revision History:
# Version 1.0 August 31, 2021, Python 3.x

# Python Standard Library Modules
from __future__ import print_function

# Import 3rd Party Modules
import os

# Psuedo Constants
SCRIPT_NAME    = "Script: File Processing"
SCRIPT_VERSION = "Version 1.0"
SCRIPT_AUTHOR  = "Author: Tala Vahedi"

if __name__ == '__main__':
    # Print Basic Script Information
    print()
    print(SCRIPT_NAME)
    print(SCRIPT_VERSION)
    print(SCRIPT_AUTHOR)
    print()

    # creating a set to hold the unique worms found in logfile
    uniqueWorms = set()

    # opening the log file and identifying it as "logfile"
    with open("redhat.txt", 'r') as logFile:
        # iterating through each line within the logfile
        for eachLine in logFile:
            # using split() to split each line in logfile and holding it in new variable
            splitLogFile = eachLine.split()
            # iterating through each work within the lines to find worms
            for line in splitLogFile:
                # if statement to see if "worm" is found in line 
                if "Worm" in line:
                    # then adding it to the unique set 
                    uniqueWorms.add(line)
    # using sorted() to sort the set in alphabetical order
    sortedSetOfWorms = sorted(uniqueWorms)
    # iterating through the sorted set 
    print("The following list of unique worms were found in logfile:")
    for worms in sortedSetOfWorms:
        # printing out each worm found in logfile
        print(worms)
 