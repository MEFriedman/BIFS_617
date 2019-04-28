##########################################################################
# Author: Tracy Ficor       BIFS 617 - Group ORF FINDER                  #
# Date: 4/26/19                                                          #
# Purpose of function: Create a function that reads in a user designated #
# file and prepare the information within the file for identifying ORFs  #
# The function should open the file, read, identify headers and sequences#
# remove new line characters and convert DNA to RNA and return to the    #
# main program.                                                          #
# Another function is here which prompts the user for a minimum ORF      #
# length.                                                                #
##########################################################################


import re
def prompt_for_min_ORF():
    # Ask user to input minimum orf, ask until at least minimum of 1 is achieved. 
    minOrf = 0
    while minOrf == 0:
        userOrfString = input("Please input the ORF minimum length or press enter to use the default [50]: ")
        userOrfInt = 0
        if userOrfString.isspace() or userOrfString == "":
            #If the user enters nothing we will use the default value of 50.
            userOrfInt = 50
        else:
            userOrfInt = int(userOrfString)   
        
        if userOrfInt > 0:
            minOrf = userOrfInt
        else:
            print("I'm sorry the ORF minimum must be greater than or equal to 1")
    return minOrf
    
def parser(file):
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
            # make sure seq is converted to DNA and uppercase
            line=re.sub('U','T',line.upper())
            line = re.sub(' ','',line)

            # create a combined string containing the nt for one species
            sequence= sequence + line.strip()
        line_num = line_num + 1
        lseq=sequence       
    seq.append(lseq)

    return header, seq
