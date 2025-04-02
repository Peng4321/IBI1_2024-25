#the program will read the file line by line 
#if start with >,find the name of the gene
#if not start with >, add the sequence to the gene_seq variable
#when meet the next >(means the last gene sequenc has been fully added),check the gene_seq variable for the TATA box 
#check the last gene seperately
import re
import re
#to read the sequence and find the gene with TATA box
#to write the variables to enable the editing of the file
input_file_path = r"Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file_path = r"tata_genes.fa"
line_length = 60
tata_pattern = re.compile(r'TATA[AT]A[AT]')
gene_name = ''
gene_seq = ''
with open(input_file_path, 'r') as input_file:
    for line in input_file:
        if line.startswith('>'):
            if gene_seq and tata_pattern.search(gene_seq):
                with open(output_file_path, 'a') as output_file:
                    output_file.write(f">{gene_name}\n")
                    for i in range(0, len(gene_seq), line_length):
                        output_file.write(gene_seq[i:i + line_length] + '\n') #output the sequence in lines of 60 characters
            gene_name = re.findall(r'gene:(.+?)\s', line)
            if gene_name:
                gene_name = gene_name[0] #change the type of gene_name to string
            else:
                gene_name=''
            gene_seq = ''
        else: 
            gene_seq += line.strip() #remove the new line character and add the sequence to gene_seq   
        
    if gene_seq and tata_pattern.search(gene_seq):
        output_file.write(f">{gene_name}\n")
        for i in range(0, len(gene_seq), line_length):
            output_file.write(gene_seq[i:i + line_length] + '\n')
 
