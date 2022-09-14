import pandas as pd

input_filename = 'data.csv'
save_filename = 'anki.csv'

df = pd.read_csv(input_filename)
df[['読み', '漢字']].to_csv(save_filename, header=False, index=False)