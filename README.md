# File-Processing-For-Cyber-Operations
Hashing Files for Forensics and Worms

File Hashing for Forensics:
Using the os library and the os.walk() method 
    a) Create a list of all files
    b) Create an empty dictionary named fileHashes 
    c) Iterate through the list of files and
       - calculate the md5 hash of each file
       - create a dictionary entry where:
         key   = md5 hash
         value = filepath
     d) Tterate through the dictionary
        - print out each key, value pair
