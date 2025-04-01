# to identify splice sites within gene sequences
# and find the largest intron in a given sequence
import re
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
largest_intron = re.findall(r'GT\S+AG',seq)
print(largest_intron)  # This will print the largest intron found in the sequence
print(len(str(largest_intron))-4)  # This will print the length of the largest intron found in the sequence
