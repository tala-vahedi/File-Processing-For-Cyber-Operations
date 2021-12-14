# Script Purpose: File Processing Object
# Script Version: 1.0 Sept 8, 2021
# Script Author:  Tala Vahedi

# Script Revision History:
# Version 1.0 Sept 8, 2021, Python 3.x

# Python Standard Library Modules
from binascii import hexlify

# Import 3rd Party Modules
import os
import time

# Psuedo Constants
SCRIPT_NAME    = "Script: File Processing Object"
SCRIPT_VERSION = "Version 1.0"
SCRIPT_AUTHOR  = "Author: Tala Vahedi"

# class named FileProcessor
class FileProcessor:
    # an init method
    def __init__(self, fileName, fileDir):
        # verifies the file exists
        if os.path.isfile(fileName):
            # extracts file  metadata from the file as instrance attributes
            self.fileDir = fileDir
            self.fileName = fileName
            stats = os.stat(self.fileName)
            self.fileSize = stats.st_size
            self.modifiedTime = time.ctime(stats.st_mtime)
            self.createTime = time.ctime(stats.st_atime)
            self.ownerID = stats.st_uid
            self.groupID = stats.st_gid
            self.mode = os.stat(fileName).st_mode
            self.device = stats.st_dev

    # a GetFileHeader Method   
    def GetFileHeader(self, fileName):
        # Opening the file as binary
        with open(self.fileName, 'rb') as f:
            # Extracting the first 20 bytes
            header = f.read(20)
            # storing them in an instance attribute
            self.hex = header

    # a PrintFileDetails Method 
    def PrintFileDetails(self):
        # Print the metadata
        print("File Path:                               ", self.fileDir)
        print("File Name:                               ", self.fileName)
        print("File Size:                               ", self.fileSize, "Bytes")
        print("File Modified Time:                      ", self.modifiedTime)
        print("File Created Time:                       ", self.createTime)
        print("File Owner ID:                           ", self.ownerID)
        print("File Group ID:                           ", self.groupID)
        print("File Inode Protection Mode:              ", self.mode)
        print("File Device Inode Resides On:            ", self.device)
        print("File header in Hex:                      ", hexlify(self.hex)) # header in hex

if __name__ == '__main__':
    # Print Basic Script Information
    print()
    print(SCRIPT_NAME)
    print(SCRIPT_VERSION)
    print(SCRIPT_AUTHOR)
    print()

    # prompting the user for a directory path continoulsy 
    while True:
        # prompting user to enter a path or enter 'exit' to end the program
        fileDir = input("Please enter a path (or enter 'exit' to stop the program): ")
        # condition that ends the program if user inputs 'exit'
        if fileDir == "exit":
            exit()
        # if path is not found, prompt the user to re-enter a path or exit the program
        elif os.path.exists(fileDir) == False:
            print("ERROR: Invalid file path, please try another path\n")
            continue
        # print processing the file path and break while statement to continue with code
        else:
            print("\nProcessing File, please wait...\n")
            break
    
    # using the os.listdir() method to extract filenames from the directory path
    directory = os.listdir(fileDir)
    # looping through each filename and instantiating an object using the FileProcessor Class
    for fileName in directory:
        classObjs = FileProcessor(fileName, fileDir)
        # invoke the GetFileHeader Method
        classObjs.GetFileHeader(fileName)
        # invoke the PrintFileDetails Method
        classObjs.PrintFileDetails()
        print()