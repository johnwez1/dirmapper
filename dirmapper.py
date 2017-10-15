# -*- coding: utf-8 -*-
"""
dirmapper v0.2
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
    
    #README.md testing read.me is identified
    
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








        
