#BIFS617 Final Project Reading Sequences
#Developed by R. B. Govindan
#Date: 04-09-2019
import os,re
os.system('clear')
#This program reads and cleans the DNA sequences stored in FASTA format
def readSequence(file):
    #File location
    c= 0
    a='x'
    files = os.listdir()
    c1 = file in files
    if c1 == True:
      c=1
    while c==0:
        file = input("Enter a file name or enter q to quit :")
        c1=file in files
        if c1==True:
           c=1
        if file == 'q':
           a='q'
           c=1
        if a=='q':
          print("Try again later")
          return
    print("File found")
    # If located, Open file and read the content
    file_open = open(file,'r')
    sequence = file_open.read()
    file_open.close()
    # Splicing sequences
    I=re.finditer('>',sequence)
    s=list()
    for m in I:
     s += [m.start()]
    seq = list()
    for k in range(0,len(s)-1):
     seq.append(sequence[s[k]:s[k+1]])
    seq.append(sequence[s[-1]:len(sequence)])
    #Parsing sequences
    hea = list()
    Indseq = list()
    for J in seq:
     q=re.finditer('\n',J)
     for i in q:
       temp=J[0:i.end()]
       temp=temp.strip("\n")
       temp1=J[i.end():len(J)]
       temp1 = temp1.replace("\n","")
       hea.append(temp)
       Indseq.append(temp1)
       break

    
    return hea,Indseq

