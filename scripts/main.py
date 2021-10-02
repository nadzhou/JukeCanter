from Bio import SeqIO
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    data = SeqIO.parse("scripts/data/covid/data.fasta", "fasta")
    seqs = []
    for sq in data:
        seqs.append(str(sq.seq))
    count = Counter(str(seqs))

    dna = ["A", "T", "C", "G"]
    dna_counts = {}
    for key, val in count.items():
        if key in dna:
            dna_counts[key] = val
    print(dna_counts)
    plt.bar(dna_counts.keys(), dna_counts.values())
    plt.show()



if __name__ == "__main__":
    main()