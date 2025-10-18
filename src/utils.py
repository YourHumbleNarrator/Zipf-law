import re
import os
import pandas as pd
from collections import Counter


def read_files(path):
    # TODO: iteruje po plikach w folderze zwraca liste krotek (nazwapliku,tekst)
    fileslist = []

    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith((".txt")) and name != "blacklist.txt":
                filepath = os.path.join(root, name)
                with open(filepath, mode='r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                pair = (filepath, content)
                fileslist.append(pair)

    return fileslist


def tokenize_text(text):
    # TODO: dzieli tekst na zdania, usuwa zbędne znaki, zwraca liste wyrazów
    text = re.sub(r'\b[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]{1,3}\.\b', '', text)  # simple abbreviations
    text = re.sub(r'\d+', '', text)  # digits
    text = re.sub(r'[^a-zA-ZáéíóúãõâêîôûàèìòùçÁÉÍÓÚÃÕÂÊÎÔÛÀÈÌÒÙÇ\s]', '', text)  # only english and portuguese letters
    text = re.sub(r'\s+', ' ', text).strip()  # multiple spaces
    text = text.lower()
    list_of_words = text.split()
    return list_of_words



def create_frequency_table(tokenslist):
    # TODO: tworzy dataframe z polami słowo, częstotliwość z listy tokenów
    frequencies = Counter(tokenslist)
    df = pd.DataFrame(frequencies.items(), columns=["word", "freq"])
    df = df.sort_values(by="freq", ascending=False).reset_index(drop=True)
    return df


def check_zipf_law(df):
    # TODO
    parameter = 0
    return {
        "parameter": parameter
    }


def create_concurence_graph():
    # TODO
    nodes = []
    edges = []
    return nodes, edges
