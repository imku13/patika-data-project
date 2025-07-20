import csv

input_file = 'datasets/bolgeler.csv'
output_file = 'datasets/bolgeler2.csv'

with open(input_file, mode='r', encoding='utf-8-sig') as infile, \
        open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        cleaned_row = [cell.lstrip("b'").rstrip("'") if cell.startswith("b'") else cell for cell in row]
        writer.writerow(cleaned_row)

print("Done.")
