import pickle

from sentence_transformers import SentenceTransformer

import settings
from utils.pq_preprocessing import preprocess_pull_quotes

_precomputed_sent_encs = {}

articles_data = preprocess_pull_quotes(directories=settings.PQ_SAMPLES_DIRS)

sent_encoder = SentenceTransformer("bert-base-nli-mean-tokens")

for article in articles_data:
	print(article['url'])
	sentences = article['sentences']
	encodings = sent_encoder.encode(sentences, show_progress_bar=True)
	assert len(sentences) == len(encodings)
	_precomputed_sent_encs.update(zip(sentences, encodings))

pickle.dump(_precomputed_sent_encs, open("precomputed_pq_sentbert.pkl", "wb"))
