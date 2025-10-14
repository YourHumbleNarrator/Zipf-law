import pandas as pd
from collections import Counter


def read_files(filepath):
    # TODO: iteruje po plikach w folderze zwraca liste krotek (nazwapliku,tekst)
    files = []

    return files


def tokenize_text(text):
    # TODO: dzieli tekst na zdania, usuwa zbędne znaki, zwraca liste wyrazów
    text = text.lower()


def create_frequency_table(tokenslist):
    # TODO: tworzy dataframe z polami słowo, częstotliwość z listy tokenów
    frequencies = Counter(tokenslist)
    df = pd.DataFrame(frequencies, columns=["word", "freq"])


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
