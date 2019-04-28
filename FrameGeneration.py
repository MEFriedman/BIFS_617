#BIFS617 Final Project Generates Frames
#Developed by R. B. Govindan
#Date: 04-09-2019
import os,reverseComplement
#This function generates sequence that corresponds to the given frame n
def FrameGen(s,k):
   if k<=3:
     s1=s[k-1:len(s)]
   elif k>3:
     k1=k-4
     ss=reverseComplement.reverseComplement(s)
     s1=ss[k1:len(ss)]
   return s1 # Contains the sequence in the given Frame k