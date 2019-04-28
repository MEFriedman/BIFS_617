#Developed by R. B. Govindan
#Date: 04-10-2019
import os,re
#os.system('clear')
#This program takes parses the DNA sequences into different frames and searches for ORFs
import FrameGeneration, M_ORFFinder
def codons(s):
  G1=list()
  G2=list()
  G3=list()
  for seq in s:
    A1 = list()
    A2 = list()
    A3 = list()
    for frame in range(1,7):
      s1 = FrameGeneration.FrameGen(seq,int(frame))
      #a1,a2,a3 = identifyORF.identifyORF(s1)
      a1,a2,a3 = M_ORFFinder.identifyORF(s1)
      print("M_ORFFinder was called and returned three items:")
      print(a1)
      print(a2)
      print(a3)
      print("")
      if frame>3 and a2 !=[]:
         for ik in range(0,len(a2)):
           a2[ik]=-1*(a2[ik]+frame-3)
      elif frame<=3 and a2!=[]:
          for ik in range(0,len(a2)): 
            a2[ik] = a2[ik] + frame
      A1.append(a1)
      A2.append(a2)
      A3.append(a3)
    G1.append(A1)
    G2.append(A2)
    G3.append(A3) 
  return G1,G2,G3