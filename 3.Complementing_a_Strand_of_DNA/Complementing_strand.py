def reverse_sequence(dna_path:str)->str:
    dna=open(dna_path,"r")
    return dna.read()[::-1].strip()

complemet = dict(A='T',T='A',C='G',G='C')

def complement_sequence(dna_path:str)->str:
    sequence = reverse_sequence(dna_path)
    sequence = list(sequence)
    for nucleotide in enumerate(sequence):
        index = nucleotide[0]
        base = nucleotide[1]
        sequence[index] = complemet[base]
    return "".join(sequence)

print(complement_sequence('rosalind_revc.txt'))