import polars as pl
df=pl.read_ndjson('tarot-deck.jsonl')
print(df.head())
print(df.shape)
print(df.describe())
df_unique = df.unique(subset=["card_name"])
df_unique.write_ndjson('tarot-deck-unique.jsonl')