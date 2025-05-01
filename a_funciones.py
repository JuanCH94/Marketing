
import pandas as pd
import re

def clean(title):
    match = re.search(r"\((\d{4})\)\s*$", title)
    year = match.group(1) if match else None
    title_clean = re.sub(r'\s*\(.*?\)', '', title).strip()
    return pd.Series([title_clean, year])

