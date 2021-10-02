from Bio import SeqIO
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np


def read_seq(file):
    return SeqIO.parse(file, "fasta")


def get_dna_counts(data):
    seqs = []
    for idx, seq in enumerate(data):
        if idx < 2:
            seqs.append(seq.seq)

    for sq in seqs:
        count = Counter(sq)
        dna = ["A", "T", "C", "G"]
        dna_counts = {}
        for key, val in count.items():
            if key in dna:
                dna_counts[key] = val
        print(dna_counts)
        plt.bar(dna_counts.keys(), dna_counts.values())
    plt.show()
    return dna_counts



def main():
    file = "scripts/data/covid/data.fasta"
    data = read_seq(file)
    get_dna_counts(data)


if __name__ == "__main__":
    main()
