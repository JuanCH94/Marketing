
import pandas as pd
import re

def clean(title):
    match = re.search(r"\((\d{4})\)\s*$", title)
    year = match.group(1) if match else None
    title_clean = re.sub(r'\s*\(.*?\)', '', title).strip()
    return pd.Series([title_clean, year])


def separar(conexion):
    query = """
        SELECT
            SUBSTR(title, 1, INSTR(title, '(') - 2) AS movie_title,
            SUBSTR(title, INSTR(title, '(') + 1, INSTR(title, ')') - INSTR(title, '(') - 1) AS Year, genres
        FROM movies
    """
    return pd.read_sql_query(query, conexion)


