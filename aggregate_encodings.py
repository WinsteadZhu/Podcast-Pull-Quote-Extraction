import glob
import pickle

import settings


all_data = {}

for directory in settings.PQ_SAMPLES_DIRS:
    file_list = glob.glob("{}/*.pkl".format(directory.rstrip("/")))
    for fname in file_list:
        print(fname)
        with open(fname, "rb") as f:
            all_data.update(pickle.load(f))

with open("precomputed_pq_sentbert.pkl", "wb") as f:
    pickle.dump(all_data, f)