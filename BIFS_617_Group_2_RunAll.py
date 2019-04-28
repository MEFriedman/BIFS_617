
import Parser_revised, GP_get_filename, codonsMaryRB, Printout_Function

# Prompting User for filename
f = GP_get_filename.get_filename('txt') # the txt argument is for error checking purposes

# Reading sequence from file f (see line 1)
minORF = Parser_revised.prompt_for_min_ORF()
g1,g2 = Parser_revised.parser(f) #g1 contains accession numbers and g2 contains sequences

# Identifies coding regions in every sequence in all six frames
#G1 contains ORFs; G2 contains starting indexes; G3 contains the length of the ORFS
G1,G2,G3 = codonsMaryRB.codingRegions(g2)

#Printing output
Printout_Function.print_out(g1,G1,G2,G3,minORF)

