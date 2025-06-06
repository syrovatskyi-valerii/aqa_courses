import csv

def read_csv_rows(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        return list(reader)

rows1 = read_csv_rows('random.csv')
rows2 = read_csv_rows('random-michaels.csv')

header = rows1[0]

all_rows = rows1[1:] + rows2[1:]

unique_rows = list({tuple(row) for row in all_rows})

with open('result_compare.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(unique_rows)