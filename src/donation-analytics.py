#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 13:23:14 2018

@author: bryanquigley
"""
from __future__ import division
import numpy as np
from collections import defaultdict

file = open("input/percentile.txt", "r")
percentile = int(file.read())
file.close

file = open("input/itcont.txt", "r") 
itcont = file.readlines() 
entries = len(itcont)

donorlist = []
recipient_dict = defaultdict(list)
output = [] 

fileoutput = open("output/repeat_donors.txt", "w") 

for i in range(0,entries):
    donation_data = itcont[i].split('|')
    donor = [donation_data[7], donation_data[10][0:5]]
    recipient_key = str(donation_data[0])+str(donation_data[10][0:5])+str(donation_data[13][4:8])
    if not donation_data[15]:
        if not donorlist:
            donorlist.append(donor)
        else:
            if donor in donorlist:
                if not recipient_dict:
                    recipient_dict.update({recipient_key: [[int(donation_data[14])]]} ) 
                    output.append( [donation_data[0], donation_data[10][0:5], donation_data[13][4:8], int(donation_data[14]), int(donation_data[14]), 1] )
                    fileoutput.write(str(output[-0][0])+'|'+str(output[0][1])+'|'+str(output[0][2])+'|'+str(output[0][3])+'|'+str(output[0][4])+'|'+str(output[0][5])+'\n')
                    
                else:
                    if recipient_key in recipient_dict:
                        recipient_dict[recipient_key].append([int(donation_data[14])])
                        percentile_rank = int(np.ceil(percentile/100*len(recipient_dict[recipient_key])))
                        output.append( [donation_data[0], donation_data[10][0:5], donation_data[13][4:8], sum(sum(recipient_dict[recipient_key], [])), recipient_dict[recipient_key][percentile_rank-1][0], len(recipient_dict[recipient_key])] )
                        fileoutput.write(str(output[-1][0])+'|'+str(output[-1][1])+'|'+str(output[-1][2])+'|'+str(output[-1][3])+'|'+str(output[-1][4])+'|'+str(output[-1][5])+'\n')
                        
                    else:
                        recipient_dict.update({recipient_key: [[int(donation_data[14])]]} ) 
                        output.append( [donation_data[0], donation_data[10][0:5], donation_data[13][4:8], int(donation_data[14]), int(donation_data[14]), 1])  
                        fileoutput.write(str(output[-1][0])+'|'+str(output[-1][1])+'|'+str(output[-1][2])+'|'+str(output[-1][3])+'|'+str(output[-1][4])+'|'+str(output[-1][5])+'\n')
            else:
                donorlist.append(donor)       
    
fileoutput.close()    
