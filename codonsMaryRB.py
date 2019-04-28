#BIFS617 Final Project
#Developed by R. B. Govindan
#Date: 04-26-2019

#-----------------------------------------------------------------
# Background
# This code can take multiple DNA sequences saved in a list
# and identify ORFs for each DNA sequence in all six frames


# Materials needed and their contributors

# The DNA sequences were read from a FASTA file and pruned for 
# artifacts;the list variable "g2" contained DNA sequences; This part
# was developed by Tracy Ficor

# The ORF is identified using the function Mary_ORFFinder 
# which was developed by Mary Friedman 


# Deliverables
# This function outputs for every sequence, the ORF in all six frames,
# their starting points, and their lenghts

# Use of deliverables to meet the project requirement
# The outputs were used in Scott's function to print the output in 
# the required format

#-----------------------------------------------------------------

def codingRegions(g2): 
    import Mary_ORFFinder, FrameGeneration
    # Initializing variables to store ORF (ORF_ALL), their starting
    # points (Location_All) and their length (Length_All)
    ORF_ALL=list()
    Location_All=list()
    Length_All=list()
    # Loops through every sequence to find ORF
    for k in g2:

      # Initialing variables for ORF, their location and lengths for 
      # individual sequences. Once calculated, they are transferred 
      # to the variables above this for loop that store this information
      # for all sequences

      Ind_ORF = list()
      Ind_Len = list()
      Ind_Pos = list()
      for frame in range(1,7): # Frame generation

        # If frame number > 3, (frame - 3) is treated as the frame number
        # This is just to calculate the position

        if frame<=3:
          frame1=frame
        else:
          frame1=frame-3

        # This generates sequence for a given frame

        seq = FrameGeneration.FrameGen(k,frame) 

        # sequence is fed into Mary code to calculate ORF

        Results = Mary_ORFFinder.contains_orf(seq)

        
        # Parsing output from Mary's code
        # only the ORF with positions that are integer multiples of 3
        # are regarded as true ORF in a given frame

        # Initializing variables for ORFs, their positions, and thier lengths,
        # that were identified in a frame. This information is transferred to variables
        # above the for loop that loops through the frame

        Frame_ORF=list()
        Frame_Pos=list()
        Frame_Len=list()
        triplet=list()
        for kk in Results:
          if kk[1]%3==0: # checks if the position is integer multiple of 3
            Frame_Len.append(len(kk[0])) #calculates and stores the length
            # stores the starting position
            if frame<=3: 
              Frame_Pos.append(kk[1]+1+frame1-1)
            else:
              Frame_Pos.append(-(kk[1]+frame-3))
            
            # Forms triplets using the nucleotides in the ORF and stores in Frame_ORF
            triplet=list()
            for j in range(0,len(kk[0]),3):
              if j<=len(kk[0]):
                triplet.append(kk[0][j:j+3])
            Frame_ORF.append(triplet)
        

        # ORF, lengths, and positions in a frame are transferred to sequence level storage 
        # variables
        Ind_ORF.append(Frame_ORF)
        Ind_Len.append(Frame_Len)
        Ind_Pos.append(Frame_Pos)
    
      # ORF, lengths, and position calculated in all six frames of 
      # a sequence are transferred to multiple sequence level variables
      Location_All.append(Ind_Pos)
      Length_All.append(Ind_Len)
      ORF_ALL.append(Ind_ORF)
    return  ORF_ALL,Location_All,Length_All #returns ORF, Position, and length