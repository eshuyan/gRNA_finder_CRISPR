# -*- coding: utf-8 -*-
"""
Created on Wed May 11 14:47:04 2016

@author: jingyan
"""

def reverse_compliment(sequence):
    D = {'A':'T',
         'T': 'A',
         'G': 'C',
         'C': 'G'}
    reverse = sequence[::-1]
    reverse_compliment = ''
    for nucleatide in reverse:
        reverse_compliment += D[nucleatide]
    return reverse_compliment
    
def GC(sequence):
    number_GC = 0
    for nucletide in sequence:
        if nucletide == 'G' or nucletide == 'C':
            number_GC += 1
    return float(number_GC)/len(sequence)
            
import re
def gRNA(sequence):  
    pattern = '.{19}[^C].GG'
    gRNA1 = re.findall(pattern, sequence)
    gRNA2 = re.findall(pattern, reverse_compliment(sequence))
    if gRNA2:
        for item in gRNA2:
            gRNA1.append(item)
    gRNA = []
    for grna in gRNA1:
        if GC(grna) < 0.8 and GC(grna) > 0.4:
            gRNA.append(grna)
    return gRNA
            
def check_DNA(sequence):
    
    DNA = ['A', 'T', 'G', 'C']
    n = 0
    for nucleatide in sequence:
        if nucleatide in DNA:
            n += 1
        else:
            return False
            break
        if n == len(sequence):
            return True

sequence = raw_input('Please input your sequences( up to 250bp)):\n')
sequence = sequence.upper()
if not check_DNA(sequence):
    print "Your sequences contain invalid symbol!"
elif len(sequence) > 250 or len(sequence) < 22:
    print "Your sequences too long or too short!"
else:
    print "Robot is looking for gRNA for you!"
    print "-----------------------------------\n"
    gRNA = gRNA(sequence)
    for seq in gRNA:
        print seq
        print '\n'
            
            
        



    
    
        
        