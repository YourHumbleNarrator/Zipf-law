import re
import os
import numpy as np
import pandas as pd
from collections import Counter
import networkx as nx
from googletrans import Translator
import nltk


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
    frequencies = df['freq'].tolist()
    zipf_law = [(x+1)*frequencies[x] for x in list(df.index)]
    av = np.average(zipf_law)
    st_dev = np.std(zipf_law)
    var = np.var(zipf_law)

    parameter = 0
    return {
        "average": av,
        "stddev": st_dev,
        "variance": var,
    }

def create_concurrence_graph(list_of_tokens):
    # TODO zwraca rdzeń języka jako listę krotek - ('słowo', liczba sąsiadów)
    G = nx.Graph()
    G.add_nodes_from(list_of_tokens)
    for i in range(len(list_of_tokens) - 1):
        G.add_edge(list_of_tokens[i], list_of_tokens[i+1])

    return G

def get_language_core(G):
    number_of_neighbors = [(x, len(list(G.neighbors(x)))) for x in G.nodes()]
    number_of_neighbors = sorted(number_of_neighbors, key=lambda x: x[1], reverse=True)
    language_core = number_of_neighbors[:50]
    return language_core

def find_most_useful_words(freq_table):
    words_to_learn = []
    print(np.sum(freq_table['freq'].tolist()[:3]))
    for i in range(len(freq_table['freq'].tolist())):
        if np.sum(freq_table['freq'].tolist()[:i]) / np.sum(freq_table['freq'].tolist()) < 0.9:
            words_to_learn.append(freq_table['word'].tolist()[i])
        else: break
    return words_to_learn

async def find_most_common_nouns(freq_table):
    nltk.download('averaged_perceptron_tagger_eng')
    english_words = []
    async with (Translator() as translator):
        for word in freq_table['word'].tolist():
            result = await translator.translate(word, src='pt', dest='en')
            text = result.text
            ans = nltk.pos_tag([text])
            val = ans[0][1]
            pattern1 = re.compile("\b[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]{1,3}\b")
            if (val == 'NN' or val == 'NNS' or val == 'NNPS' or val == 'NNP') and not pattern1.match(text):
                english_words.append(text)
            if len(english_words) >= 50:
                break

    return english_words
