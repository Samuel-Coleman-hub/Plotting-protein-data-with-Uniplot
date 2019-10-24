def average_len(records):
    total = 0
    for i in range(len(records)):
        total = total + len(records[i])
    return total/len(records)



