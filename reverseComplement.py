#BIFS617 Final Project Identifying Open Reading Frames (ORF)
#Developed by R. B. Govindan
#Date: 04-09-2019
import os,re,math
#This function generates reverse complement of a given DNA sequence
def reverseComplement(s):
 s=s.upper()
 s1=s
 s1=s1.replace('A','t')
 s1=s1.replace('T','a')
 s1=s1.replace('C','g')
 s1=s1.replace('G','c')
 s1=s1.upper()
 s1=s1[::-1]
 return s1