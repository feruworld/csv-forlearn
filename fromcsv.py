import pandas as pd

filename = 'data.csv'
df = pd.read_csv(filename)

# random shuffle
df = df.sample(frac=1)

for i, row in df.iterrows():
    print(row['読み'])
    var = input()
    print(row['漢字'])
    if var == "end":
        exit(0)
    print()