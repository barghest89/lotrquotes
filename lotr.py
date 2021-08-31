import json
import random

with open('quotes.json') as f:
    data = json.load(f)
    quote_dict = random.choice(data)
    print(f"{quote_dict['quote']}\n")
    source = quote_dict['source']
    if source != "":
        print(f"- {source}")
    print(quote_dict['book'])