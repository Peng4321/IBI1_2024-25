import re
#to read the sequence and find the gene with TATA box
#to write the variables to enable the editing of the file
input_file_path = r"C:\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file_path = r"C:\Users\彭大扬\OneDrive - International Campus, Zhejiang University\桌面\IBI\IBI1_2024-25\Practical7\tata_genes.fa.txt"
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
                        output_file.write(gene_seq[i:i + line_length] + '\n')
            gene_name = re.findall(r'gene:(.+?)\s', line)
            if gene_name:
                gene_name = gene_name[0] #change the type of gene_name to string
            else:
                gene_name = ''
            gene_seq = ''
        else:
            gene_seq += line.strip() #add the sequence to the gene_seq variable
