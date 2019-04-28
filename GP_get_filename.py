# BIFS 617 (Group Project) Read Data Function
# Walter Scott Hindle - April 22, 2019

import os

def get_filename(file_type):  # Gets the filename and does error trapping for
    flag =1          # invalid file pathsa nd wrong extension types
    fail_count = 0
    
    path = '/Desktop/Python Working Directory/BIFS 617 - Group Project/'
    while flag:
        my_string = "Enter the name of a " + file_type + " file for open reading frame extraction? (e.g. cat." + file_type + " ) \n"
        file=input(my_string)      
        if os.path.exists(file):
            ext_len = len(file_type)
            if file[-ext_len:]== file_type:
                flag=0
            else:
                print("Please enter a file name that has a \." + file_type + " extension.")
                fail_count = fail_count + 1
        else:
            print("File not found!")           
            fail_count = fail_count + 1           
        if fail_count == 5:
            print("Exiting: You did not enter a valid filename!")
            file="Invalid"
            flag=0
            
    return file
                       
'''   
def read_fasta(filename):
    
    my_file = open(filename)  
    my_file_contents1 = my_file.read().rstrip("\n").replace(" ","")
    my_file.close()

    # creates a new fasta file white space and newline char removed
    # for possible future use

    my_new_file = open("GroupProjectFile.fasta", "w")
    my_new_file.write(my_file_contents1)
    my_new_file.close()
    
    return (my_file_contents1)
       

def main():

    name = get_filename("txt")
    seq_data = read_fasta(name)
    
main()
'''
