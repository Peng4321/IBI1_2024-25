import re
# to identify the sequence of the gene, and select the gene that contains the TATA box

# Define the input and output file paths which may easier to edit
input_file_path = r"C:\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file_path = r"C:\Users\彭大扬\OneDrive - International Campus, Zhejiang University\桌面\IBI\IBI1_2024-25\Practical7\tata_genes.fa.txt"

# Read the input file and extract gene sequences containing TATA box
tata_pattern = re.compile(r'TATA[AT]A[AT]')
gene_name = ''
gene_seq = ''
with open(output_file_path, 'w') as output_file:
    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            if line.startswith('>'):
                if gene_seq and tata_pattern.search(gene_seq):
                    output_file.write(f">{gene_name}\n{gene_seq}\n")
                gene_name = re.findall(r'gene:(.+?)\s', line)
                if gene_name:
                    # change the type of gene_name from list to string
                    gene_name = gene_name[0]
                else:
                    gene_name = ''
                gene_seq = ''
            else:
                gene_seq += line.strip()
    if gene_seq and tata_pattern.search(gene_seq):
        output_file.write(f">{gene_name}\n{gene_seq}\n")