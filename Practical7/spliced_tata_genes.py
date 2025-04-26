#the overall goal of the script is to find the genes that have a specific splice combination and TATA box in their sequence and tell the numbers of TATA boxes in the sequence
#the program will read the file line by line 
#if start with >,find the name of the gene
#if not start with >, add the sequence to the gene_seq variable
#when meet the next >( means the last gene sequenc has been fully added),check the gene_seq variable for the TATA box and the splice combination
import re

splice_combination=input("Please enter the splice combination: ") #get the splice combination from the user
splice_donor=splice_combination[0:2] #get the splice donor from the splice combination
splice_acceptor=splice_combination[2:4] #get the splice acceptor from the splice combination

tata_pattern = re.compile(r'TATA[AT]A[AT]')
input_filename = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_filename = f"{splice_combination}_spliced_genes.fa"

with open(input_filename, 'r') as fasta_file, open(output_filename, 'w') as out_file:
    gene_name = None
    gene_seq = ""

    for line in fasta_file:
        if line.startswith(">"):  
            if gene_name and tata_pattern.search(gene_seq): 
                tata_count = len(tata_pattern.findall(gene_seq))
                if re.search(splice_donor + r".+" + splice_acceptor, gene_seq):
                    out_file.write(f">{gene_name} TATA count: {tata_count}\n{gene_seq}\n")
            
            gene_name = re.search(r'gene:(\S+)', line)
            gene_name = gene_name.group(1) 
            gene_seq = ""  
        
        else: 
            gene_seq += line.strip()
   
   
#to check the last gene
    if gene_name and tata_pattern.search(gene_seq):
        tata_count = len(tata_pattern.findall(gene_seq))
        if re.search(splice_donor + r".+" + splice_acceptor, gene_seq):
            out_file.write(f">{gene_name} TATA count: {tata_count}\n{gene_seq}\n")



