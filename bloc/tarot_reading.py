import json
import polars as pl


def reading_json(name):
    with open(name,'r',encoding='utf-8') as f:
        data=json.load(f)
    return data
data_cards=reading_json('./data/tarot-images.json')
data_contexts=reading_json('./data/contexts.json')
cards=data_cards['cards']
elements=data_contexts['elements']
df_cards=pl.DataFrame(cards)
df_elements=pl.DataFrame(elements)