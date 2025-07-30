import polars as pl

df = pl.read_parquet('hf://datasets/jtatman/tarot_dataset/data/train-00000-of-00001-7600cacde474200b.parquet')
print(df.head())
print(df.shape)
print(df.describe())
df=df.drop('image')
df.write_ndjson('tarot-deck.jsonl')
