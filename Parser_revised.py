##########################################################################
# Author: Tracy Ficor       BIFS 617 - Group ORF FINDER                  #
# Date: 4/26/19                                                          #
# Purpose of function: Create a function that reads in a user designated #
# file and prepare the information within the file for identifying ORFs  #
# The function should open the file, read, identify headers and sequences#
# remove new line characters and convert DNA to RNA and return to the    #
# main program developed by Scott Hindle                                 #
##########################################################################

import re
def parser(file):
    # Ask user to input minimum orf, ask until at least minimum of 50 is achieved. 
    minOrf = 50
    count = 0
    while minOrf != count:
        userOrf = int(input("Please input the ORF minimum: "))
        if userOrf >= 50:
            minOrf = userOrf
            count = 50
        else:
            print("I'm sorry the ORF minimum must be greater than or equal to 50")
    # define lists, count numbers, and open file
    header = []
    seq = []
    myfile= open(file,'r')
    line_num = 0
    sequence=''
    # get headers and sequences and append lists
    for line in myfile:
        if line[0] == ">":
            # appends to the header list
            header.append(line.strip())
            if sequence != '':
                seq.append(sequence)
                sequence=''
            
        else:
            # make sure seq is converted to RNA and uppercase
            line=re.sub('U','T',line.upper())
            line = re.sub(' ','',line)

            # create a combined string containing the nt for one species
            sequence= sequence + line.strip()
        line_num = line_num + 1
        lseq=sequence       
    seq.append(lseq)

    return header, seq
