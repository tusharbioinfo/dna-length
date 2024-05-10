dna_len = 0
gc_count = 0
with open('ltf', 'r') as fasta:
    for line in fasta:
        if line.startswith('>'):
            print('sequence header: ' + line)
            continue

        dna_len += len(line.strip('\n'))
        print(len(line.strip('\n')))
        for c in line:
            if c == "C" or c == "G":
                gc_count += 1
print (dna_len)
print(gc_count)