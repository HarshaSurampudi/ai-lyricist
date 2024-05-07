import pandas as pd
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import PointStruct
import uuid
from embedding import get_embedding                                

df = pd.read_csv('sirivennela_lyrics.csv')
df = df[['url','song', 'lyrics', 'lyrics_en', 'instructions']]

client = QdrantClient(url="http://localhost:6333")


client.recreate_collection(
    collection_name="instructions",
    vectors_config=VectorParams(size=768, distance=Distance.COSINE),
)

points = []

for idx, row in df.iterrows():
    print("Indexing song: ", row['song'])
    vector = get_embedding(row['instructions'])
    points.append(PointStruct(
        id=str(uuid.uuid4()),
        vector=vector,
        payload={"url": row['url'], "lyrics": row['lyrics'], "instructions": row['instructions'], "lyrics_en": row['lyrics_en']}
    ))


client.upsert(
    collection_name="instructions",
    points=points
)