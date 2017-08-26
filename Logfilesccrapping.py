# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 13:28:19 2017

@author: Ashish Pal
"""

# log file path
plm_file_path = r"R:\PLM\NewLookIntergrationTrace - 20170512.txt"
# text sheet path where we have to copy products 
plm_data_path = r'R:\PLM\NewLookIntergrationTrace - 20170512-data.txt'

 # Declare an empty list named "lines"
lines = []                 
with open(plm_file_path, 'rt') as in_file_plm:
    for line in in_file_plm:  # For each line of text in in_file, where the data is named "line",
        lines.append(line.rstrip('\n'))   # add that line to our list of lines, stripping newlines.
		
		
for element in lines:
    if element.find("Warning") != -1:    # write the element in find function which you want to search in your log file  
       element= element.split('Cannot find RMS',1)         # this will split your list on the basis of parameter you pass in split function
       element= element[-1].split('Item  in  Plm',1)       # Again you can split your list to extract any particular Word or data you want to extract
       # For each element in our list,
       print(element[0])
       fh = open(plm_data_path,'a')                       # open text file
       fh.write(""+element[0]+"\n")                      # write the list in text file
       fh.close()
