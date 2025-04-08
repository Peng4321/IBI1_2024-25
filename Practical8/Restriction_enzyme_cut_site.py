#the code aims to detect the restriction enzyme cut site in a given DNA sequence.
#and show the position of the cut site.
import re
def find_cut_site(dna_sequence, enzyme_sequence):
    # Find the position of the enzyme sequence in the DNA sequence
    position = dna_sequence.find(enzyme_sequence)
    # to check if the sequence is valid
    if re.match("^[ATCG]*$", dna_sequence):
        if position != -1: 
            return position + 1
        else:
            print("Enzyme sequence not found in the DNA sequence.")
            return None
    else:
        print("Invalid DNA sequence. Please enter a valid DNA sequence.")
        return None


#example
dna_sequence = "ATCGTAGCTAGCTACGTGTAGCTAGCTAGC"
enzyme_sequence = "ACGT"
cut_site = find_cut_site(dna_sequence, enzyme_sequence)
print(f"Cut site position: {cut_site}")  # Output: Cut site position: 12