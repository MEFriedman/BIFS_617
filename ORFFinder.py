#BIFS617 Final Project Identifying Open Reading Frames (ORF)
#Developed by R. B. Govindan
#Date: 04-09-2019
import os,re
#This program takes DNA sequences as inputs and identifies ORF
def identifyORF(s):
  print(s)
  sc=['TAA','TAG','TGA']
  h=list()
  L=len(s)
  Q=list()
  count=0
  for k in range(0,L,3):
    if k+2<=L:
      count=count+1
      h.append(s[k:k+3])
      if s[k:k+3]=='ATG':
        Q.append(count)           
         
  
  seq=list()
  c=list()
  c1=list()
  if Q!=( ):
    for k in range(0,len(Q)):
      if k>len(Q):
       return seq,c,c1
      g=h[Q[k]-1:len(h)]
      sci=list()
      for i in sc:
        if i in g:
          I=g.index(i)
          sci.append(I)
      if sci !=():
        m=min(sci)
      else:
        m=len(g)
      seq.append(g[0:m+1])
      c.append((Q[k]-1)*3)
      c1.append((m+1)*3)
  return seq, c, c1   
  