import json
from unicodedata import normalize
from datetime import datetime

IN_FILE_PATH = "train_data.txt"
OUT_FILE_PATH = "frequencies.json"
HISTORY_FOLDER_PATH = "History/"

symbols_to_omit = ",.;:',?!()[]{}\/" + '"' + "0123456789"

def parse_data():
    text = None
    with open(IN_FILE_PATH, "r") as f:
        text = f.read().strip().lower()
        text = normalize('NFKD', text).encode('ascii','ignore').decode("utf-8")

    for i in symbols_to_omit:
        text = text.replace(i, "")
        text = text.replace("\n", " ")

    return text

def store_frequencies():
    freq = None
    with open(OUT_FILE_PATH, "r") as f:
        freq = json.loads(f.read())

    with open(HISTORY_FOLDER_PATH+str(datetime.now().strftime("%c"))+".json", "w") as f:
        f.write(json.dumps(freq, indent=4))
    
    words = parse_data().split(" ")
    parsed_words = []
    for i in words:
        word = i.strip()

        if "-" in word:
            hyphenated = word.split("-")
            parsed_words += hyphenated
        else:
            if word != "\n":
                parsed_words.append(word)

    # Store frequencies for each word
    for i in range(len(parsed_words)):
        word = parsed_words[i]
        if word not in freq.keys():
            freq[word] = {}

        if (i != len(parsed_words) - 1):
            next_word = parsed_words[i+1]
            if next_word not in freq[word].keys():
                freq[word][next_word] = 1
            else:
                freq[word][next_word] += 1
    
    # Store the word with highest frequency
    for word in parsed_words:
        sorting_key = lambda w: int(freq[word][w])
        freq_list = [i for i in freq[word].keys()]

        if "ORDERED" in freq_list:
            freq_list.remove("ORDERED")
        freq_list.sort(key=sorting_key, reverse=True)

        freq[word]["ORDERED"] = freq_list

    with open(OUT_FILE_PATH, "w") as f:
        f.write(json.dumps(freq, indent=4))

    with open(IN_FILE_PATH, "w") as f:
        f.write("")

store_frequencies()