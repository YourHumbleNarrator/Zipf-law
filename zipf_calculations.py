import os

import numpy as np
import asyncio

from src.utils import (
    read_files,
    tokenize_text,
    create_frequency_table,
    check_zipf_law,
    create_concurrence_graph,
    get_language_core,
    find_most_useful_words,
    find_most_common_nouns
)


def main():
    # TODO: wczytać pliki funkcją, zapisać wyniki (tabelki, wyznaczniki) do plików json bo na tym polega podobno to całe API
    # TODO: tutaj też możemy tworzyć i zapisywać pliki z wykresików do folderu plots
    file_list = read_files("Data")
    list_of_texts = [x[1] for x in file_list]
    list_of_tokens = [tokenize_text(text) for text in list_of_texts]
    flat_list = []
    for sublist in list_of_tokens:
        for token in sublist:
            flat_list.append(token)
    print(len(flat_list))

    freq_table = create_frequency_table(flat_list)
    print(freq_table.head())

    check_zipf_law(freq_table)
    concurrence_graph = create_concurrence_graph(flat_list)
    language_core = get_language_core(concurrence_graph)
    # find_most_useful_words(freq_table)
    english_words = asyncio.run(find_most_common_nouns(freq_table))
    # print(english_words)

if __name__ == "__main__":
    main()
