import os
import pickle

import settings
from sentence_transformers import SentenceTransformer

from utils.pq_preprocessing import preprocess_pull_quotes_map


articles_data_map = preprocess_pull_quotes_map(directories=settings.PQ_SAMPLES_DIRS)

sent_encoder = SentenceTransformer("bert-base-nli-mean-tokens")

for txt_file, article in articles_data_map.items():
    print(txt_file)
    assert txt_file[-3:] == "txt"
    pkl_file = txt_file[:-3] + "pkl"
    if os.path.isfile(pkl_file) and os.path.getsize(pkl_file) > 0:
        print("DONE")
        continue

    sentences = article['sentences']
    encodings = sent_encoder.encode(sentences, show_progress_bar=True)
    assert len(sentences) == len(encodings)
    sent_encs = dict(zip(sentences, encodings))
    with open(pkl_file, "wb") as f:
        pickle.dump(sent_encs, f)
