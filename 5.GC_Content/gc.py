def count_mio(string : str):
    
    return (string.count('C') + string.count('G'))/len(string) *100


def gc(fasta_path):
    fasta = open(fasta_path,'r')
    fasta_dict = dict()
    last_fasta = ''
    for line in fasta:
        trimline = line.strip()
        if trimline[0] == '>':
            fasta_dict[trimline] = ''
            last_fasta = trimline
        else:
            fasta_dict[last_fasta] += trimline
    maxId = ' '
    maxValue = -1
    for key in fasta_dict:
        count = count_mio(fasta_dict[key])
        if(count > maxValue):
            maxValue = count
            maxId = key

    return '{name}\n{maxValue}'.format(name = maxId[1:],maxValue =  maxValue)

print(gc('rosalind_gc.txt'))
