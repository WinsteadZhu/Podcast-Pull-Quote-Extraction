import pandas as pd

from datasets.scrapers.utils import clean_text, get_sentences
from models.sentence_encoders import SentBERTEncoder
from models.FlexiblePQModel import FlexiblePQModel
import settings


query = """
WITH
  segment AS (
  SELECT
    episode_uri,
    unnested.segment AS segment
  FROM
    `tr-research.podcast_transcripts_trec.transcripts`,
    UNNEST(transcription_segments) AS unnested)
SELECT
  episode_uri,
  ARRAY_TO_STRING(ARRAY_AGG(segment.segment), ' ') AS transcript
FROM
  segment
GROUP BY
  episode_uri
LIMIT 10
"""

print("loading sentences")
df = pd.read_gbq(query=query, project_id="acmacquisition", dialect="standard")
df["sentences"] = df["transcript"].map(clean_text).map(lambda t: get_sentences([t]))

print("loading model")
pq_model = FlexiblePQModel(sent_encoder=SentBERTEncoder(), mode="C_deep")
pq_model.load_model(settings.MODEL_SAVE_DIR + "flexible_C_deep_0_32_4_2.keras")

print("running model")
df["locations"] = df["sentences"].map(pq_model.predict_article)
df["argmax"] = df["locations"].map(lambda s: s.argmax())
df["sentence_max"] = df.apply(lambda row: row["sentences"][row["argmax"]], axis=1)
df["location_max"] = df.apply(lambda row: row["locations"][row["argmax"]], axis=1)

df[["episode_uri", "argmax", "sentence_max", "location_max"]].to_gbq(project_id="acmacquisition", location="EU", destination_table="test_ctang.pull_quotes")