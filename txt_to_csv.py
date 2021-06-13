import pandas as pd

read_file = pd.read_csv (r'bewertungen.txt')
read_file.to_csv (r'deneme.csv', index=None)