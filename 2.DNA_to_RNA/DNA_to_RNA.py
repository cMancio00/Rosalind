def dna_to_rna(dna_path)->str:
    dna=open(dna_path,"r")
    return dna.read().replace('T','U')

print(dna_to_rna('rosalind_rna.txt'))