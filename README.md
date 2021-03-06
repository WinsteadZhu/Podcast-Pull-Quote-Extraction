# Automatic Pull Quote Selection
_Learning_ to automatically select pull quotes [(wikipedia)](https://en.wikipedia.org/wiki/Pull_quote).

This code accompanies the accepted COLING-2020 paper [Catching Attention with Automatic Pull Quote Selection](https://arxiv.org/abs/2005.13263).

## Requirements
This project is written in Python3.6.9

The following non-default libraries are used:
* numpy 1.18.2
* sklearn 0.22.2.post1
* seaborn 0.9.0
* matplotlib 3.1.2
* scipy 1.4.1
* keras 2.3.0
* tensorflow 1.14.0
* sumy 0.8.1
* nltk 3.4.5
* textstat 0.6.0
* textblob 0.15.3
* sentence_transformers 0.2.5


## Preparing the dataset
To reproduce our dataset:

1. execute `bash setup.sh` to setup a Python environment
2. navigate to the `datasets/url_lists/` directory and unzip `url_lists.zip` so that the 4 files are in `datasets/url_lists/`
3. nagivate to `datasets/` and run `python3.6 construct_dataset.py source ../corpora/`.
   * source can be one of `intercept`, `ottawa-citizen`, `cosmo`, `national-post`, or `all`
   * the samples for a given source will be stored in `corpora/source/`
   * :warning: Update `settings.py` so that `base_pq_directory` points to `corpora/`.
   * :warning: This will take a long time. (2-3 days)
4. navigate to the root repo folder and run `python3.6 calculate_data_stats.py` to calculate dataset statistics to compare with our paper.
5. run `python3.6 construct_encodings.py`
   * :worning: This will take a long time. (~1 day)
6. run `python3.6 aggregate_encodings.py` and `mv precomputed_pq_sentbert.pkl ./ml_data/`
   * :warning: This file will be about 2GB in size.

## Reproducing experiments
To reproduce our experimental results, run `bash run_experiments.sh` (output will be stored in `/results`).

:information_source: To first make sure that things work, run `bash run_experiments.sh --quick`. It should take just a few minutes.

## Miscellaneous

To reproduce the handcrafted feature value distribution figures, run `python3.6 view_feature_dists.py`

To analyze test articles with a all models, run `bash generate_model_samples.sh`. The `--quick` argument can similarly be used to make sure things are working.
