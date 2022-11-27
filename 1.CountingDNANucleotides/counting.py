def count()->str:
    dna=open("rosalind_dna.txt","r")
    dna_dict = dict(A=0,C=0,G=0,T=0)
    dna_string = dna.read()
    for nucleotide in dna_string:
        try:
            dna_dict[nucleotide] += 1
        except KeyError:
            dna.close()
    return '{A} {C} {G} {T}'.format(A=dna_dict['A'],C=dna_dict['C'],G=dna_dict['G'],T=dna_dict['T'])

