import random
import json
import polars as pl
from pathlib import Path
CARDS_FILE = Path("./data/tarot-images.json")
ELEMENTS_FILE = Path("./data/contexts.json")
OUTPUT_FILE = Path("./data/sample.json")
N_SAMPLES = 10000
def reading_json(path):
    """Load a JSON file and return its contents."""
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)
def generating_numbers(df_1, df_2, n=N_SAMPLES):
    """Return random indices for cards and elements."""
    card_indices = [random.randint(0, df_1.shape[0] - 1) for _ in range(n)]
    element_indices = [random.randint(0, df_2.shape[0]-1) for _ in range(n)]
    return card_indices, element_indices

def prepare_data(df_cards, df_elements, card_indices, element_indices):
    """Create a list of dictionaries with selected card-element pairs."""
    data = []
    for c_idx, e_idx in zip(card_indices, element_indices):
        data.append({
            "card": df_cards['name'][c_idx],
            "element": df_elements['title'][e_idx],
            "description": df_elements['description'][e_idx]
        })
    return data

def write_jsonl(data, output_path):
    """Write a list of dicts to a JSONL file."""
    with output_path.open("w", encoding='utf-8') as f:
        json.dump(data,f, ensure_ascii=False,indent=2)
def main():
    data_cards = reading_json(CARDS_FILE)
    data_elements = reading_json(ELEMENTS_FILE)
    df_cards = pl.DataFrame(data_cards['cards'])
    df_elements = pl.DataFrame(data_elements['elements'])
    card_indices, element_indices = generating_numbers(df_cards, df_elements)
    mixed_data = prepare_data(df_cards, df_elements, card_indices, element_indices)
    write_jsonl(mixed_data, OUTPUT_FILE)
    print(f" {len(mixed_data)} combinations saved to {OUTPUT_FILE}")
if __name__ == "__main__":
    main()
