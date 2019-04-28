# Print out function for BIFS 617 Group Project
# WS HINDLE April 18, 2019
# rev. 1 - frame number corrected

def print_out(acc_lst, orf_lst, start_index_lst, lengths_lst):
    acc_num = 0

    # loops through the various accession numbers contained in the original FASTA file
    for acc in start_index_lst:
        frame_num = 0

        # loops through all six reading frames
        for frame in start_index_lst[acc_num]:
            start_num  = 0

            # loops through and prints the reading frame, start position and length of each ORF
            for start in start_index_lst[acc_num][frame_num]:               
                if start_index_lst[acc_num][frame_num][start_num] !='':
                    print(acc_lst[acc_num],'| FRAME =',frame_num + 1,'POS =', start_index_lst[acc_num][frame_num][start_num],'LEN =', lengths_lst[acc_num][frame_num][start_num])
                    codon_num = 0

                    # loops through and prints out the codons contained in the ORF
                    for codons in orf_lst[acc_num][frame_num][start_num]:
                        print(orf_lst[acc_num][frame_num][start_num][codon_num], end = ' ')
                        codon_num = codon_num + 1
                    print()
                start_num = start_num + 1
            frame_num = frame_num + 1
        acc_num = acc_num +1
    return()
'''
def main():
    # main function is provided only for testing purposes!!!
    G1 = [[[['ATG', 'CTA', 'CCG', 'TAG']], [], [], [], [], []], [[], [['ATG', 'ATC', 'ATA', 'ACA', 'TAA'], ['ATG', 'TCT', 'TAG']], [], [['ATG', 'TTA', 'TGA']], [], [['ATG', 'ATC', 'ATG', 'GGC', 'TGA']]]]
    G2 = [[[1], [], [], [], [], []], [[], [17, 38], [], [-40], [], [-45]]]
    G3 = [[[12], [], [], [], [], []], [[], [15,9], [], [9], [], [15]]]
    acc_lst = ['> sequence1', '> sequence2']
    print_out(acc_lst, G1, G2, G3)

main()
'''
    
