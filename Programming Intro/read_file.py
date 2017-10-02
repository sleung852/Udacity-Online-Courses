import unicodecsv

date_file = '/Users/See/Downloads/enrollments.csv'

with open(date_file, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)


enrollments[0]
