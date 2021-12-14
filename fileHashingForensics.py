# Script Purpose: Hashing Files for Forensics
# Script Version: 1.0 August 31, 2021
# Script Author:  Tala Vahedi

# Script Revision History:
# Version 1.0 August 31, 2021, Python 3.x

# Python Standard Library Modules
from __future__ import print_function

# Import 3rd Party Modules
import os
import hashlib

# Psuedo Constants
SCRIPT_NAME    = "Script: Hashing Files for Forensics"
SCRIPT_VERSION = "Version 1.0"
SCRIPT_AUTHOR  = "Author: Tala Vahedi"

if __name__ == '__main__':
   # Print Basic Script Information
   print()
   print(SCRIPT_NAME)
   print(SCRIPT_VERSION)
   print(SCRIPT_AUTHOR)
   print()

   # directory place holder
   directory = "."

   # creating empty list and dictionary
   fileList = []
   fileHashes = {}

   # iterating through the director
   for root, dirs, files in os.walk(directory):
      # iterating through each file and getting filenames
      for fileName in files:
         # appending all files to list
         fileList.append(fileName)
         #iterating through each file in list
         for file in fileList:
            # calculating the md5 hash of each file in hex to set as key of dict
            key = hashlib.md5(file).hexdigest()
            # establishing the path of each file to set as the value of dict
            path = os.path.join(root, file)
            value = os.path.abspath(path)
            # adding the key, value of each file in director to dict
            fileHashes[key]=value
      
   # iterating through each key, value pair and printing out the values
   for key, value in fileHashes.items():
      print("Key (md5 hash):", key)
      print("Value (file path):", value)
      print()