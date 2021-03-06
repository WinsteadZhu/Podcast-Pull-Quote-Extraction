import os


HEADLINE_FNAME 		= "datasets/headlines_vs_clickbait/non_clickbait_data"

CLICKBAIT_FNAME 	= "datasets/headlines_vs_clickbait/clickbait_data"

HEADLINE_POPULARITY_FNAME = "datasets/headline_popularity/News_Final.csv"

CONCRETENESS_FNAME 	= "datasets/word_sets/Concreteness_ratings_Brysbaert_et_al_BRM.txt"

AFFECT_FNAME 		= "datasets/word_sets/Ratings_Warriner_et_al.csv"

EASY_WORDS_FNAME	= "datasets/word_sets/easy_words.txt"

MODEL_SAVE_DIR      = "./ml_models/"

PRECOMPUTED_SBERT_EMBEDDINGS_FNAME = "./ml_data/precomputed_pq_sentbert.pkl" #None
if not os.path.exists(PRECOMPUTED_SBERT_EMBEDDINGS_FNAME):
	PRECOMPUTED_SBERT_EMBEDDINGS_FNAME = None

PRECOMPUTED_HANDCRAFTED_EMBEDDINGS_FNAME = "./ml_data/precomputed_handcrafted_embeddings.pkl"

base_pq_directory = "./corpora/"

assert base_pq_directory != "directory_to_data/"

PQ_SAMPLES_DIRS		= [
	f"{base_pq_directory}national-post/",
	f"{base_pq_directory}intercept/",
	f"{base_pq_directory}ottawa-citizen/",
	f"{base_pq_directory}cosmo/",
]
