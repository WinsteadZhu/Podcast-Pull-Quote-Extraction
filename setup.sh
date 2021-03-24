# Create Python environment
pyenv virtualenv 3.6.10 pull-quotes.3.6.10
pyenv local pull-quotes.3.6.10
pip install --upgrade pip
pip install -r requirements.txt

# Setup NLTK
python -m textblob.download_corpora

# Create save dir to store corpora
mkdir corpora

# Create save dir to store encodings
mkdir ml_data

# Create save dir to store models
mkdir ml_models

# Get the movie quotes data
curl https://www.cs.cornell.edu/\~cristian/memorability_files/cornell_movie_quotes_corpus.zip --output datasets/cornell_movie_quotes_corpus.zip
unzip cornell_movie_quotes_corpus.zip -x __MACOSX/\* -d cornell_movie_quotes_data
