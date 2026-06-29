from Bio import SeqIO
for record in SeqIO.parse("neuron.fasta","fasta"):
    print("RNA:", record.seq.transcribe())
    print("Protein:",record.seq.translate())
