####proteins

aminoacids = [
    'Methionine',  # AUG
    'Phenylalanine', 'Phenylalanine',  # UUU, UUC
    'Leucine', 'Leucine',  # UUA, UUG
    'Serine', 'Serine', 'Serine', 'Serine',  # UCU, UCC, UCA, UCG
    'Tyrosine', 'Tyrosine',  # UAU, UAC
    'Cysteine', 'Cysteine',  # UGU, UGC
    'Tryptophan'  # UGG
]

nucleotides = [
    'AUG', 'UUU', 'UUC', 'UUA', 'UUG', 'UCU', 'UCC', 'UCA',
    'UCG', 'UAU', 'UAC', 'UGU', 'UGC', 'UGG'
]
stop_codons = {'UAA', 'UAG', 'UGA'}
def group_nucleotides(strand):
#creating list of separated group of nucleotides
    nucleotides_list = []
    for i in range (0,len(strand), 3):
        nucleotides_list.append(strand[i:i + 3])
    return nucleotides_list

def proteins(strand):
    protein_list = []
#creating list of proteins matching nocleotides strands
    for group in  group_nucleotides(strand):
        if group in nucleotides:
            index = nucleotides.index(group)
            protein_list.append(aminoacids[index])
        elif group in stop_codons:
            break
        # else:
        #     continue
    return protein_list
