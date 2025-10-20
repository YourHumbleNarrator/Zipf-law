import os
import json
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
    i=0
    for sublist in list_of_tokens:
        print(f'{file_list[i][0]}: {len(sublist)}')
        i+=1
        for token in sublist:
            flat_list.append(token)
    print(f"Corpus contains: {len(flat_list)} words.")

    freq_table = create_frequency_table(flat_list)
    print(freq_table.head())
    freq_table_json = freq_table.to_dict(orient="records")

    with open("results/frequency_table.json", "w", encoding="utf-8") as f:
        json.dump(freq_table_json, f, ensure_ascii=True, indent=4)

    zipf_stats = check_zipf_law(freq_table)
    with open("results/zipf_stats.json", "w", encoding="utf-8") as f:
        json.dump(zipf_stats, f, ensure_ascii=False, indent=4)

    concurrence_graph = create_concurrence_graph(flat_list)
    language_core = get_language_core(concurrence_graph)
    with open("results/language_core.json", "w", encoding="utf-8") as f:
        json.dump([{"word": w, "neighbors": n} for w, n in language_core], f, ensure_ascii=True, indent=4)

    useful_words = find_most_useful_words(freq_table)
    with open("results/useful_words.json", "w", encoding="utf-8") as f:
        json.dump(useful_words, f, ensure_ascii=True, indent=4)

    english_nouns = asyncio.run(find_most_common_nouns(freq_table))
    print(english_nouns)
    with open("results/common_nouns.json", "w", encoding="utf-8") as f:
        json.dump([{"English": e, "Portuguese": p} for e, p in english_nouns], f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
