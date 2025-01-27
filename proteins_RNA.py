####proteins

'''
Instructions
Translate RNA sequences into proteins.

RNA can be broken into three-nucleotide sequences called codons, and then translated to a protein like so:

RNA: "AUGUUUUCU" => translates to

Codons: "AUG", "UUU", "UCU" => which become a protein with the following sequence =>

Protein: "Methionine", "Phenylalanine", "Serine"

There are 64 codons which in turn correspond to 20 amino acids; however, all of the codon sequences and resulting amino acids are not important in this exercise. If it works for one codon, the program should work for all of them. However, feel free to expand the list in the test suite to include them all.

There are also three terminating codons (also known as 'STOP' codons); if any of these codons are encountered (by the ribosome), all translation ends and the protein is terminated.

All subsequent codons after are ignored, like this:

RNA: "AUGUUUUCUUAAAUG" =>

Codons: "AUG", "UUU", "UCU", "UAA", "AUG" =>

Protein: "Methionine", "Phenylalanine", "Serine"

Note the stop codon "UAA" terminates the translation and the final methionine is not translated into the protein sequence.

Below are the codons and resulting amino acids needed for the exercise
'''


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
