#BIFS617 Final Project Identifying Open Reading Frames (ORF)
#Developed by R. B. Govindan
#Date: 04-09-2019
import os,re
#os.system('clear')
#This program takes DNA sequences as inputs and identifies ORF
def identifyORF(s):
  seq=list()
  index = list()
  L=list()
  c=1
  begin=0
  while c==1:
    LA=list(range(begin,len(s),3))
    for i in list(range(begin,len(s),3)):
      triplet = s[i:i+3]
      if i+3>LA[-1]:
        c=0
        break
      if triplet == 'ATG':
        k=0
        for j in list(range(i,len(s),3)):
          triplet1 = s[j:j+3]
          if triplet1 == 'TAA' or triplet1 == 'TAG' or triplet1 == 'TGA':
            k=j
            break
          if k==0:
            L1=len(s)
          else:
            L1=k
          seq.append(s[i:L1-1])
          L.append(L1-i+1)
          index.append(i)
          if L1>=LA[-1]:
           c=0
           return seq,index,L
          else:
           begin=k
           I=i
  return seq,index,L  
