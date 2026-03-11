def calculate_gc_content(sequence):
    sequence = sequence.upper()
    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / len(sequence)) * 100 if len(sequence) > 0 else 0


def read_fasta(file_path):
    sequences = {}
    with open(file_path, "r") as file:
        seq_id = ""
        seq = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if seq_id:
                    sequences[seq_id] = seq
                seq_id = line[1:]
                seq = ""
            else:
                seq += line
        if seq_id:
            sequences[seq_id] = seq
    return sequences


def analyze_fasta(file_path):
    sequences = read_fasta(file_path)
    print("Sequence_ID\tLength\tGC_Content(%)")
    for seq_id, seq in sequences.items():
        length = len(seq)
        gc = calculate_gc_content(seq)
        print(f"{seq_id}\t{length}\t{gc:.2f}")


if __name__ == "__main__":
    analyze_fasta("sample_sequences.fasta")