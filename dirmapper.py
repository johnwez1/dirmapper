# -*- coding: utf-8 -*-
"""
place in read.me

dirmapper v0.2

development of prototype classes and methods

the purpose of dirmapper is to read a codebase
and present an easily decipherable map of 
how files relate to each other and any
external libraries

the backend should contain relatively simple logic

the frontend should be created using a markup language
latex is easy but probably not practical as a dependancy

lets try XML?


this commented section to go into read.me after spyder git works
"""

import os

def mapdir(directory = os.getcwd(), filetypes = [".py", ".md"], language = "python"):
    allfiles = os.listdir()
    allfilestemp = []
    for file in allfiles:
        for filetype in filetypes:
            if filetype in file:
                allfilestemp.append(file)
    allfiles = allfilestemp
    
    #add explicit languages if existing methods for mapping out dir
    if language == "python":
        libreceptor = "import" #should do, maybe add more
    
    else:
        return
    globalout = 0
    globalinc = 0
    
    assert globalout == globalinc
        
        
    return  allfilestemp
    
def fileprocessor(filename, files, libreceptor):
    #two places to pull from
    #same dir
    #external files
    
    #only map the dir
    file = open(filename, "r")
    lines = file.readlines()
    
    libpulls = []
    dirpulls = []
    
    #README.md
    
    #collect file pulls and assign to pull buckets
    for line in lines:
        for file in files:
            if file in line: #if file is in dir, then add it to dir
                dirpulls.append(line)
            elif libreceptor == line.split(sep = " ")[0]: #if pull is not in dir then add it to libs
                libpulls.append(line)
                
    libpulls = set(libpulls)
    dirpulls = set(dirpulls)          
                
    return libpulls, dirpulls 








        