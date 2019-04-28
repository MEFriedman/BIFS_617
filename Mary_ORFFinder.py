# Finds Open Reading Frames (ORF) in the provided Nucleotide Sequence.  Returns all ORFs for reading
# frames 1-3.  To search through reading frames -1 to -3, you must reverse-complement the input 
# Nucleotide Sequence, then call this function, then negate the start positions returned as output;
# this function has no concept of reading frames -1 to -3; that is the caller's responsibility.
# Input: Nucleotide Sequence
# Output: A list of tuples.  Each tuple contains (text of ORF match, start location of ORF match)
#Developed by Mary E Friedman
import re
import os
import sys
def contains_orf(sequence_text):
    #Set TESTING_MODE to true to print extra information to the console (for testing)
    TESTING_MODE = False
    HIDE_INTERNAL_MATCHES = True
    sequence_text = sequence_text.upper()
    #Regex is searching for the normal codon as well as the reverse complement.

    #Replacing "T" with "[TU]" allows us to search for either DNA/RNA
    #Note: For lists of length 1, surround with [square brackets]
    START_CODON_LIST = (["ATG"])
    END_CODON_LIST = ("TAA", "TAG", "TGA")
    start_codon_regex = ""
    end_codon_regex = ""

    for codon in START_CODON_LIST:
        start_codon_regex += codon + "|"

    for codon in END_CODON_LIST:
        end_codon_regex += codon + "|"

    #Above loops leave an extra | at the end of the regex
    end_codon_regex = end_codon_regex[0:len(end_codon_regex) - 1]
    start_codon_regex = start_codon_regex[0:len(start_codon_regex) - 1]
    end_codon_regex.replace("T", "[TU]")
    start_codon_regex.replace("T", "[TU]")
    # The regular expression here is complicated, but can be broken into three parts
    # Line 1:  Do not consume matched text when matching it (to allow finding of
    #          matches within matches):  (?=(
    # Line 2:  Match a start codon
    # Line 3:  Match any set of three nucleotides: [ATCGU]{3}
    #          However, do NOT match any of the end codons: (?!( + end_codon + ))
    #          Do this 0 or more times:  ( ... )*
    # Line 4:  Match an end codon
    # Line 5:  Close parenthesis from line 1
    # Note:    An unfortunate side effect of line 1, is that since the text is not
    #          consumed, the finditer results return a length of zero (since zero
    #          text was consumed). Luckily, finditer does return correct start
    #          locations, while findall returns the text at that location (which
    #          we can use the len() function on to determine the end location.
    regex = ("(?=(" +
             "(" + start_codon_regex + ")" +
             "((?!(" + end_codon_regex + "))[ATCGU]{3})*" +
             "(" + end_codon_regex + ")" +
             "))")

    orf_iter = re.finditer(regex, sequence_text)
    orf_all = re.findall(regex, sequence_text)

    results=list()
    count=0
    for match in orf_iter:
        #orf_all is a list of tuples, where the first item in the tuple is the whole matched text
        match_text=orf_all[count][0]
        results.append((match_text, match.start()))
        #Test to make sure that the start value + len() matches the regex findall output
        if (TESTING_MODE):
            print("Adding to results, a match that starts at index " + str(match.start()) + ": " + match_text)
            test_value = sequence_text[match.start():match.start() + len(match_text)]
            if (test_value == match_text):
                print("VALIDATED (start/end indexes are correct)")
            else:
                print("ERROR: Start/end indexes do not match")
                sys.exit(1)
        count += 1

    if(HIDE_INTERNAL_MATCHES):
        newResults = list()
        for result in results:
            is_internal = False
            for result2 in results:
                if (result[0] != result2[0] and result[1] != result2[1]):
                    #Check if results 2 starts before result, and ends after result
                    result_end = result[1] + len(result[0])
                    result2_end = result2[1] + len(result2[0])
                    if (result2[1] <= result[1] and (result2_end >= result_end)):
                        #Also check to make sure they are in the same reading frame
                        offset = result[1] - result2[1]
                        if(offset % 3 == 0):
                            is_internal = True
                            if (TESTING_MODE):
                                print("Discarding " + str(result) + " because it is within " + str(result2))
                            break
            if (is_internal == False):
                newResults.append(result)
        results = newResults

    return results