# -*- coding: utf-8 -*-
"""
dirmapper v0.2
"""

import os
import sys

def MapDir(directory = os.getcwd(), filetypes = [".py", ".md"], language = "python"):
    allfiles = os.listdir()
    allfilestemp = []
    for file in allfiles:
        for filetype in filetypes:
            if filetype in file:
                allfilestemp.append(file)
    allfiles = allfilestemp
    
    #add explicit languages if existing methods for mapping out dir
    if language == "python":
        pass #todo: change to python specific logic
    
    else:
        return #todo: change to general purpose shit
    globalout = 0
    globalinc = 0
    
    assert globalout == globalinc
        
        
    return  allfilestemp
    
def FileProcessor(filename, files, filetypes):
    #two places to pull from
    #same dir
    #external files
    
    #only map the dir
    file = open(filename, "r")
    lines = file.readlines()
    
    extpulls = []
    dirpulls = []
    
    #README.md testing readme is identified
    
    #todo: this is the most simple logic to get the job mostly done (in python)
    #      functionality will follow after frontend complete
    test = "thisisatestfile.md"
    #collect file pulls and assign to pull buckets
    for line in lines:
        #assign to dir bucket
        for file in files:
            if file in line: #if file is in dir, then add it to dirpulls
                dirpulls.append(file) #add logic for commented lines
                
        #assign to ext bucket
        lsplit = line.split(sep = " ")
        
        files_in_line = []
        for ft in filetypes:
            for el in lsplit:
                if len(el) > 0:
                    if el[0] == "#":
                        break
                if ft in el:
                    files_in_line.append(el)
                    
        extpulls += files_in_line
      
    #assign to lib bucket
    libpulls =  set(sys.modules)&set(globals())
        
        
    #remove dupes
    extpulls = set(extpulls)
    op, mid1, mid2, cl = '["', '"', '",', '"],'
    mistakenlyAdded = [op + filetypes[0] + mid2] + [mid1 + ft + mid2 for ft in filetypes] + [mid1 + filetypes[-1] + cl]
    extpulls = extpulls.difference(set(mistakenlyAdded))
    
    dirpulls = set(dirpulls)          
                    
    #todo: refine names
    
    return libpulls, dirpulls, extpulls

def TidyBucket():
    #todo: tidy the buckets by removing bad entries, cleaning double quotes,
    #cleaning line breaks etc
    return

def IgnoreFiles():
    #todo: add logic to ignore files, we really dont want to read
    #lengthy files that arent part of code
    return





        
