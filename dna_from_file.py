# DNA Analysis from File

with open("dna_sequence.txt", "r") as file:
    dna_sequence = file.read().strip()

dna_sequence = dna_sequence.upper()

count_A = dna_sequence.count("A")
count_T = dna_sequence.count("T")
count_C = dna_sequence.count("C")
count_G = dna_sequence.count("G")

total_bases = len(dna_sequence)
gc_content = ((count_G + count_C) / total_bases) * 100

print("DNA Sequence:", dna_sequence)
print("Total Bases:", total_bases)
print("A:", count_A)
print("T:", count_T)
print("C:", count_C)
print("G:", count_G)
print("GC Content: {:.2f}%".format(gc_content)),