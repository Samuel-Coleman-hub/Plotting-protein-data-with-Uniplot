def average_len(records):
    """Returns average protein length"""
    total = 0
    for i in range(len(records)):
        total = total + len(records[i])
    return total/len(records)

def average_len_taxa(records, depth):
    """Returns the average length for the top level taxa"""
    record_by_taxa = {}
    for r in records:
        taxa = r.annotations["taxonomy"][depth]
        record_by_taxa.setdefault(taxa, []).append(r)

    return {taxa:average_len(record) for (taxa, record) in record_by_taxa.items()}

def total_proteins(records, depth):
    """Returns the number of proteins of each type"""
    record_by_taxa = {}
    for r in records:
        taxa = r.annotations["taxonomy"][depth]
        record_by_taxa.setdefault(taxa, 0)
        record_by_taxa[taxa] = record_by_taxa[taxa] + 1

    return record_by_taxa
